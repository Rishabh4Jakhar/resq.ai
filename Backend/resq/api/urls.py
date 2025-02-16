from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, ReliefCenterViewSet, ShelterViewSet, AlertViewSet, predict_bed_shortage_view, MedicineStockViewSet, FoodResourceViewSet, ReliefTeamViewSet, VolunteerViewSet

router = DefaultRouter()
router.register('hospital', HospitalViewSet)
router.register('relief_center', ReliefCenterViewSet)
router.register('shelter', ShelterViewSet)
router.register('alert', AlertViewSet)
router.register('medicine_stock', MedicineStockViewSet)
router.register('food_resource', FoodResourceViewSet)
router.register('relief_team', ReliefTeamViewSet)
router.register('volunteer', VolunteerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ai/predict_bed_shortage', predict_bed_shortage_view),
]
