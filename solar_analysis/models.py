
from django.db import models

class SolarAnalysis(models.Model):
    location = models.CharField(max_length=100)
    panel_efficiency = models.FloatField()
    panel_area = models.FloatField()
    solar_radiation = models.FloatField()
    temperature = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

    def calculate_power(self):
        return self.panel_efficiency * self.panel_area * self.solar_radiation

    def __str__(self):
        return f"Solar Analysis for {self.location}"
