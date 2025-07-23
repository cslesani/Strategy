from django.db import models

class BalancedScorecard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Benchmarking(models.Model):
    title = models.CharField(max_length=200)
    benchmark_subject = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class GapAnalysis(models.Model):
    title = models.CharField(max_length=200)
    current_state = models.TextField()
    desired_state = models.TextField()
    gaps = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class RiskMatrix(models.Model):
    title = models.CharField(max_length=200)
    risk_description = models.TextField()
    likelihood = models.IntegerField()
    impact = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
