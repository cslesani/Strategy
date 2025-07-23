from django.db import models

class ProcessMapping(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SOP(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="روش اجرایی استاندارد را وارد کنید")
    created_at = models.DateTimeField(auto_now_add=True)

class LeanSixSigma(models.Model):
    tool_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ProjectManagement(models.Model):
    project_name = models.CharField(max_length=200)
    gantt_chart_url = models.URLField(blank=True)
    wbs_description = models.TextField(blank=True)
    critical_path_description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class KanbanScrum(models.Model):
    board_type = models.CharField(max_length=50, choices=[('Kanban', 'کانبان'), ('Scrum', 'اسکرام')])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
