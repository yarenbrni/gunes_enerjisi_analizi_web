
from django.urls import path
from . import views

urlpatterns = [
    path('', views.analysis_form, name='analysis_form'),
    path('panels/', views.panel_list, name='panel_list'),
    path('panel/<int:panel_id>/', views.panel_detail, name='panel_detail'),
    path('overview/', views.overview, name='overview'),
    path('inverter-analysis/', views.inverter_analysis, name='inverter_analysis'),
    path('maintenance-prediction/', views.maintenance_prediction, name='maintenance_prediction'),
    path('statistics/', views.statistics, name='statistics'),
    path('settings/', views.settings, name='settings'),
]
