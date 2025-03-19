from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def locator(request):
    return render(request, 'locator.html')

def crisis_map(request):
    return render(request, 'crisis_map.html')

def alerts(request):
    return render(request, 'alerts.html')

def signin(request):
    return render(request, 'sign-in.html')