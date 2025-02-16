from django.db import models
from django.contrib.auth.models import User 

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

class MedicineStock(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medicine_name}: {self.quantity} at {self.hospital.name}"

class FoodResource(models.Model):
    relief_center = models.CharField(max_length=255)
    food_type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.food_type}: {self.quantity} at {self.relief_center}"

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
    
class ReliefTeam(models.Model):
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    availability_status = models.CharField(max_length=50, choices=[("Available", "Available"), ("Busy", "Busy")])
    last_updated = models.DateTimeField(auto_now=True)

class Volunteer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Verified personnel
    full_name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    skills = models.CharField(max_length=255)
    availability_status = models.CharField(max_length=50, choices=[("Available", "Available"), ("Busy", "Busy")])
    last_updated = models.DateTimeField(auto_now=True)
    
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

class Resource(models.Model):
    name = models.CharField(max_length=255)  # e.g., Oxygen, Medicine, Food
    quantity = models.IntegerField()  # Current stock level
    location = models.CharField(max_length=255)  # Warehouse/Hospital location
    last_updated = models.DateTimeField(auto_now=True)

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)  # e.g., Oxygen, Medicine
    reliability_score = models.FloatField()  # AI-generated rating
    response_time = models.FloatField()  # Avg delivery time in hours
    cost_efficiency = models.FloatField()  # AI-predicted cost efficiency

class SupplyChainLog(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)  # e.g., "Reallocated", "Shortage Detected"
    timestamp = models.DateTimeField(auto_now_add=True)