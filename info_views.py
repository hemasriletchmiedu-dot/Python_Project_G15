## Info view functions for Smart Public Transportation Calculator

# Console colours
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

from data import TRANSPORT_OPTIONS, SUSTAINABILITY_THRESHOLDS
from calculation import get_sustainability_rating


def view_transport_info():
    print("\n" + "=" * 65)
    print(BLUE + "TRANSPORT OPTIONS INFORMATION" + RESET)
    print("=" * 65)
    print(f"{'Transport':<12} {'Fare/km (RM)':>14} {'Speed (km/h)':>14} {'CO2 g/km/pass':>18} {'Sustainability':<15}")
    print("-" * 65)
    for key, transport in TRANSPORT_OPTIONS.items():
        sustain = get_sustainability_rating(
            transport.co2_per_km_per_passenger
            )
        print(
            f"{transport.name:<12}"
            f"{transport.base_fare_per_km:>14.2f}"
            f"{transport.speed_kmh:>14}"
            f"{transport.co2_per_km_per_passenger:>15}"
            f" {sustain:<15}"
            )
    print("-" * 65)


def view_sustainability_guidelines():
    print("\n" + "=" * 65)
    print( BLUE + "SUSTAINABILITY RATING GUIDELINES" + RESET)
    print("=" * 65)
    print("  CO2 Emissions (g/km/passenger) -> Rating")
    print("-" * 65)
    print(f"  <= {SUSTAINABILITY_THRESHOLDS['Excellent']:<3} g/km      -> Excellent")
    print(f"  <= {SUSTAINABILITY_THRESHOLDS['Good']:<3} g/km           -> Good")
    print(f"  <= {SUSTAINABILITY_THRESHOLDS['Fair']:<3} g/km           -> Fair")
    print(f"  >  {SUSTAINABILITY_THRESHOLDS['Fair']:<3} g/km           -> Poor")
    print("-" * 65)
    print(GREEN + "\n  Tips for Sustainable Travel:" + RESET)
    print("  * Choose MRT/KTMB for longer distances")
    print("  * Use Bus/LRT for shorter trips")
    print("  * Travel off-peak to reduce congestion")
    print("  * Combine trips to reduce total journeys")
    print("  * Consider walking/cycling for very short distances")
    print("=" * 65)
    
    
    
    
    
    
    
    
    
    
    