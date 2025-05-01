
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

def overview(request):
    panels = Panel.objects.all()
    total_power = sum(panel.power_rating for panel in panels)
    avg_efficiency = sum(panel.current_efficiency for panel in panels) / len(panels) if panels else 0
    
    context = {
        'total_panels': len(panels),
        'total_power': total_power,
        'avg_efficiency': avg_efficiency,
        'panels': panels
    }
    return render(request, 'solar_analysis/overview.html', context)

def inverter_analysis(request):
    inverters = Inverter.objects.all()
    years = range(2018, 2026)  # 2018-2025 yılları
    
    selected_inverter_id = request.GET.get('inverter')
    start_year = int(request.GET.get('start_year', 2018))
    end_year = int(request.GET.get('end_year', 2025))
    
    context = {
        'inverters': inverters,
        'years': years,
        'start_year': start_year,
        'end_year': end_year
    }
    
    if selected_inverter_id:
        selected_inverter = get_object_or_404(Inverter, id=selected_inverter_id)
        
        # Performans verilerini hesapla
        performance_data = {
            'avg_efficiency': 95.5,  # Örnek veri
            'total_hours': 8760 * (end_year - start_year + 1),  # Yıllık saat * yıl sayısı
        }
        
        context.update({
            'selected_inverter': selected_inverter.id,
            'selected_inverter_data': selected_inverter,
            'performance_data': performance_data
        })
    
    return render(request, 'solar_analysis/inverter_analysis.html', context)

def maintenance_prediction(request):
    panels = Panel.objects.all()
    for panel in panels:
        # Basit bir bakım tahmini algoritması
        efficiency_threshold = 85
        if panel.current_efficiency < efficiency_threshold:
            panel.maintenance_needed = True
        else:
            panel.maintenance_needed = False
    
    context = {
        'panels': panels
    }
    return render(request, 'solar_analysis/maintenance_prediction.html', context)

def statistics(request):
    return render(request, 'solar_analysis/statistics.html')

def settings(request):
    return render(request, 'solar_analysis/settings.html')
