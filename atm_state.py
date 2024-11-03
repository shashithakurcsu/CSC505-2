class ATM:
    def __init__(self):
        self.current_state = "Idle"
        self.pin_attempts = 0
        self.max_attempts = 3
        self.account_balance = 1000  # Starting balance for demonstration
        self.correct_pin = "1234"    # Hardcoded PIN for demonstration
        self.transaction_history = []

    def log_transition(self, event, guard="", action=""):
        """Log state transitions for debugging and demonstration"""
        transition = f"State: {self.current_state}"
        if event:
            transition += f" | Event: {event}"
        if guard:
            transition += f" | Guard: {guard}"
        if action:
            transition += f" | Action: {action}"
        print(transition)
        print("-" * 50)

    def process_card(self):
        """Handle card insertion event"""
        if self.current_state == "Idle":
            self.current_state = "Authentication"
            self.log_transition("InsertCard", action="ReadCardData")
            print("Welcome! Please enter your PIN.")
            return True
        return False

    def validate_pin(self, entered_pin):
        """Handle PIN validation"""
        self.current_state = "ProcessingPIN"
        self.log_transition("EnterPIN", action="ValidateInput")
        
        if entered_pin == self.correct_pin:
            self.current_state = "AccountActive"
            self.pin_attempts = 0
            self.log_transition("CheckPIN", "correct", "ResetErrorCount")
            print(f"Authentication successful. Current balance: ${self.account_balance}")
            return True
        else:
            self.pin_attempts += 1
            self.log_transition("CheckPIN", "incorrect", "IncrementErrorCount")
            
            if self.pin_attempts >= self.max_attempts:
                self.current_state = "AccountLocked"
                self.log_transition("CheckErrorCount", "exceeds limit", "LockAccount")
                print("Account locked due to too many incorrect attempts.")
                return False
            
            print(f"Incorrect PIN. Attempts remaining: {self.max_attempts - self.pin_attempts}")
            self.current_state = "Authentication"
            return False

    def withdraw(self, amount):
        """Handle withdrawal transaction"""
        if self.current_state != "AccountActive":
            print("Error: Not in active state")
            return False
            
        self.current_state = "TransactionInProgress"
        self.log_transition("RequestWithdrawal", "balance > 0", "ProcessRequest")
        
        if amount <= 0:
            print("Invalid amount")
            self.current_state = "AccountActive"
            return False
            
        if amount > self.account_balance:
            print("Insufficient funds")
            self.current_state = "AccountActive"
            return False
            
        self.account_balance -= amount
        self.transaction_history.append(f"Withdrawal: ${amount}")
        print(f"Withdrawal successful. Remaining balance: ${self.account_balance}")
        
        if self.account_balance == 0:
            self.current_state = "AccountClosed"
            self.log_transition("CheckBalance", "balance = 0", "CloseAccount")
            print("Account closed due to zero balance.")
            return True
            
        self.current_state = "AccountActive"
        self.log_transition("CompleteTransaction", action="UpdateBalance")
        return True

    def exit_session(self):
        """Handle session termination"""
        if self.current_state == "AccountActive":
            self.current_state = "Idle"
            self.log_transition("ExitRequest", action="EjectCard")
            print("Thank you for using our ATM. Card ejected.")
            return True
        return False

def main():
    """Main function to demonstrate ATM functionality"""
    atm = ATM()
    print("ATM State Machine Demonstration")
    print("=" * 50)
    
    # Simulate card insertion
    atm.process_card()
    
    # Simulate PIN entry (successful case)
    atm.validate_pin("1234")
    
    # Simulate withdrawal
    atm.withdraw(500)
    
    # Show another withdrawal
    atm.withdraw(300)
    
    # End session
    atm.exit_session()
    
    print("\nDemonstrating incorrect PIN scenario:")
    print("=" * 50)
    
    # Start new session
    atm.process_card()
    
    # Simulate multiple incorrect PIN attempts
    for _ in range(3):
        atm.validate_pin("0000")

if __name__ == "__main__":
    main()
