from django.urls import path
from . import views

urlpatterns = [
    path('organizational-chart/', views.organizational_chart_view, name='org_chart'),
    path('competency-model/', views.competency_model_view, name='competency_models'),
    path('performance-appraisal/', views.performance_appraisal_view, name='performance_appraisal'),
    path('kpi-dashboard/', views.kpi_dashboard_view, name='kpi_dashboard'),
    path('okr/', views.okr_view, name='okr_framework'),
]
