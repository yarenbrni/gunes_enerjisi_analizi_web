
from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_form, name='analysis_form'),
    path('panels/', views.panel_list, name='panel_list'),
    path('panel/<int:panel_id>/', views.panel_detail, name='panel_detail'),
]
