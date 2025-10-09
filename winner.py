# winner.py (fixed)
from game_logic import winning_rules

def determine_the_winner(user_choice, computer_choice):
    """Determine the winner based on rules of rock paper scissors(RPS)"""
    if user_choice == computer_choice:
        return "tie"  # Changed from "It's a tie!" for consistency
    if (user_choice, computer_choice) in winning_rules:
        return "win"
    return "lose"