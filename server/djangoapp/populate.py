import json
from pathlib import Path

from django.db import transaction

from .models import CarMake, CarModel


CAR_RECORDS_FILE = (
    Path(__file__).resolve().parents[1] / "database" / "data" / "car_records.json"
)


@transaction.atomic
def initiate():
    """Idempotently import the IBM starter's car inventory as demo make/model data."""
    with CAR_RECORDS_FILE.open(encoding="utf-8") as data_file:
        records = json.load(data_file).get("cars", [])

    for record in records:
        make_name = (record.get("make") or "").strip()
        model_name = (record.get("model") or "").strip()
        if not make_name or not model_name:
            continue

        make, _ = CarMake.objects.get_or_create(
            name=make_name,
            defaults={"description": f"Demo catalog entries for {make_name} vehicles."},
        )
        raw_type = (record.get("bodyType") or "Other").strip()
        valid_types = {choice for choice, _label in CarModel.BodyType.choices}
        body_type = raw_type if raw_type in valid_types else CarModel.BodyType.OTHER
        year = int(record.get("year") or 2020)
        if not 2015 <= year <= 2023:
            continue
        CarModel.objects.get_or_create(
            car_make=make,
            name=model_name,
            year=year,
            defaults={"type": body_type},
        )

    return {"makes": CarMake.objects.count(), "models": CarModel.objects.count()}
