# Create your models here.
from django.contrib.gis.db import models


class MonitoringStation(models.Model):
    ALERT_TYPES = (
        ('fire', 'Fire'),
        ('wildlife', 'Wildlife'),
    )

    name = models.CharField(max_length=100)
    location = models.PointField()
    description = models.TextField(blank=True, null=True)
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPES, default='wildlife')
    country = models.CharField(max_length=100)  # Added field

    def __str__(self):
        return self.name


class Alert(models.Model):
    ALERT_TYPES = [
        ('illegal_logging', 'Illegal Logging'),
        ('wildlife_trafficking', 'Endangered Species Trafficking'),
        ('wildfire', 'Wildfire'),
        ('habitat_destruction', 'Habitat Destruction'),
    ]
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPES)

    def __str__(self):
        return f"{self.title} in {self.location} on {self.date}"
