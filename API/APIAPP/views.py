from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class AddData(APIView):
    def post(self, request, format=None):
        try:
            data = {}
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={
                'error': str(error)
            }, status=status.HTTP_200_OK)


class SendData(APIView):
    def get(self, request, format=None):
        try:
            data = {}
            return Response(data=data, status=status.HTTP_200_OK)
        except Exception as error:
            return Response(data={
                'error': str(error)
            }, status=status.HTTP_200_OK)
