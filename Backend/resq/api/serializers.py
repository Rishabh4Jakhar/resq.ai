from rest_framework import serializers
from .models import Hospital, ReliefCenter, Shelter, Alert, MedicineStock, FoodResource, ReliefTeam, Volunteer, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'age', 'gender', 'location', 'mobile_no', 'is_vendor', 'organization']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'password', 'age', 'gender', 'location', 'mobile_no', 'is_vendor', 'organization']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

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
