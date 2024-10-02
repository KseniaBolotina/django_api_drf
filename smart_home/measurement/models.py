from django.db import models
class Sensor(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.name

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.temperature}, {self.created_at}"