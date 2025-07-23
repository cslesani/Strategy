from django.shortcuts import render, redirect
from .models import *
from .forms import *

# ------------------------ Budgeting ------------------------
def budgeting_list(request):
    items =BudgetingTool.objects.all()
    form = BudgetingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('financial_tools:budgeting_list')

    return render(request, 'finance_tools/budgeting.html', {
        'form': form,
        'items': items  # فقط ارسال کن، نیازی به محاسبه دستی نیست
    })



# ------------------------ Cash Flow ------------------------
def cashflow_list(request):
    items = CashFlowForecast.objects.all()
    form = CashFlowForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('cashflow_forecast')

    for item in items:
        item.net_cash = item.net_cash_flow
        item.status_label = item.status

    return render(request, 'finance_tools/cashflow.html', {
        'form': form,
        'items': items,
    })


# ------------------------ Break-Even ------------------------
def break_even_list(request):
    items = BreakEvenAnalysis.objects.all()
    form = BreakEvenForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('break_even')

    for item in items:
        item.break_even_units_value = item.break_even_units

    return render(request, 'finance_tools/break_even.html', {
        'form': form,
        'items': items,
    })


# ------------------------ ROI & Payback ------------------------
def roi_list(request):
    items = ROITool.objects.all()
    form = ROIForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('roi_payback')

    for item in items:
        item.roi_value = item.roi * 100  # Convert to percentage
        item.payback_value = item.payback_period

    return render(request, 'finance_tools/roi.html', {
        'form': form,
        'items': items,
    })


# ------------------------ Valuation Models ------------------------
def valuation_list(request):
    items = ValuationModel.objects.all()
    form = ValuationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('valuation')

    for item in items:
        item.dcf_val = item.dcf_value
        item.multiple_val = item.multiple_value

    return render(request, 'finance_tools/valuation.html', {
        'form': form,
        'items': items,
    })
