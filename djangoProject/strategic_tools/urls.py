from django.urls import path
from . import views

urlpatterns = [
    # SWOT
    path('', views.swot_index, name='swot'),
    path('<int:pk>/', views.swot_detail, name='swot_detail'),

    # PESTEL
    path('pestel/', views.pestel_index, name='pestel'),
    path('pestel/<int:pk>/', views.pestel_detail, name='pestel_detail'),

    # PORTER
    path('porter/', views.porter_index, name='porter'),
    path('porter/<int:pk>/', views.porter_detail, name='porter_detail'),

    # BCG
    path('bcg/', views.bcg_index, name='bcg'),
    path('bcg/<int:pk>/', views.bcg_detail, name='bcg_detail'),

    # ANSOFF
    path('ansoff/', views.ansoff_index, name='ansoff'),
    path('ansoff/<int:pk>/', views.ansoff_detail, name='ansoff_detail'),

    # CANVAS
    path('canvas/', views.canvas_index, name='canvas'),
    path('canvas/<int:pk>/', views.canvas_detail, name='canvas_detail'),

    # VALUE PROPOSITION
    path('valueprop/', views.valueprop_index, name='valueprop'),
    path('valueprop/<int:pk>/', views.valueprop_detail, name='valueprop_detail'),
]
