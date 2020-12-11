from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Sport
from .serializers import SportSerializer

# Create your views here.
class SportView(APIView):
    def get(self,request):
        queryset = Sport.objects.all()
        serializer = SportSerializer(queryset, many=True)
        return Response(serializer.data)