## Main entry point for Smart Public Transportation Calculator

# Console colours
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

from input import get_validated_input, get_trip_details
from calculation import calculate_all_options, find_best_option
from display import display_welcome_menu, display_comparison_table, display_recommendation, display_trip_summary
from info_views import view_transport_info, view_sustainability_guidelines

def main():
    print(BLUE + "\nStarting Smart Public Transportation Calculator" + RESET)

    while True:
        display_welcome_menu()
        choice = get_validated_input(
            GREEN + "  Enter your choice [1-4]: " + RESET, 
            str, 
            lambda x: x in ["1", "2", "3", "4"], "Please enter a number between 1 and 4.")

        if choice == "1":
            trip_details = get_trip_details()
            results = calculate_all_options(trip_details)
            best_option = find_best_option(results)
            display_comparison_table(results, trip_details)
            display_recommendation(best_option, trip_details, results)
            display_trip_summary(trip_details, results, best_option)
        elif choice == "2":
            view_transport_info()
        elif choice == "3":
            view_sustainability_guidelines()
        elif choice == "4":
            print(GREEN + "\nThank you for using Smart Public Transportation Calculator!" + RESET)
            print( GREEN + "Together we build sustainable cities!" + RESET)
            break

        if choice != "4":
            input("\n  Press Enter to return to menu...")


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    