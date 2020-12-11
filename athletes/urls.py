from django.urls import path
from .views import AthleteView, AthleteInstanceView

urlpatterns = [
    path('athletes/', AthleteView.as_view()),
    path('athletes_instance/', AthleteInstanceView.as_view())
]