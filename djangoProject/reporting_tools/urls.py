from django.urls import path
from . import views

urlpatterns = [
    path('balanced-scorecard/', views.balanced_scorecard_view, name='balanced_scorecard'),
    path('benchmarking/', views.benchmarking_view, name='benchmarking'),
    path('gap-analysis/', views.gap_analysis_view, name='gap_analysis'),
    path('risk-matrix/', views.risk_matrix_view, name='risk_matrix'),
]
