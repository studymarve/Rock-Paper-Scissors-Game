# history.py (fixed)
import datetime
import os

def save_game_history(player_name, player_wins, computer_wins, ties, mode):
    """Save game results to history.txt"""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Determine game outcome
    if player_wins > computer_wins:
        result = f"{player_name} Won: Wins {player_wins}, Lost {computer_wins}, Ties {ties} | {mode} mode | {timestamp}"
    elif player_wins < computer_wins:
        result = f"Computer Won: Wins {computer_wins}, Lost {player_wins}, Ties {ties} | Against {player_name} | {mode} mode | {timestamp}"
    else:
        result = f"TIED: {player_name} {player_wins} - Computer {computer_wins} | Ties {ties} | {mode} mode | {timestamp}"
    
    # Use a single history file
    filename = "game_history.txt"
    
    # Create header if file doesn't exist
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write("=== ROCK-PAPER-SCISSORS GAME HISTORY ===\n\n")
    
    # Append the result
    with open(filename, "a", encoding="utf-8") as file:
        file.write(result + "\n")
        file.write("-" * 50 + "\n")
    
    print(f"📊 Game saved to {filename}")
    return result