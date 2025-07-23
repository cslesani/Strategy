from django import forms
from .models import *

class BalancedScorecardForm(forms.ModelForm):
    class Meta:
        model = BalancedScorecard
        fields = '__all__'

class BenchmarkingForm(forms.ModelForm):
    class Meta:
        model = Benchmarking
        fields = '__all__'

class GapAnalysisForm(forms.ModelForm):
    class Meta:
        model = GapAnalysis
        fields = '__all__'

class RiskMatrixForm(forms.ModelForm):
    class Meta:
        model = RiskMatrix
        fields = '__all__'
