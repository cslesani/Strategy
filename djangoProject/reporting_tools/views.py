from django.shortcuts import render, redirect
from .models import *
from .forms import *

def balanced_scorecard_view(request):
    if request.method == 'POST':
        form = BalancedScorecardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('balanced_scorecard')
    else:
        form = BalancedScorecardForm()
    items = BalancedScorecard.objects.all()
    return render(request, 'reporting_tools/balanced_scorecard.html', {'form': form, 'items': items})

def benchmarking_view(request):
    if request.method == 'POST':
        form = BenchmarkingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('benchmarking')
    else:
        form = BenchmarkingForm()
    items = Benchmarking.objects.all()
    return render(request, 'reporting_tools/benchmarking.html', {'form': form, 'items': items})

def gap_analysis_view(request):
    if request.method == 'POST':
        form = GapAnalysisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gap_analysis')
    else:
        form = GapAnalysisForm()
    items = GapAnalysis.objects.all()
    return render(request, 'reporting_tools/gap_analysis.html', {'form': form, 'items': items})

def risk_matrix_view(request):
    if request.method == 'POST':
        form = RiskMatrixForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('risk_matrix')
    else:
        form = RiskMatrixForm()
    items = RiskMatrix.objects.all()
    return render(request, 'reporting_tools/risk_matrix.html', {'form': form, 'items': items})
