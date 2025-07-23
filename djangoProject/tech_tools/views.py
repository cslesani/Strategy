from django.shortcuts import render, redirect
from .models import *
from .forms import *

def erp_view(request):
    form = ERPSystemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('erp')
    items = ERPSystem.objects.all()
    return render(request, 'tech_tools/erp.html', {'form': form, 'items': items})

def crm_view(request):
    form = CRMSystemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crm')
    items = CRMSystem.objects.all()
    return render(request, 'tech_tools/crm.html', {'form': form, 'items': items})

def bi_dashboard_view(request):
    form = BIDashboardForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bi_dashboard')
    items = BIDashboard.objects.all()
    return render(request, 'tech_tools/bi_dashboard.html', {'form': form, 'items': items})

def data_analytics_view(request):
    form = DataAnalyticsToolForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('data_analytics')
    items = DataAnalyticsTool.objects.all()
    return render(request, 'tech_tools/data_analytics.html', {'form': form, 'items': items})

def tech_stack_view(request):
    form = TechStackForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('tech_stack')
    items = TechStack.objects.all()
    return render(request, 'tech_tools/tech_stack.html', {'form': form, 'items': items})
