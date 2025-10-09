def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("n", "no"):
            return False
        elif answer in ("y", "yes"):
            return True
        else:
             print("🏋️🏋️🙏🙏 Type yes or no")
             continue
           
def get_positive_integer(prompt):
    """Get a positive integer from user with validation"""
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive number (at least 1)")
        except ValueError:
            print("Please enter a valid number (like 3, 5, 10)")