## Display functions for Smart Public Transportation Calculator

# Console colours
BLUE = "\033[94m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def display_welcome_menu():
    print("\n" + "=" * 65)
    print(BLUE + "SMART PUBLIC TRANSPORTATION FARE AND SUSTAINABILITY CALCULATOR" + RESET)
    print("=" * 65)
    print("-" * 65)
    print("  [1] Calculate Trip AND Compare Options")
    print("  [2] View Transport Information")
    print("  [3] View Sustainability Guidelines")
    print("  [4] Exit")
    print("-" * 65)


def format_passenger_types(passenger_types):
    ## Format list of passenger types for display
    if not passenger_types:
        return "None"
    types = [pt['name'] for pt in passenger_types]
    if len(types) <= 3:
        return ", ".join(types)
    else:
        return f"{', '.join(types[:3])} +{len(types)-3} more"


def display_comparison_table(results, trip_details):
    passenger_str = format_passenger_types(trip_details['passenger_types'])
    print("\n" + "=" * 95)
    print(BLUE + f"TRANSPORT COMPARISON: {trip_details['start']} -> {trip_details['destination']}" + RESET)
    print(f"    Distance: {trip_details['distance']} km | Passengers: {trip_details['num_passengers']} ({passenger_str}) | Trip: {trip_details['trip_type']['name']}")
    print("=" * 95)
    print(f"{'Transport':<12} {'Fare (RM)':>12} {'Time':>12} {'CO2/Pass (g)':>15} {'Total CO2 (g)':>15} {'Sustainability':<18}")
    print("-" * 95)

    for result in results:
        time_str = f"{result['travel_time_minutes']:.0f} min"
        if result['travel_time_minutes'] >= 60:
            time_str = f"{result['travel_time_hours']:.1f} hr"
        print(f"{result['name']:<12} {result['total_fare']:>12.2f} {time_str:>12} {result['co2_per_passenger']:>15.1f} {result['total_co2']:>15.1f} {result['sustainability']:<18}")

    print("-" * 95)


def display_recommendation(best_option, trip_details, results):
    print("\n" + "=" * 65)
    print(GREEN + "RECOMMENDED OPTION" + RESET)
    print("=" * 65)
    print(GREEN + f"  Transport: {best_option['name']}" + RESET)
    print(f"  Total Fare: RM {best_option['total_fare']:.2f}")

    time_str = f"{best_option['travel_time_minutes']:.0f} minutes"
    if best_option['travel_time_minutes'] >= 60:
        time_str = f"{best_option['travel_time_hours']:.1f} hours"
    print(f"  Travel Time: {time_str}")
    print(f"  CO2 per Passenger: {best_option['co2_per_passenger']:.1f} g")
    print(f"  Total CO2 Emissions: {best_option['total_co2']:.1f} g")
    print(YELLOW + f"  Sustainability Rating: {best_option['sustainability']}" + RESET)
    print("=" * 65)

    print("\n  WHY THIS OPTION?")
    if best_option['sustainability_score'] == 5:
        print("  * Lowest carbon emissions per km - most environmentally friendly")
    elif best_option['sustainability_score'] == 4:
        print("  * Low carbon emissions - good for sustainability")

    if best_option['total_fare'] == min(r['total_fare'] for r in results):
        print("  * Most affordable option")
    elif best_option['total_fare'] < max(r['total_fare'] for r in results):
        print("  * Good balance of cost and sustainability")



def display_trip_summary(trip_details, results, best_option):
    passenger_str = format_passenger_types(trip_details['passenger_types'])
    print("\n" + "=" * 65)
    print(BLUE + "TRIP SUMMARY" + RESET)
    print("=" * 65)
    print(f"  Route: {trip_details['start']} -> {trip_details['destination']}")
    print(f"  Distance: {trip_details['distance']} km")
    print(f"  Passengers: {trip_details['num_passengers']} ({passenger_str})")
    print(f"  Trip Type: {trip_details['trip_type']['name']}")
    print("-" * 65)

    # Individual passenger breakdown
    print("\n  Passenger Breakdown:")
    for i, pt in enumerate(trip_details['passenger_types'], 1):
        print(f"    Passenger {i}: {pt['name']} (Fare: {int(pt['fare_multiplier']*100)}%)")

    print(GREEN + f"\n  BEST CHOICE: {best_option['name']}" + RESET)
    print(f"     Fare: RM {best_option['total_fare']:.2f}")
    print(f"     Time: {best_option['travel_time_minutes']:.0f} min")
    print(f"     CO2: {best_option['total_co2']:.1f} g total")
    print(YELLOW + f"     Rating: {best_option['sustainability']}" + RESET)

    co2_kg = best_option['total_co2'] / 1000
    tree_offset = co2_kg / 21
    print(f"\n  Environmental Context:")
    print(f"     This trip produces {co2_kg:.3f} kg CO2")
    print(f"     ~ {tree_offset:.2f} tree-years to offset")
    print(GREEN + "\n  Thank you for choosing sustainable transport!" + RESET)
    print("=" * 65)
    
    
    
    
    
    
    
    