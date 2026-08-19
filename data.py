## Data and Transport Class for Smart Public Transportation Calculator
class Transport:
    def __init__(self, name, base_fare_per_km, speed_kmh,
                 co2_per_km_per_passenger, sustainability_base):

        self.name = name
        self.base_fare_per_km = base_fare_per_km
        self.speed_kmh = speed_kmh
        self.co2_per_km_per_passenger = co2_per_km_per_passenger
        self.sustainability_base = sustainability_base

TRANSPORT_OPTIONS = {
    "1": Transport("Bus", 0.15, 30, 40, 3),
    "2": Transport("MRT", 0.20, 60, 70, 4),
    "3": Transport("LRT", 0.18, 45, 70, 4),
    "4": Transport("KTMB", 0.25, 80, 90, 3)
}
PASSENGER_TYPES = {
    "1": {"name": "Adult", "fare_multiplier": 1.0, "co2_multiplier": 1.0},
    "2": {"name": "Student", "fare_multiplier": 0.5, "co2_multiplier": 1.0},
    "3": {"name": "Senior", "fare_multiplier": 0.4, "co2_multiplier": 1.0},
    "4": {"name": "Child", "fare_multiplier": 0.3, "co2_multiplier": 1.0}
}

TRIP_TYPES = {
    "1": {"name": "One-way", "multiplier": 1},
    "2": {"name": "Return", "multiplier": 2}
}

SUSTAINABILITY_THRESHOLDS = {"Excellent": 30, "Good": 50, "Fair": 80, "Poor": float('inf')}







