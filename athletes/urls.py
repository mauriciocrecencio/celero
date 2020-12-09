from django.urls import path
from .views import AthleteView

urlpatterns = [
    path('athletes/', AthleteView.as_view())
]