from django.shortcuts import render, get_object_or_404
from .models import Service

def home(request):
    services = Service.objects.all()
    return render(request, 'car_service/home.html', {'services': services})

def service_detail(request, id):
    service = get_object_or_404(Service, id=id)
    return render(request, 'car_service/service_detail.html', {'service': service})

def closed_orders(request):
    all_services = Service.objects.all()
    allowed_brands = ['Toyota', 'Mazda', 'Honda', 'Nissan']
    closed_services = [i for i in all_services if i.car_model.startswith(tuple(allowed_brands))]
    return render(request, 'car_service/closed_orders.html', {'closed_services': closed_services})