
from django.shortcuts import render
from .models import SolarAnalysis

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
