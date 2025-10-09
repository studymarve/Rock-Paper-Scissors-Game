# messages.py
import random
from result import game_status

# Create your own personality messages - make them unique!
winning_messages = [
    "I'm dominating this game! 😎",
    "The computer reigns supreme! 👑", 
    "Look at you 🔍🙄 {player_name}, You can't beat Marvellous Logic",
    "Haha 😅😅😅, Are you really bad at this game",
    "Looks like the legend 💪💪 of me is true don't you think"
]

losing_messages = [
    "You're getting really good at this! 🎯",
    "I have to say 🗣️ {player_name}, You are really good at this Game 🎮",
    "I heard a legend about a player who could defeat any player in The RPS Game, Looks like that You?",
    "Look at you taking the game like a Grandmaster",
    "Let's see {player_name} if you can win the next round",
    "Have mercy 🥺🥺 {player_name}"
    
]

tied_messages = [
    "We're evenly matched! ⚖️",
    "Looks like Luck did not want both of us to win 🏆",
    "Is our luck really bad",
    "For us to tie looks like you are not as they described"
]

def get_personality_message(player_name):
    """Get message based on current game state"""
    status = game_status()
    if status == "player_winning":
      message_template = random.choice(losing_messages)
    elif status == "computer_winning":
      message_template = random.choice(winning_messages)
    else:
      message_template = random.choice(tied_messages)
    return message_template.format(player_name=player_name)
    
def get_final_message(player_wins, computer_wins, ties, player_name):
    """Get final personality message"""
    if player_wins > computer_wins:
      return f"Wow {player_name}, you won fair and square {player_wins}-{computer_wins}"
    elif player_wins < computer_wins:
      return f"I have to say {player_name}, Looks like i won {computer_wins}-{player_wins}"
    else:
      return f"We are sure evenly tied {player_wins}-{computer_wins}-{ties}"
    # Your logic here - return message based on who won