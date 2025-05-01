
from django.db import models

class Panel(models.Model):
    panel_id = models.CharField(max_length=50, unique=True)
    manufacturer = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    power_rating = models.FloatField(help_text="Watt cinsinden güç değeri")
    installation_date = models.DateField()
    current_efficiency = models.FloatField()
    last_maintenance = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.manufacturer} - {self.model_name} ({self.panel_id})"

class SolarAnalysis(models.Model):
    location = models.CharField(max_length=100)
    panel_efficiency = models.FloatField()
    panel_area = models.FloatField()
    solar_radiation = models.FloatField()
    temperature = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    panel = models.ForeignKey(Panel, on_delete=models.CASCADE, null=True, blank=True)

    def calculate_power(self):
        return self.panel_efficiency * self.panel_area * self.solar_radiation

    def __str__(self):
        return f"Solar Analysis for {self.location}"

class Inverter(models.Model):
    name = models.CharField(max_length=100)
    power_rating = models.FloatField(help_text="kW cinsinden güç değeri")
    efficiency = models.FloatField(help_text="Verimlilik yüzdesi")
    installation_date = models.DateField()
    last_maintenance = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.power_rating}kW)"
