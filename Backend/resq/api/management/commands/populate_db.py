import random
from django.core.management.base import BaseCommand
from faker import Faker
from api.models import User, Hospital, MedicineStock, FoodResource, ReliefTeam, Volunteer, CrisisEvent, Alert, Supplier

fake = Faker()

class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Populating database...'))

        # ✅ Create Users (Normal + Vendors)
        for _ in range(10):
            is_vendor = fake.boolean()
            User.objects.create_user(
                name=fake.name(),
                password="password123",  # Simple password for testing
                age=random.randint(20, 60),
                gender=random.choice(["Male", "Female", "Other"]),
                location=fake.city(),
                mobile_no=fake.numerify("##########"),  # ✅ Generates a 10-digit number
                is_vendor=is_vendor,
                organization=fake.company() if is_vendor else None
            )

        # ✅ Create Hospitals
        hospitals = []
        for _ in range(5):
            hospital = Hospital.objects.create(
                name=fake.company() + " Hospital",
                location=fake.city(),
                location_link = fake.url(),
                total_beds=random.randint(50, 500),
                available_beds=random.randint(0, 50),
                icu_beds=random.randint(0, 20),
                ventilators=random.randint(0, 10),
                oxygen_supply=random.randint(0, 100),
            )
            hospitals.append(hospital)

        # ✅ Create Medicine Stock
        medicines = ["Paracetamol", "Insulin", "Aspirin", "Amoxicillin", "Metformin"]
        for hospital in hospitals:
            for med in medicines:
                MedicineStock.objects.create(
                    hospital=hospital,
                    medicine_name=med,
                    quantity=random.randint(0, 100)
                )

        # ✅ Create Food Resources
        foods = ["Rice", "Bread", "Milk", "Canned Food"]
        for _ in range(10):
            FoodResource.objects.create(
                relief_center=fake.city() + " Relief Center",
                food_type=random.choice(foods),
                quantity=random.randint(100, 1000)
            )

        # ✅ Create Relief Teams
        for _ in range(5):
            ReliefTeam.objects.create(
                name=fake.company() + " Team",
                organization=fake.company(),
                availability_status=random.choice(["Available", "Busy"])
            )

        # ✅ Fetch users as a list to avoid queryset issues
        users = list(User.objects.all())

        if not users:
            raise ValueError("No users found in the database. Please populate users first.")

        for _ in range(8):
            selected_user = random.choice(User.objects.all())  # ✅ Select user directly
            volunteer = Volunteer.objects.create(
                user=selected_user,  # ✅ Assign directly
                full_name=fake.name(),
                contact_info=fake.phone_number(),
                skills=random.choice(["Medical", "Logistics", "Rescue"]),
                availability_status=random.choice(["Available", "Busy"])
            )

        # ✅ Create Crisis Events
        crisis_types = ["Earthquake", "Flood", "Fire", "Medical Emergency", "Resource Shortage"]
        crisis_events = []
        for _ in range(5):
            crisis_event = CrisisEvent.objects.create(
                crisis_type=random.choice(crisis_types),
                location=fake.city(),
                severity=random.randint(1, 5)
            )
            crisis_events.append(crisis_event)

        # ✅ Create Alerts for Crisis Events
        for crisis in crisis_events:
            Alert.objects.create(
                crisis_event=crisis,
                message=f"Emergency alert: {crisis.crisis_type} detected in {crisis.location}!"
            )

        # ✅ Create Suppliers
        resources = ["Oxygen", "Medicine", "Food"]
        for _ in range(5):
            Supplier.objects.create(
                name=fake.company(),
                resource_type=random.choice(resources),
                reliability_score=random.uniform(1, 5),
                response_time=random.uniform(1, 24),
                cost_efficiency=random.uniform(0.5, 1.5)
            )

        self.stdout.write(self.style.SUCCESS('✅ Database populated successfully!'))
