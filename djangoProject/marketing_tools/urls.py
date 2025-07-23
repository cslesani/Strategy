from django.urls import path
from . import views

urlpatterns = [
    path('persona/', views.customer_persona_view, name='customer_persona'),
    path('journey/', views.customer_journey_view, name='customer_journey'),
    path('funnel/', views.sales_funnel_view, name='sales_funnel'),
    path('plan/', views.marketing_plan_view, name='marketing_plan'),
    path('mix/', views.marketing_mix_view, name='marketing_mix'),
    path('digital/', views.digital_marketing_view, name='digital_marketing'),
]
