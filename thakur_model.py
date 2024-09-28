# Define a dictionary to store the phases and their corresponding steps
thakur_model_phases = {
    "Communication": [
        "Project Initiation",
        "Requirements Gathering"
    ],
    "Planning": [
        "Estimating",
        "Scheduling",
        "Tracking",
        "Customer Review"
    ],
    "Modeling": [
        "Analysis",
        "Design",
        "Early Testing",
        "Customer Review"
    ],
    "Construction": [
        "Analysis",
        "Design",
        "Early Testing",
        "Customer Review",
        "User Testing Feedback"
    ],
    "Deployment": [
        "Delivery",
        "Design",
        "Feedback",
        "Create Backlog for Issues in Production"
    ]
}

def display_phase_steps(phase):
    # Check if the phase is in the dictionary
    if phase in thakur_model_phases:
        print(f"\nSteps in the {phase} Phase:")
        for step in thakur_model_phases[phase]:
            print(f"- {step}")
    else:
        print(f"\n'{phase}' is not a valid phase in the Thakur Model. Please try again.")

def main():
    print("Welcome to the Thakur Model!")
    print("Available phases: Communication, Planning, Modeling, Construction, Deployment")
    
    while True:
        # Ask user to input a phase
        phase = input("\nEnter the name of the phase you want to learn about (or type 'exit' to quit): ").capitalize()

        # Exit condition
        if phase.lower() == 'exit':
            print("Exiting the Thakur Model program. Goodbye!")
            break

        # Display the steps of the chosen phase
        display_phase_steps(phase)

if __name__ == "__main__":
    main()
