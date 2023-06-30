from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('itinerary/', views.ItineraryView.as_view(), name='itinerary'),
]