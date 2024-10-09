class SoftwareEngineerTraits:
    def __init__(self):
        self.steps = []

    def add_step(self, step_name, description):
        self.steps.append({"Step Name": step_name, "Description": description})

    def display_steps(self):
        print(f"Number of Important Steps: {len(self.steps)}")
        print("Brief Description: This program outlines the key steps required to build an excellent software engineer with specific personality traits.")
        print("\nSteps Overview:")
        for index, step in enumerate(self.steps, 1):
            print(f"Step {index}: {step['Step Name']} - {step['Description']}")

# Create an instance of the traits class
traits_program = SoftwareEngineerTraits()

# Add steps with their names and descriptions
traits_program.add_step("Initialize Program", "Set up the builder and create an instance of the engineer.")
traits_program.add_step("Add Attention to Details", "Include the trait that ensures high-quality, accurate work.")
traits_program.add_step("Add Collaboration", "Incorporate teamwork and effective communication skills.")
traits_program.add_step("Add Resilience Under Pressure", "Ensure the ability to maintain performance under stress.")
traits_program.add_step("Finalize Engineer", "Complete the build and display the final engineer traits.")

# Display the steps
traits_program.display_steps()
