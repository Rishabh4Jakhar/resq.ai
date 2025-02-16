from rest_framework import serializers
from .models import Hospital, ReliefCenter, Shelter, Alert

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