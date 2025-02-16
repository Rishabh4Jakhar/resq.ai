from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HospitalViewSet, ReliefCenterViewSet, ShelterViewSet, AlertViewSet, predict_bed_shortage_view

router = DefaultRouter()
router.register('hospital', HospitalViewSet)
router.register('relief_center', ReliefCenterViewSet)
router.register('shelter', ShelterViewSet)
router.register('alert', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ai/predict_bed_shortage', predict_bed_shortage_view),
]
