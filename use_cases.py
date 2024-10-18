# Define the actors and use cases   
actors = {
    "Citizen": "Reports potholes through the web interface.",
    "Public Works Department Staff": "Assigns and manages work orders based on potholes reported.",
    "Repair Crew": "Conducts repair tasks and updates repair status in the system.",
    "System Administrator": "Manages the system’s operation, user access, and maintenance."
}

use_cases = {
    "Report Pothole": "Citizens log in to report the location and size of potholes.",
    "Assign Work Order": "Public works staff assign work orders to repair crews.",
    "Track Pothole Repairs": "Citizen tracks the status of ongoing repairs..",
    "Update Pothole Repairs" : "Repair crews update the status of ongoing repairs.",
    "Generate Damage Report File": "The system logs and stores damage information provided by citizens.",
    "Monitor System Performance": "The system administrator ensures the system is functional and up-to-date.",
    "Login": "Login to the system"
}

# Define a function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Display number of actors")
    print("2. Display number of use cases")
    print("3. List all actors")
    print("4. List all use cases")
    print("5. Exit")

# Define a function to handle user input
def handle_user_choice(choice):
    if choice == "1":
        print(f"\nNumber of Actors: {len(actors)}")
    elif choice == "2":
        print(f"\nNumber of Use Cases: {len(use_cases)}")
    elif choice == "3":
        print("\nList of Actors:")
        for actor in actors:
            print(f"- {actor}: {actors[actor]}")
    elif choice == "4":
        print("\nList of Use Cases:")
        for use_case in use_cases:
            print(f"- {use_case}: {use_cases[use_case]}")
    elif choice == "5":
        print("Exiting the program.")
        return False
    else:
        print("Invalid choice. Please enter a valid option.")
    return True

# Main loop to interact with the user
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if not handle_user_choice(choice):
            break

# Run the main loop
main()
