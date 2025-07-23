from django.shortcuts import render, redirect
from .models import *
from .forms import *

def process_mapping_view(request):
    if request.method == 'POST':
        form = ProcessMappingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('process_mapping')
    else:
        form = ProcessMappingForm()
    items = ProcessMapping.objects.all()
    return render(request, 'ops_tools/process_mapping.html', {'form': form, 'items': items})

def sop_view(request):
    if request.method == 'POST':
        form = SOPForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sop')
    else:
        form = SOPForm()
    items = SOP.objects.all()
    return render(request, 'ops_tools/sop.html', {'form': form, 'items': items})

def lean_six_sigma_view(request):
    if request.method == 'POST':
        form = LeanSixSigmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lean_six_sigma')
    else:
        form = LeanSixSigmaForm()
    items = LeanSixSigma.objects.all()
    return render(request, 'ops_tools/lean_six_sigma.html', {'form': form, 'items': items})

def project_management_view(request):
    if request.method == 'POST':
        form = ProjectManagementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_management')
    else:
        form = ProjectManagementForm()
    items = ProjectManagement.objects.all()
    return render(request, 'ops_tools/project_management.html', {'form': form, 'items': items})

def kanban_scrum_view(request):
    if request.method == 'POST':
        form = KanbanScrumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanban_scrum')
    else:
        form = KanbanScrumForm()
    items = KanbanScrum.objects.all()
    return render(request, 'ops_tools/kanban_scrum.html', {'form': form, 'items': items})
