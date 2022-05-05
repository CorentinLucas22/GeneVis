from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('about/', views.about_view, name='about'),
    path('request/', views.request_view, name='request'),
    path('request/result/', views.result_view, name='result'),
]

urlpatterns += staticfiles_urlpatterns()

# This file builds the URL patterns for the different views in this application.
