import random

"""A simple Rock-Paper-Scissors game Phase 2."""

# Game data
choices = ("r", "p", "s")
emojis = {"r": "🌋", "p": "📜", "s": "✂️"}
aliases = {
    'r': 'r', 'rock': 'r',
    'p': 'p', 'paper': 'p',
    's': 's', 'scissors': 's'
}
winning_rules = {('r', 's'), ('s', 'p'), ('p', 'r')}



def get_user_choice():
    """Prompt for user's move until valid"""
    while True:
        user_input = input("Rock, Paper or Scissors (r/p/s): ").lower().strip()
        user_choice = aliases.get(user_input)
        if user_choice is None:
            print("Invalid choice! Please type r/p/s or rock/paper/scissors.")
            continue
        return user_choice
        
        
if __name__ == "__main__":
    get_user_choice()
        