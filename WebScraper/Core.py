import requests

from Scraper import Scraper

send_data_url = 'https://solfaplus.ir/api/add'
get_data_url = 'https://solfaplus.ir/api/get'


def get_data(number):
    data = {"number": str(number)}
    request = requests.post(url=get_data_url, data=data)
    return request.json()


def send_data(application_name,
              category_the_app_belongs,
              overall_user_rating_of_the_app,
              number_of_user_reviews_for_the_app,
              size_of_the_app,
              number_of_user_downloads_installs_for_the_app,
              paid_or_free,
              price_of_the_app,
              age_group_the_app_is_targeted_at_children_mature_adult,
              an_app_can_belong_to_multiple_genres):
    data = {
        'application_name': str(application_name),
        'category_the_app_belongs': str(category_the_app_belongs),
        'overall_user_rating_of_the_app': str(overall_user_rating_of_the_app),
        'number_of_user_reviews_for_the_app': str(number_of_user_reviews_for_the_app),
        'size_of_the_app': str(size_of_the_app),
        'number_of_user_downloads_installs_for_the_app': str(number_of_user_downloads_installs_for_the_app),
        'paid_or_free': str(paid_or_free),
        'price_of_the_app': str(price_of_the_app),
        'age_group_the_app_is_targeted_at_children_mature_adult': str(
            age_group_the_app_is_targeted_at_children_mature_adult),
        'an_app_can_belong_to_multiple_genres': str(an_app_can_belong_to_multiple_genres),

    }
    request = requests.post(url=send_data_url, data=data)
    return request.json()


sc = Scraper()
sc.scraper(number=50)
sc.driver.close()
for key, value in sc.data.items():
    send_data(
        application_name=str(key),
        category_the_app_belongs=str(value[0]),
        overall_user_rating_of_the_app=str(value[1]),
        number_of_user_reviews_for_the_app=str(value[2]),
        size_of_the_app=str(value[3]),
        number_of_user_downloads_installs_for_the_app=str(value[4]),
        paid_or_free=str(value[5]),
        price_of_the_app=str(value[6]),
        age_group_the_app_is_targeted_at_children_mature_adult=str(value[7]),
        an_app_can_belong_to_multiple_genres=str(value[8]),
    )
    print(key, value)
