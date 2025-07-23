from django import forms
from .models import *

class OrganizationalChartForm(forms.ModelForm):
    class Meta:
        model = OrganizationalChart
        fields = '__all__'

class CompetencyModelForm(forms.ModelForm):
    class Meta:
        model = CompetencyModel
        fields = '__all__'

class PerformanceAppraisalForm(forms.ModelForm):
    class Meta:
        model = PerformanceAppraisal
        fields = '__all__'

class KPIDashboardForm(forms.ModelForm):
    class Meta:
        model = KPIDashboard
        fields = '__all__'

class OKRForm(forms.ModelForm):
    class Meta:
        model = OKR
        fields = '__all__'
