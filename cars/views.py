from django.shortcuts import render, get_object_or_404
from .models import Car


def home(request):
    cars = Car.objects.all()

    fuel = request.GET.get("fuel")
    body = request.GET.get("body")

    if fuel:
        cars = cars.filter(fuel_type=fuel)

    if body:
        cars = cars.filter(body_type=body)

    context = {
        "cars": cars,
        "selected_fuel": fuel,
        "selected_body": body,
    }

    return render(request, "home.html", context)


def car_detail(request, car_id):
    car = get_object_or_404(
        Car,
        id=car_id,
        is_available=True
    )

    return render(
        request,
        "car_detail.html",
        {"car": car}
    )