from django.shortcuts import render, redirect
from .models import *
from .forms import *

def organizational_chart_view(request):
    if request.method == 'POST':
        form = OrganizationalChartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizational_chart')
    else:
        form = OrganizationalChartForm()
    items = OrganizationalChart.objects.all()
    return render(request, 'hr_tools/organizational_chart.html', {'form': form, 'items': items})


def competency_model_view(request):
    if request.method == 'POST':
        form = CompetencyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('competency_model')
    else:
        form = CompetencyModelForm()
    items = CompetencyModel.objects.all()
    return render(request, 'hr_tools/competency_model.html', {'form': form, 'items': items})


def performance_appraisal_view(request):
    if request.method == 'POST':
        form = PerformanceAppraisalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_appraisal')
    else:
        form = PerformanceAppraisalForm()
    items = PerformanceAppraisal.objects.all()
    return render(request, 'hr_tools/performance_appraisal.html', {'form': form, 'items': items})


def kpi_dashboard_view(request):
    if request.method == 'POST':
        form = KPIDashboardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kpi_dashboard')
    else:
        form = KPIDashboardForm()
    items = KPIDashboard.objects.all()
    return render(request, 'hr_tools/kpi_dashboard.html', {'form': form, 'items': items})


def okr_view(request):
    if request.method == 'POST':
        form = OKRForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('okr')
    else:
        form = OKRForm()
    items = OKR.objects.all()
    return render(request, 'hr_tools/okr.html', {'form': form, 'items': items})
