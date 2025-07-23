from django.shortcuts import render, redirect
from .models import *
from .forms import *

def customer_persona_view(request):
    if request.method == 'POST':
        form = CustomerPersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_persona')
    else:
        form = CustomerPersonaForm()
    items = CustomerPersona.objects.all()
    return render(request, 'marketing_tools/customer_persona.html', {'form': form, 'items': items})


def customer_journey_view(request):
    if request.method == 'POST':
        form = CustomerJourneyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_journey')
    else:
        form = CustomerJourneyForm()
    items = CustomerJourney.objects.all()
    return render(request, 'marketing_tools/customer_journey.html', {'form': form, 'items': items})


def sales_funnel_view(request):
    if request.method == 'POST':
        form = SalesFunnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_funnel')
    else:
        form = SalesFunnelForm()
    items = SalesFunnel.objects.all()
    return render(request, 'marketing_tools/sales_funnel.html', {'form': form, 'items': items})


def marketing_plan_view(request):
    if request.method == 'POST':
        form = MarketingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketing_plan')
    else:
        form = MarketingPlanForm()
    items = MarketingPlan.objects.all()
    return render(request, 'marketing_tools/marketing_plan.html', {'form': form, 'items': items})


def marketing_mix_view(request):
    if request.method == 'POST':
        form = MarketingMixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('marketing_mix')
    else:
        form = MarketingMixForm()
    items = MarketingMix.objects.all()
    return render(request, 'marketing_tools/marketing_mix.html', {'form': form, 'items': items})


def digital_marketing_view(request):
    if request.method == 'POST':
        form = DigitalMarketingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('digital_marketing')
    else:
        form = DigitalMarketingForm()
    items = DigitalMarketing.objects.all()
    return render(request, 'marketing_tools/digital_marketing.html', {'form': form, 'items': items})
