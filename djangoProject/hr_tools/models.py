from django.db import models

class OrganizationalChart(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CompetencyModel(models.Model):
    title = models.CharField(max_length=200)
    competencies = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PerformanceAppraisal(models.Model):
    employee_name = models.CharField(max_length=200)
    appraisal_period = models.CharField(max_length=100)
    score = models.FloatField()
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class KPIDashboard(models.Model):
    title = models.CharField(max_length=200)
    kpis = models.TextField(help_text="شاخص‌ها را با کاما جدا کنید.")
    created_at = models.DateTimeField(auto_now_add=True)

class OKR(models.Model):
    objective = models.CharField(max_length=300)
    key_results = models.TextField(help_text="نتایج کلیدی را با خط فاصله یا عدد جدا کنید.")
    created_at = models.DateTimeField(auto_now_add=True)
