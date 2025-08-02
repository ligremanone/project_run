from geopy import distance


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
