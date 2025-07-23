from django import forms
from .models import *

class ERPSystemForm(forms.ModelForm):
    class Meta:
        model = ERPSystem
        fields = '__all__'

class CRMSystemForm(forms.ModelForm):
    class Meta:
        model = CRMSystem
        fields = '__all__'

class BIDashboardForm(forms.ModelForm):
    class Meta:
        model = BIDashboard
        fields = '__all__'

class DataAnalyticsToolForm(forms.ModelForm):
    class Meta:
        model = DataAnalyticsTool
        fields = '__all__'

class TechStackForm(forms.ModelForm):
    class Meta:
        model = TechStack
        fields = '__all__'
