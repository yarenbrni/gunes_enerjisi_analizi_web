
from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_form, name='analysis_form'),
]
