from django.contrib import admin
from django.urls import path
from .views import home, dashboard, locator, crisis_map, alerts, signin

urlpatterns = [
    path('', home, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('locator/', locator, name='locator'),
    path('crisis-map/', crisis_map, name='crisis_map'),
    path('alerts/', alerts, name='alerts'),
    path('signin/', signin, name='signin'),
]
