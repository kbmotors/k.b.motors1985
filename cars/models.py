from django.db import models
import re


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

    brand = models.CharField(max_length=100)

    model_name = models.CharField(max_length=100)

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

    image_url = models.URLField(
        blank=True,
        null=True,
        help_text="Paste normal image URL or Google Drive sharing link"
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def get_image_url(self):

        if not self.image_url:
            return ""

        url = self.image_url.strip()

        # ---------------------------------
        # GOOGLE DRIVE LINK CONVERSION
        # ---------------------------------

        # Example:
        # https://drive.google.com/file/d/FILE_ID/view

        match = re.search(
            r"drive\.google\.com/file/d/([^/]+)",
            url
        )

        if match:
            file_id = match.group(1)

            return (
                f"https://drive.google.com/uc"
                f"?export=view&id={file_id}"
            )

        # ---------------------------------
        # Google Drive open?id=FILE_ID
        # ---------------------------------

        match = re.search(
            r"drive\.google\.com/open\?id=([^&]+)",
            url
        )

        if match:
            file_id = match.group(1)

            return (
                f"https://drive.google.com/uc"
                f"?export=view&id={file_id}"
            )

        # ---------------------------------
        # Already direct URL
        # ---------------------------------

        return url

    def __str__(self):
        return f"{self.brand} {self.model_name}"