## Input handling functions for Smart Public Transportation Calculator
# Console colours
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

from data import PASSENGER_TYPES, TRIP_TYPES

def get_validated_input(prompt, input_type, validator=None, error_msg="Invalid input. Please try again."):
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print(RED + " Input cannot be empty. Please try again." + RESET)
                continue
            value = input_type(user_input)
            if validator and not validator(value):
                print(RED + "  " + error_msg + RESET)
                continue
            return value
        except ValueError:
            print(RED + f"  Please enter a valid {input_type.__name__}." + RESET)
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            exit()


def get_trip_details():
    print("\n" + "-" * 65)
    print("ENTER TRIP DETAILS")
    print("-" * 65)

    start = get_validated_input(GREEN + "  Starting Point: " + RESET, str, lambda x: len(x) >= 2, "Starting point must be at least 2 characters." )
    destination = get_validated_input(GREEN + "  Destination: " + RESET, str, lambda x: len(x) >= 2, "Destination must be at least 2 characters.")
    distance = get_validated_input(GREEN + "  Distance (km): " + RESET, float, lambda x: x > 0, "Distance must be greater than 0.")
    num_passengers = get_validated_input(GREEN +"  Number of Passengers: " + RESET, int, lambda x: x > 0, "Number of passengers must be at least 1.")

    print("\n  Passenger Types:")
    for key, val in PASSENGER_TYPES.items():
        print(f"    [{key}] {val['name']} (Fare: {int(val['fare_multiplier']*100)}%)")

    passenger_types = []
    for i in range(num_passengers):
        print(f"\n  Passenger {i+1}:")
        passenger_key = get_validated_input(GREEN + f"    Select type [1-4]: " + RESET, str, lambda x: x in PASSENGER_TYPES, "Please select a valid option (1-4).")
        passenger_types.append(PASSENGER_TYPES[passenger_key])

    print("\n  Trip Type:")
    for key, val in TRIP_TYPES.items():
        print(f"    [{key}] {val['name']}")

    trip_key = get_validated_input(GREEN + "  Select trip type [1-2]: " + RESET, str, lambda x: x in TRIP_TYPES, "Please select a valid option (1-2).")
    trip_type = TRIP_TYPES[trip_key]

    return {
        "start": start,
        "destination": destination,
        "distance": distance,
        "num_passengers": num_passengers,
        "passenger_types": passenger_types,
        "trip_type": trip_type
    }
    
    
    
    