from django.urls import path
from . import views

urlpatterns = [
    path('process-mapping/', views.process_mapping_view, name='process_mapping'),
    path('sop/', views.sop_view, name='sops'),
    path('lean-six-sigma/', views.lean_six_sigma_view, name='quality_tools'),
    path('project-management/', views.project_management_view, name='project_management'),
    path('kanban-scrum/', views.kanban_scrum_view, name='kanban_scrum'),
]
