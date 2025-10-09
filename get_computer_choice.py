import random
from game_logic import choices

def get_computer_choice():
      """Generate a random choice based on the choices in the Game"""
      return random.choice(choices)
      