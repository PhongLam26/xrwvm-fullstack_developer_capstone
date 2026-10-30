from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    class BodyType(models.TextChoices):
        SEDAN = "Sedan", "Sedan"
        SUV = "SUV", "SUV"
        HATCHBACK = "Hatchback", "Hatchback"
        COUPE = "Coupe", "Coupe"
        CONVERTIBLE = "Convertible", "Convertible"
        PICKUP = "Pickup", "Pickup"
        MINIVAN = "Minivan", "Minivan"
        WAGON = "Wagon", "Wagon"
        OTHER = "Other", "Other"

    car_make = models.ForeignKey(
        CarMake, on_delete=models.CASCADE, related_name="models"
    )
    name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=24, choices=BodyType.choices, default=BodyType.OTHER
    )
    year = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2015), MaxValueValidator(2023)]
    )

    class Meta:
        ordering = ("car_make__name", "name", "year")
        constraints = [
            models.UniqueConstraint(
                fields=("car_make", "name", "year"), name="unique_make_model_year"
            )
        ]

    def __str__(self):
        return f"{self.year} {self.car_make.name} {self.name}"
