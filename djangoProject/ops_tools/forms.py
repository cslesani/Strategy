from django import forms
from .models import *

class ProcessMappingForm(forms.ModelForm):
    class Meta:
        model = ProcessMapping
        fields = '__all__'

class SOPForm(forms.ModelForm):
    class Meta:
        model = SOP
        fields = '__all__'

class LeanSixSigmaForm(forms.ModelForm):
    class Meta:
        model = LeanSixSigma
        fields = '__all__'

class ProjectManagementForm(forms.ModelForm):
    class Meta:
        model = ProjectManagement
        fields = '__all__'

class KanbanScrumForm(forms.ModelForm):
    class Meta:
        model = KanbanScrum
        fields = '__all__'
