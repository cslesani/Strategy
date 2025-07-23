from django.db import models

class CustomerPersona(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(blank=True, null=True)
    occupation = models.CharField(max_length=200, blank=True)
    interests = models.TextField(blank=True)
    pain_points = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class CustomerJourney(models.Model):
    stage = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SalesFunnel(models.Model):
    stage = models.CharField(max_length=100)
    conversion_rate = models.FloatField(help_text="نرخ تبدیل به درصد")
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class MarketingPlan(models.Model):
    title = models.CharField(max_length=200)
    goals = models.TextField()
    target_audience = models.TextField()
    strategy = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MarketingMix(models.Model):
    type = models.CharField(max_length=10, choices=[('4P', '4P'), ('7P', '7P')])
    elements = models.TextField(help_text="هر مؤلفه را با خط فاصله جدا کنید.")
    created_at = models.DateTimeField(auto_now_add=True)

class DigitalMarketing(models.Model):
    tools = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=[
        ('SEO', 'SEO'), ('Ads', 'تبلیغات'), ('CRM', 'CRM'), ('Other', 'سایر')
    ])
    created_at = models.DateTimeField(auto_now_add=True)
