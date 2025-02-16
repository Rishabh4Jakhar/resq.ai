from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

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

class CrisisEvent(models.Model):
    CRISIS_TYPES = [
        ('Earthquake', 'Earthquake'),
        ('Flood', 'Flood'),
        ('Fire', 'Fire'),
        ('Medical Emergency', 'Medical Emergency'),
        ('Resource Shortage', 'Resource Shortage'),
        ('Pandemic', 'Pandemic'),
        ('Other', 'Other')
    ]
    
    crisis_type = models.CharField(max_length=50, choices=CRISIS_TYPES)
    location = models.CharField(max_length=255)
    severity = models.IntegerField()  # 1 (Low) - 5 (Critical)
    timestamp = models.DateTimeField(auto_now_add=True)

class Alert(models.Model):
    crisis_event = models.ForeignKey(CrisisEvent, on_delete=models.CASCADE)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class SafetyInstruction(models.Model):
    crisis_type = models.CharField(max_length=50, choices=CrisisEvent.CRISIS_TYPES)
    dos = models.TextField()  # Safety steps to follow
    donts = models.TextField()  # Things to avoid
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

class UserManager(BaseUserManager):
    def create_user(self, name, password, age, gender, location, mobile_no, is_vendor=False, organization=None):
        if not name or not password:
            raise ValueError("Users must have a name and password.")
        user = self.model(
            name=name,
            age=age,
            gender=gender,
            location=location,
            mobile_no=mobile_no,
            is_vendor=is_vendor,
            organization=organization if is_vendor else None
        )
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)  # Hashed password
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")])
    location = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15, unique=True)
    
    is_vendor = models.BooleanField(default=False)
    organization = models.CharField(max_length=255, null=True, blank=True)  # Only for vendors
    
    objects = UserManager()

    USERNAME_FIELD = 'name'  # Login with name
    REQUIRED_FIELDS = ['password', 'age', 'gender', 'location', 'mobile_no']
    
    def __str__(self):
        return self.name