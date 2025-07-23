from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# ---------- SWOT ----------
def swot_index(request):
    swots = SWOT.objects.all().order_by('-created_at')
    form = SWOTForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        swot = form.save()
        return redirect('swot_detail', pk=swot.pk)
    return render(request, 'strategic_tools/swot.html', {'swots': swots, 'form': form})

def swot_detail(request, pk):
    swot = get_object_or_404(SWOT, pk=pk)

    strength_form = StrengthForm(request.POST or None, prefix='strength')
    weakness_form = WeaknessForm(request.POST or None, prefix='weakness')
    opportunity_form = OpportunityForm(request.POST or None, prefix='opportunity')
    threat_form = ThreatForm(request.POST or None, prefix='threat')

    if request.method == 'POST':
        if 'add_strength' in request.POST and strength_form.is_valid():
            s = strength_form.save(commit=False)
            s.swot = swot
            s.save()
            return redirect('swot_detail', pk=pk)

        elif 'add_weakness' in request.POST and weakness_form.is_valid():
            w = weakness_form.save(commit=False)
            w.swot = swot
            w.save()
            return redirect('swot_detail', pk=pk)

        elif 'add_opportunity' in request.POST and opportunity_form.is_valid():
            o = opportunity_form.save(commit=False)
            o.swot = swot
            o.save()
            return redirect('swot_detail', pk=pk)

        elif 'add_threat' in request.POST and threat_form.is_valid():
            t = threat_form.save(commit=False)
            t.swot = swot
            t.save()
            return redirect('swot_detail', pk=pk)

    return render(request, 'strategic_tools/swot_detail.html', {
        'swot': swot,
        'strength_form': strength_form,
        'weakness_form': weakness_form,
        'opportunity_form': opportunity_form,
        'threat_form': threat_form,
    })


# ---------- PESTEL ----------
def pestel_index(request):
    pestels = PESTEL.objects.all().order_by('-created_at')
    form = PESTELForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        pestel = form.save()
        return redirect('pestel_detail', pk=pestel.pk)
    return render(request, 'strategic_tools/pestel.html', {'form': form, 'pestels': pestels})

def pestel_detail(request, pk):
    pestel = get_object_or_404(PESTEL, pk=pk)
    form = PESTELFactorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        factor = form.save(commit=False)
        factor.pestel = pestel
        factor.save()
        return redirect('pestel_detail', pk=pk)
    return render(request, 'strategic_tools/pestel_detail.html', {'pestel': pestel, 'form': form})


# ---------- PORTER ----------
def porter_index(request):
    porters = Porter.objects.all().order_by('-created_at')
    form = PorterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        porter = form.save()
        return redirect('porter_detail', pk=porter.pk)
    return render(request, 'strategic_tools/porters.html', {'form': form, 'porters': porters})

def porter_detail(request, pk):
    porter = get_object_or_404(Porter, pk=pk)
    form = PorterFactorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        factor = form.save(commit=False)
        factor.porter = porter
        factor.save()
        return redirect('porter_detail', pk=pk)
    return render(request, 'strategic_tools/porter_detail.html', {'porter': porter, 'form': form})


# ---------- BCG ----------
def bcg_index(request):
    bcgs = BCG.objects.all().order_by('-created_at')
    form = BCGForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        bcg = form.save()
        return redirect('bcg_detail', pk=bcg.pk)
    return render(request, 'strategic_tools/bcg.html', {'form': form, 'bcgs': bcgs})

def bcg_detail(request, pk):
    bcg = get_object_or_404(BCG, pk=pk)
    form = BCGItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.bcg = bcg
        g, s = item.market_growth, item.market_share
        if g >= 0.5 and s >= 0.5:
            item.quadrant = 'Star'
        elif g < 0.5 and s >= 0.5:
            item.quadrant = 'CashCow'
        elif g >= 0.5 and s < 0.5:
            item.quadrant = 'QuestionMark'
        else:
            item.quadrant = 'Dog'
        item.save()
        return redirect('bcg_detail', pk=pk)
    items = bcg.items.all()
    return render(request, 'strategic_tools/bcg_detail.html', {'bcg': bcg, 'form': form, 'items': items})


# ---------- ANSOFF ----------
def ansoff_index(request):
    ansoffs = Ansoff.objects.all().order_by('-created_at')
    form = AnsoffForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        ansoff = form.save()
        return redirect('ansoff_detail', pk=ansoff.pk)
    return render(request, 'strategic_tools/ansoff.html', {'form': form, 'ansoffs': ansoffs})

def ansoff_detail(request, pk):
    ansoff = get_object_or_404(Ansoff, pk=pk)
    form = AnsoffItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.ansoff = ansoff
        item.save()
        return redirect('ansoff_detail', pk=pk)
    items = ansoff.items.all()
    return render(request, 'strategic_tools/ansoff_detail.html', {'ansoff': ansoff, 'form': form, 'items': items})


# ---------- CANVAS ----------
def canvas_index(request):
    canvases = Canvas.objects.all().order_by('-created_at')
    form = CanvasForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        canvas = form.save()
        return redirect('canvas_detail', pk=canvas.pk)
    return render(request, 'strategic_tools/canvas.html', {'form': form, 'canvases': canvases})

def canvas_detail(request, pk):
    canvas = get_object_or_404(Canvas, pk=pk)
    form = CanvasBlockForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        block = form.save(commit=False)
        block.canvas = canvas
        block.save()
        return redirect('canvas_detail', pk=pk)
    blocks = canvas.blocks.all()
    return render(request, 'strategic_tools/canvas_detail.html', {'canvas': canvas, 'form': form, 'blocks': blocks})


# ---------- VALUE PROPOSITION ----------
def valueprop_index(request):
    props = ValueProp.objects.all().order_by('-created_at')
    form = ValuePropForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        prop = form.save()
        return redirect('valueprop_detail', pk=prop.pk)
    return render(request, 'strategic_tools/valueprop.html', {'form': form, 'props': props})

def valueprop_detail(request, pk):
    prop = get_object_or_404(ValueProp, pk=pk)
    form = ValuePropositionItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.value_prop = prop
        item.save()
        return redirect('valueprop_detail', pk=pk)
    items = prop.items.all()
    return render(request, 'strategic_tools/valueprop_detail.html', {'prop': prop, 'form': form, 'items': items})
