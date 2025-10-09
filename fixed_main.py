# fixed_main.py (updated)
from welcome import welcome_message, get_player_name
from game_mode import play_game
from utils import get_yes_or_no, get_positive_integer
from method import get_method

# Get player name and welcome (once at start)
player_name = get_player_name()
wel_mgs = welcome_message(player_name)
print(wel_mgs)

# Main game loop
while True:
    # Get mode choice
    mode = get_method()
    
    # Play game with player name
    if mode == 1:
        play_game(player_name=player_name)  # Infinity mode
    elif mode == 2:
        rounds = get_positive_integer("How many rounds do you want to play? ")
        play_game(rounds=rounds, player_name=player_name)  # Rounds mode
    
    if not get_yes_or_no("Do you want to return to the main menu? (y/n): "):
        break

# Final goodbye message
print(f"\nThanks for playing, {player_name}! Goodbye! 👋")