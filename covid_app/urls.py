from django.urls import path

from .views import CovidListCreateView,CovidDetailView,allCountries,CountryCases

urlpatterns= [
    path('',CovidListCreateView.as_view()),
    path('allCountries/',allCountries.as_view()),
    path('countryCases/',CountryCases.as_view()),
    path('<pk>',CovidDetailView.as_view()),
]