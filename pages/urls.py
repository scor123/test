from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from .views import ServicesPageView
from .views import BasePageView


urlpatterns =[
    path('',HomePageView.as_view(),name="home"),
path('base/',BasePageView.as_view(),name="base"),
    path('about/',AboutPageView.as_view(),name="about"),
    path('services/', ServicesPageView.as_view(), name="services")

]

