# Class to handle the CheckWriter functionality
class CheckWriter:
    
    # Main function to convert the numeric amount into words
    def convert_amount_to_words(self, amount):
        # Step 1: Split the amount into dollars and cents
        dollars, cents = self.split_amount(amount)
        
        # Step 2: Convert dollars and cents to words
        dollar_words = self.convert_dollars_to_words(dollars)
        cent_words = self.convert_cents_to_words(cents)
        
        # Step 3: Combine results and return final string
        return self.combine_results(dollar_words, cent_words)

    # Function to split the amount into dollars and cents
    def split_amount(self, amount):
        dollars = int(amount)
        cents = round((amount - dollars) * 100)
        return dollars, cents

    # Function to convert the dollar part to words
    def convert_dollars_to_words(self, dollars):
        if dollars == 0:
            return "Zero dollars"
        elif dollars == 1:
            return "One dollar"
        else:
            return self.apply_pluralization(self.number_to_words(dollars), dollars, "dollar", "dollars")

    # Function to convert the cent part to words
    def convert_cents_to_words(self, cents):
        if cents == 0:
            return "Zero cents"
        elif cents == 1:
            return "One cent"
        else:
            return self.apply_pluralization(self.number_to_words(cents), cents, "cent", "cents")

    # Function to apply pluralization
    def apply_pluralization(self, word, value, singular, plural):
        return f"{word} {singular}" if value == 1 else f"{word} {plural}"

    # Function to convert numbers to words
    def number_to_words(self, number):
        units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

        if number == 0:
            return "Zero"
        elif 1 <= number <= 9:
            return units[number]
        elif 11 <= number <= 19:
            return teens[number - 11]
        elif 10 <= number <= 99:
            ten_part = tens[number // 10]
            unit_part = units[number % 10]
            return ten_part + (f"-{unit_part}" if unit_part else "")
        elif 100 <= number <= 999:
            hundred_part = units[number // 100] + " hundred"
            remainder = number % 100
            if remainder:
                return hundred_part + " " + self.number_to_words(remainder)
            else:
                return hundred_part
        else:
            return "Out of range"

    # Function to combine the dollar and cent words into the final string
    def combine_results(self, dollar_words, cent_words):
        return f"{dollar_words} and {cent_words}"

# Menu-based program for user input
def main_menu():
    writer = CheckWriter()  # Create an instance of CheckWriter class
    print("Check Writer Program")
    print("--------------------")
    
    while True:
        try:
            # User input for the amount
            user_input = input("Enter the amount (or 'q' to quit): ")
            if user_input.lower() == 'q':
                print("Exiting the program.")
                break
            else:
                # Convert input to float and use the CheckWriter class to convert to words
                amount = float(user_input)
                result = writer.convert_amount_to_words(amount)
                print(f"Final Output: {result}\n")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.\n")

# Run the menu
main_menu()
