## Calculation functions for Smart Public Transportation Calculator

from data import TRANSPORT_OPTIONS, SUSTAINABILITY_THRESHOLDS


def get_sustainability_rating(co2_per_km):
    ## Return a sustainability rating based on CO2 per km per passenger.
    if co2_per_km <= SUSTAINABILITY_THRESHOLDS["Excellent"]:
        return "Excellent"
    elif co2_per_km <= SUSTAINABILITY_THRESHOLDS["Good"]:
        return "Good"
    elif co2_per_km <= SUSTAINABILITY_THRESHOLDS["Fair"]:
        return "Fair"
    else:
        return "Poor"


def calculate_transport_option(transport, trip_details):
    ## Calculate fare, travel time, and CO2 for one transport option.
    distance = trip_details["distance"]
    passenger_types = trip_details["passenger_types"]
    trip_multiplier = trip_details["trip_type"]["multiplier"]

    # Fare: base rate per km x distance, repeated for each passenger
    base_fare = transport.base_fare_per_km * distance
    total_fare = 0
    for passenger in passenger_types:
        total_fare += base_fare * passenger["fare_multiplier"] * trip_multiplier

    # Travel time in minutes
    travel_time_hours = distance / transport.speed_kmh
    travel_time_minutes = travel_time_hours * 60 * trip_multiplier

    # CO2: grams per km per passenger, for the whole trip
    co2_per_passenger = transport.co2_per_km_per_passenger * distance * trip_multiplier
    total_co2 = co2_per_passenger * len(passenger_types)

    return {
        "name":transport. name,
        "total_fare": round(total_fare, 2),
        "travel_time_minutes": round(travel_time_minutes, 1),
        "travel_time_hours": round(travel_time_minutes / 60, 2),
        "co2_per_passenger": round(co2_per_passenger, 1),
        "total_co2": round(total_co2, 1),
        "sustainability": get_sustainability_rating(transport.co2_per_km_per_passenger),
        "sustainability_score": transport.sustainability_base
    }


def calculate_all_options(trip_details):
    ## Calculate results for every transport option.
    results = []
    for transport in TRANSPORT_OPTIONS.values():
        results.append(calculate_transport_option(transport, trip_details))
    return results


def find_best_option(results):
    ## Return the best option: most sustainable first, cheapest to break ties.
    best_option = results[0]

    for option in results[1:]:
        # Prefer a higher sustainability score
        if option["sustainability_score"] > best_option["sustainability_score"]:
            best_option = option
        # If scores are equal, prefer the lower fare
        elif (option["sustainability_score"] == best_option["sustainability_score"]
              and option["total_fare"] < best_option["total_fare"]):
            best_option = option

    return best_option









