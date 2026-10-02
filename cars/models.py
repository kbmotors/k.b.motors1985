from django.db import models


class Car(models.Model):

    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG', 'CNG'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
    ]

    BODY_CHOICES = [
        ('SUV', 'SUV'),
        ('Sedan', 'Sedan'),
        ('Hatchback', 'Hatchback'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        ('MPV', 'MPV'),
    ]

    TRANSMISSION_CHOICES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('AMT', 'AMT'),
        ('DCT', 'DCT'),
        ('CVT', 'CVT'),
    ]

    brand = models.CharField(
        max_length=100
    )

    model_name = models.CharField(
        max_length=100
    )

    year = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_CHOICES
    )

    body_type = models.CharField(
        max_length=30,
        choices=BODY_CHOICES
    )

    transmission = models.CharField(
        max_length=30,
        choices=TRANSMISSION_CHOICES
    )

    mileage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text="Mileage in KM/L"
    )

    engine = models.CharField(
        max_length=100,
        blank=True
    )

    seats = models.PositiveIntegerField(
        default=5
    )

    description = models.TextField(
        blank=True
    )

    registration_number = models.CharField(
        max_length=50,
        blank=True
    )

    owner = models.CharField(
        max_length=100,
        blank=True
    )

    insurance_valid_upto = models.DateField(
        blank=True,
        null=True
    )

    # =========================
    # VEHICLE PHOTOS
    # =========================

    image_url = models.URLField(
        blank=True,
        null=True
    )

    image_url_2 = models.URLField(
        blank=True,
        null=True
    )

    image_url_3 = models.URLField(
        blank=True,
        null=True
    )

    image_url_4 = models.URLField(
        blank=True,
        null=True
    )

    image_url_5 = models.URLField(
        blank=True,
        null=True
    )

    image_url_6 = models.URLField(
        blank=True,
        null=True
    )

    image_url_7 = models.URLField(
        blank=True,
        null=True
    )

    image_url_8 = models.URLField(
        blank=True,
        null=True
    )

    image_url_9 = models.URLField(
        blank=True,
        null=True
    )

    image_url_10 = models.URLField(
        blank=True,
        null=True
    )

    # =========================
    # AVAILABILITY
    # =========================

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.brand} {self.model_name}"