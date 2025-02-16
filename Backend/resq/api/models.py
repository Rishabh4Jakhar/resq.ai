from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    location_link = models.CharField(max_length=255)
    total_beds = models.IntegerField()
    available_beds = models.IntegerField()
    icu_beds = models.IntegerField()
    ventilators = models.IntegerField()
    oxygen_supply = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ReliefCenter(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    location_link = models.CharField(max_length=255)
    food_stock = models.IntegerField()
    water_stock = models.IntegerField()
    medical_stock = models.IntegerField()
    volunteer_count = models.IntegerField()
    transport_count = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Shelter(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    location_link = models.CharField(max_length=255)
    total_capacity = models.IntegerField()
    available_capacity = models.IntegerField()
    food_stock = models.IntegerField()
    water_stock = models.IntegerField()
    medical_stock = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Alert(models.Model):
    ALERT_TYPES = [
        ('Oxygen Shortage', 'Oxygen Shortage'),
        ('Bed Full', 'Bed Full'),
        ('Food Shortage', 'Food Shortage'),
        ('Water Shortage', 'Water Shortage'),
        ('Medical Shortage', 'Medical Shortage'),
        ('Volunteer Required', 'Volunteer Required'),
        ('Transport Required', 'Transport Required'),
        ('Other', 'Other')
    ]
    
    alert_type = models.CharField(max_length=50, choices=ALERT_TYPES)
    location = models.CharField(max_length=255)
    location_link = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alert_type} at {self.location}"
