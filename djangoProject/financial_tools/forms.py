# financial_tools/forms.py

from django import forms
from .models import *

class BudgetingForm(forms.ModelForm):
    class Meta:
        model = BudgetingTool
        fields = '__all__'

class CashFlowForm(forms.ModelForm):
    class Meta:
        model = CashFlowForecast
        fields = '__all__'

class BreakEvenForm(forms.ModelForm):
    class Meta:
        model = BreakEvenAnalysis
        fields = '__all__'

class ROIForm(forms.ModelForm):
    class Meta:
        model = ROITool
        fields = '__all__'

class ValuationForm(forms.ModelForm):
    class Meta:
        model = ValuationModel
        fields = '__all__'
