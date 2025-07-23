from django.urls import path
from . import views

urlpatterns = [
    path('budgeting/', views.budgeting_list, name='budgeting'),
    path('cashflow/', views.cashflow_list, name='cashflow_forecast'),
    path('break-even/', views.break_even_list, name='break_even'),
    path('roi/', views.roi_list, name='roi_payback'),
    path('valuation/', views.valuation_list, name='valuation_models'),
]
