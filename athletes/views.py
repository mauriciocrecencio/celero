from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Athlete, Athlete_instance
from .serializers import AthleteSerializer, AthleteInstanceSerializer

# Create your views here.
class AthleteView(APIView):
    def get(self,request):
        queryset = Athlete.objects.all()
        serializer = AthleteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    # def post(self,request):
    #     athlete = Athlete.objects.create(**kwargs)
    #     serializer = AthleteSerializer(athlete)
    #     return Response(serializer.data)

    # # def patch(self,request):


    # def delete(self, request, pk):
    #     athlete = Athlete.objects.get(id=pk)
    #     athlete.delete()
    #     return Response(status=status.HTTP_200_OK)

class AthleteInstanceView(APIView):
    def get(self,request):
        queryset = Athlete_instance.objects.all()
        serializer = AthleteInstanceSerializer(queryset, many=True)
        return Response(serializer.data)