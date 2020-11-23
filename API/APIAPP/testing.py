import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "API.settings")
django.setup()

from rest_framework.test import APIClient


def add_tdd():
    client = APIClient()
    data = {
        'application_name': 'application_name',
        'category_the_app_belongs': 'category_the_app_belongs',
        'overall_user_rating_of_the_app': 'overall_user_rating_of_the_app',
        'number_of_user_reviews_for_the_app': 'number_of_user_reviews_for_the_app',
        'size_of_the_app': 'size_of_the_app',
        'number_of_user_downloads_installs_for_the_app': 'number_of_user_downloads_installs_for_the_app',
        'paid_or_free': 'paid_or_free',
        'price_of_the_app': 'price_of_the_app',
        'age_group_the_app_is_targeted_at_children_mature_adult': 'age_group_the_app_is_targeted_at_children_mature_adult',
        'an_app_can_belong_to_multiple_genres': 'an_app_can_belong_to_multiple_genres',
    }
    respond = client.post('/api/add', data)
    return respond


def get_tdd():
    client = APIClient()
    data = {
        'number': '1',
    }
    respond = client.get('/api/get', data)
    return respond
