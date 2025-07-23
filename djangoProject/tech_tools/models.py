from django.db import models

class ERPSystem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    vendor = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CRMSystem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    version = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class BIDashboard(models.Model):
    title = models.CharField(max_length=200)
    data_sources = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class DataAnalyticsTool(models.Model):
    name = models.CharField(max_length=100)
    purpose = models.TextField()
    language = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # Frontend, Backend, DevOps, etc.
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
