from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets, permissions, status
from .models import Hospital, ReliefCenter, Shelter, Alert, MedicineStock, FoodResource, ReliefTeam, Volunteer
from .serializers import HospitalSerializer, ReliefCenterSerializer, ShelterSerializer, AlertSerializer, MedicineStockSerializer, FoodResourceSerializer, ReliefTeamSerializer, VolunteerSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import predict_bed_shortage, predict_shortages, suggest_alternative_suppliers

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    #permission_classes = [permissions.IsAuthenticated]

class ReliefCenterViewSet(viewsets.ModelViewSet):
    queryset = ReliefCenter.objects.all()
    serializer_class = ReliefCenterSerializer

class ShelterViewSet(viewsets.ModelViewSet):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer

class MedicineStockViewSet(viewsets.ModelViewSet):
    queryset = MedicineStock.objects.all()
    serializer_class = MedicineStockSerializer
    permission_classes = [permissions.IsAuthenticated]

class FoodResourceViewSet(viewsets.ModelViewSet):
    queryset = FoodResource.objects.all()
    serializer_class = FoodResourceSerializer
    permission_classes = [permissions.IsAuthenticated]

class ReliefTeamViewSet(viewsets.ModelViewSet):
    queryset = ReliefTeam.objects.all()
    serializer_class = ReliefTeamSerializer
    permission_classes = [permissions.IsAuthenticated]

class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def predict_bed_shortage_view(request):
    bed_shortage = predict_bed_shortage()
    return Response({'bed_shortage': bed_shortage})

@api_view(['GET', 'POST'])
def hospital_list(request):
    if request.method == 'GET':  # Fetch all hospitals
        hospitals = Hospital.objects.all()
        serializer = HospitalSerializer(hospitals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Save new hospital data
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def medicine_stock_list(request):
    if request.method == 'GET':  # Fetch medicine stock data
        medicines = MedicineStock.objects.all()
        serializer = MedicineStockSerializer(medicines, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':  # Save new medicine stock data
        serializer = MedicineStockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def ai_shortage_predictions(request):
    predictions = predict_shortages()
    return JsonResponse(predictions)

@api_view(['GET'])
def ai_supplier_suggestions(request, resource_name):
    suggestions = suggest_alternative_suppliers(resource_name)
    return JsonResponse({"suggestions": suggestions})


class SupplierSuggestionViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        suggestions = suggest_alternative_suppliers(pk)
        return Response({"suggestions": suggestions})
    
class ShortagePredictionViewSet(viewsets.ViewSet):
    def list(self, request):
        predictions = predict_shortages()
        return Response(predictions)

def home(request):
    return render(request, 'index.html')