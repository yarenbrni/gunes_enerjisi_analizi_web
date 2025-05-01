
from django.shortcuts import render, get_object_or_404
from .models import SolarAnalysis, Panel

def analysis_form(request):
    if request.method == 'POST':
        # Handle form submission
        analysis = SolarAnalysis(
            location=request.POST['location'],
            panel_efficiency=float(request.POST['efficiency']),
            panel_area=float(request.POST['area']),
            solar_radiation=float(request.POST['radiation']),
            temperature=float(request.POST['temperature'])
        )
        analysis.save()
        power = analysis.calculate_power()
        return render(request, 'solar_analysis/result.html', {'analysis': analysis, 'power': power})
    return render(request, 'solar_analysis/form.html')

def panel_list(request):
    panels = Panel.objects.all()
    return render(request, 'solar_analysis/panel_list.html', {'panels': panels})

def panel_detail(request, panel_id):
    panel = get_object_or_404(Panel, id=panel_id)
    analyses = panel.solaranalysis_set.all().order_by('-date_created')
    return render(request, 'solar_analysis/panel_detail.html', {
        'panel': panel,
        'analyses': analyses
    })
