from django import forms
from .models import *

class CustomerPersonaForm(forms.ModelForm):
    class Meta:
        model = CustomerPersona
        fields = '__all__'

class CustomerJourneyForm(forms.ModelForm):
    class Meta:
        model = CustomerJourney
        fields = '__all__'

class SalesFunnelForm(forms.ModelForm):
    class Meta:
        model = SalesFunnel
        fields = '__all__'

class MarketingPlanForm(forms.ModelForm):
    class Meta:
        model = MarketingPlan
        fields = '__all__'

class MarketingMixForm(forms.ModelForm):
    class Meta:
        model = MarketingMix
        fields = '__all__'

class DigitalMarketingForm(forms.ModelForm):
    class Meta:
        model = DigitalMarketing
        fields = '__all__'
