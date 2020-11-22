# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ScrapedData


class AddData(APIView):
    def post(self, request, format=None):
        data = {}
        try:
            application_name = request.POST.get('application_name', None)
            category_the_app_belongs = request.POST.get('category_the_app_belongs', None)
            overall_user_rating_of_the_app = request.POST.get('overall_user_rating_of_the_app', None)
            number_of_user_reviews_for_the_app = request.POST.get('number_of_user_reviews_for_the_app', None)
            size_of_the_app = request.POST.get('size_of_the_app', None)
            number_of_user_downloads_installs_for_the_app = request.POST.get(
                'number_of_user_downloads_installs_for_the_app', None)
            paid_or_free = request.POST.get('paid_or_free', None)
            price_of_the_app = request.POST.get('price_of_the_app', None)
            age_group_the_app_is_targeted_at_children_mature_adult = request.POST.get(
                'age_group_the_app_is_targeted_at_children_mature_adult', None)
            an_app_can_belong_to_multiple_genres = request.POST.get('an_app_can_belong_to_multiple_genres', None)

            try:
                add_to_db = ScrapedData.objects.get_or_create(application_name=application_name)
                add_to_db.category_the_app_belongs = category_the_app_belongs
                add_to_db.overall_user_rating_of_the_app = overall_user_rating_of_the_app
                add_to_db.number_of_user_reviews_for_the_app = number_of_user_reviews_for_the_app
                add_to_db.size_of_the_app = size_of_the_app
                add_to_db.number_of_user_downloads_installs_for_the_app = number_of_user_downloads_installs_for_the_app
                add_to_db.paid_or_free = paid_or_free
                add_to_db.price_of_the_app = price_of_the_app
                add_to_db.age_group_the_app_is_targeted_at_children_mature_adult = age_group_the_app_is_targeted_at_children_mature_adult
                add_to_db.an_app_can_belong_to_multiple_genres = an_app_can_belong_to_multiple_genres
                add_to_db.save()

                data['RESULT'] = "Data has been added to database."
            except Exception as error:
                data['RESULT'] = str(error)

            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={
                'RESULT': str(error)
            }, status=status.HTTP_200_OK)


class SendData(APIView):
    def get(self, request, format=None):
        try:
            data = {}
            number = int(request.POST.get('number', None))
            try:
                from_db = ScrapedData.objects.all()[number]
                data['application_name'] = from_db.application_name
                data['category_the_app_belongs'] = from_db.category_the_app_belongs
                data['overall_user_rating_of_the_app'] = from_db.overall_user_rating_of_the_app
                data['number_of_user_reviews_for_the_app'] = from_db.number_of_user_reviews_for_the_app
                data['size_of_the_app'] = from_db.size_of_the_app
                data[
                    'number_of_user_downloads_installs_for_the_app'] = from_db.number_of_user_downloads_installs_for_the_app
                data['paid_or_free'] = from_db.paid_or_free
                data['price_of_the_app'] = from_db.price_of_the_app
                data[
                    'age_group_the_app_is_targeted_at_children_mature_adult'] = from_db.age_group_the_app_is_targeted_at_children_mature_adult
                data['an_app_can_belong_to_multiple_genres'] = from_db.an_app_can_belong_to_multiple_genres
                data['RESULT'] = 'DATA SENT.'
            except Exception as error:
                data['RESULT'] = str(error)

            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={
                'RESULT': str(error)
            }, status=status.HTTP_200_OK)
