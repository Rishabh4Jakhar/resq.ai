from django.shortcuts import render
from rest_framework import viewsets
from .models import Hospital, ReliefCenter, Shelter, Alert
from .serializers import HospitalSerializer, ReliefCenterSerializer, ShelterSerializer, AlertSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import predict_bed_shortage

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class ReliefCenterViewSet(viewsets.ModelViewSet):
    queryset = ReliefCenter.objects.all()
    serializer_class = ReliefCenterSerializer

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer


@api_view(['GET'])
def predict_bed_shortage_view(request):
    bed_shortage = predict_bed_shortage()
    return Response({'bed_shortage': bed_shortage})