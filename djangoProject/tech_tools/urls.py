from django.urls import path
from . import views

urlpatterns = [
    path('erp/', views.erp_view, name='erp'),
    path('crm/', views.crm_view, name='crm'),
    path('bi-dashboard/', views.bi_dashboard_view, name='bi_dashboard'),
    path('data-analytics/', views.data_analytics_view, name='data_analytics'),
    #path('tech-stack/', views.tech_stack_view, name='tech_stack'),
]
