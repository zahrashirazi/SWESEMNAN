from django.db import models


# Create your models here.
class ScrapedData(models.Model):
    application_name = models.CharField(default='', blank=False, null=True, max_length=4200)
    category_the_app_belongs = models.CharField(default='', blank=False, null=True, max_length=4200)
    overall_user_rating_of_the_app = models.CharField(default='', blank=False, null=True, max_length=4200)
    number_of_user_reviews_for_the_app = models.CharField(default='', blank=False, null=True, max_length=4200)
    size_of_the_app = models.CharField(default='', blank=False, null=True, max_length=4200)
    number_of_user_downloads_installs_for_the_app = models.CharField(default='', blank=False, null=True,
                                                                     max_length=4200)
    paid_or_free = models.CharField(default='', blank=False, null=True, max_length=4200)
    price_of_the_app = models.CharField(default='', blank=False, null=True, max_length=4200)
    age_group_the_app_is_targeted_at_children_mature_adult = models.CharField(default='', blank=False, null=True,
                                                                              max_length=4200)
    an_app_can_belong_to_multiple_genres = models.CharField(default='', blank=False, null=True, max_length=4200)
