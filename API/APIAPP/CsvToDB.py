import csv
from django.conf import settings
import API.settings as app_settings

settings.configure(INSTALLED_APPS=app_settings.INSTALLED_APPS, DATABASES=app_settings.DATABASES)
import django

django.setup()
from APIAPP.models import ScrapedData


def data_extractor():
    csv_reader = csv.reader(open('googleplaystore.csv', encoding="utf8"))
    data = {}
    for line in csv_reader:
        data[str(line[0])] = [
            str(line[1]),
            str(line[2]),
            str(line[3]),
            str(line[4]),
            str(line[5]),
            str(line[6]),
            str(line[7]),
            str(line[8]),
            str(line[9]),
        ]
    return data


for key, value in data_extractor().items():
    print(key, value)
    add_to_db, created = ScrapedData.objects.get_or_create(application_name=key)
    add_to_db.category_the_app_belongs = value[0]
    add_to_db.overall_user_rating_of_the_app = value[1]
    add_to_db.number_of_user_reviews_for_the_app = value[2]
    add_to_db.size_of_the_app = value[3]
    add_to_db.number_of_user_downloads_installs_for_the_app = value[4]
    add_to_db.paid_or_free = value[5]
    add_to_db.price_of_the_app = value[6]
    add_to_db.age_group_the_app_is_targeted_at_children_mature_adult = value[7]
    add_to_db.an_app_can_belong_to_multiple_genres = value[8]
    add_to_db.save()
