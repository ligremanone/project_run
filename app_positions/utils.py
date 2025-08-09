from django.db.models import QuerySet
from geopy import distance

from app_positions.models import Position


def calculate_distance_to_item(
    position_latitude: float,
    position_longitude: float,
    item_latitude: float,
    item_longitude: float,
) -> float:
    return distance.distance(
        (position_latitude, position_longitude),
        (item_latitude, item_longitude),
    ).km


def is_distance_to_item_less_than(
    position_latitude: float,
    position_longitude: float,
    item_latitude: float,
    item_longitude: float,
    distance_to_item: float,
) -> bool:
    return (
        calculate_distance_to_item(
            position_latitude,
            position_longitude,
            item_latitude,
            item_longitude,
        )
        < distance_to_item
    )


def speed_calculation(prev_position: Position, current_position: Position) -> float:
    distance_between_positions = distance.distance(
        (prev_position.latitude, prev_position.longitude),
        (current_position.latitude, current_position.longitude),
    ).m
    time = (current_position.date_time - prev_position.date_time).seconds
    return round(distance_between_positions / time, 2)


def calculate_all_distance(positions: QuerySet) -> float:
    result = 0
    for i in range(len(positions) - 1):
        result += distance.distance(
            (positions[i].latitude, positions[i].longitude),
            (positions[i + 1].latitude, positions[i + 1].longitude),
        ).km
    return round(result, 2)
