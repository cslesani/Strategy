from django import forms
from .models import *

# ---------- SWOT ----------
class SWOTForm(forms.ModelForm):
    class Meta:
        model = SWOT
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان تحلیل'}),
        }

class StrengthForm(forms.ModelForm):
    class Meta:
        model = Strength
        fields = ['text', 'weight']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'متن قوت'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

class WeaknessForm(forms.ModelForm):
    class Meta:
        model = Weakness
        fields = ['text', 'weight']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'متن ضعف'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['text', 'weight']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'متن فرصت'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }

class ThreatForm(forms.ModelForm):
    class Meta:
        model = Threat
        fields = ['text', 'weight']
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'متن تهدید'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }


# ---------- PESTEL ----------
class PESTELForm(forms.ModelForm):
    class Meta:
        model = PESTEL
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان تحلیل'}),
        }

class PESTELFactorForm(forms.ModelForm):
    class Meta:
        model = PESTELFactor
        fields = ['category', 'text', 'weight']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'متن'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ---------- PORTER ----------
class PorterForm(forms.ModelForm):
    class Meta:
        model = Porter
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'عنوان تحلیل'}),
        }

class PorterFactorForm(forms.ModelForm):
    class Meta:
        model = PorterFactor
        fields = ['category', 'text', 'weight']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'توضیحات'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ---------- BCG ----------
class BCGForm(forms.ModelForm):
    class Meta:
        model = BCG
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BCGItemForm(forms.ModelForm):
    class Meta:
        model = BCGItem
        fields = ['name', 'market_growth', 'market_share']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'market_growth': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'market_share': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }


# ---------- ANSOFF ----------
class AnsoffForm(forms.ModelForm):
    class Meta:
        model = Ansoff
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AnsoffItemForm(forms.ModelForm):
    class Meta:
        model = AnsoffItem
        fields = ['name', 'strategy', 'weight']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'strategy': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ---------- CANVAS ----------
class CanvasForm(forms.ModelForm):
    class Meta:
        model = Canvas
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CanvasBlockForm(forms.ModelForm):
    class Meta:
        model = CanvasBlock
        fields = ['block_type', 'content', 'weight']
        widgets = {
            'block_type': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ---------- VALUE PROPOSITION ----------
class ValuePropForm(forms.ModelForm):
    class Meta:
        model = ValueProp
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ValuePropositionItemForm(forms.ModelForm):
    class Meta:
        model = ValuePropositionItem
        fields = ['customer_segment', 'gains', 'pains', 'products_services', 'weight']
        widgets = {
            'customer_segment': forms.TextInput(attrs={'class': 'form-control'}),
            'gains': forms.Textarea(attrs={'class': 'form-control'}),
            'pains': forms.Textarea(attrs={'class': 'form-control'}),
            'products_services': forms.Textarea(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
        }
