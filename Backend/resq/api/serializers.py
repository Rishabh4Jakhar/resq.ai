from rest_framework import serializers
from .models import Hospital, ReliefCenter, Shelter, Alert, MedicineStock, FoodResource, ReliefTeam, Volunteer

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class ReliefCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliefCenter
        fields = '__all__'

class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelter
        fields = '__all__'

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'

class MedicineStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineStock
        fields = '__all__'

class FoodResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodResource
        fields = '__all__'

class ReliefTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliefTeam
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteer
        fields = '__all__'
        