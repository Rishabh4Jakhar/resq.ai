from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, ReliefCenterViewSet, ShelterViewSet, AlertViewSet,ai_shortage_predictions, predict_bed_shortage_view, MedicineStockViewSet, FoodResourceViewSet, ReliefTeamViewSet, VolunteerViewSet, hospital_list, medicine_stock_list, ShortagePredictionViewSet

router = DefaultRouter()
router.register('hospital', HospitalViewSet)
router.register('relief_center', ReliefCenterViewSet)
router.register('shelter', ShelterViewSet)
router.register('alert', AlertViewSet)
router.register('medicine_stock', MedicineStockViewSet)
router.register('food_resource', FoodResourceViewSet)
router.register('relief_team', ReliefTeamViewSet)
router.register('volunteer', VolunteerViewSet)
#router.register('hospital_list', hospital_list, basename='hospital_list')
#router.register('medicine_stock_list', medicine_stock_list, basename='medicine_stock_list')
#router.register(r'ai/shortages', ShortagePredictionViewSet, basename='ai_shortage_predictions')
#router.register(r'ai/predict_bed_shortage', predict_bed_shortage_view, basename='predict_bed_shortage_view')

urlpatterns = [
    path('', include(router.urls)),
    path('ai/shortages/', ai_shortage_predictions, name="ai-shortages"),
]
