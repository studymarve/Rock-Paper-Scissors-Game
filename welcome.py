def get_player_name():
  """Get player name with validation"""
  while True:
            name = input("What is your name: ").strip()
            if not name:
                print("🙏🙏 Please type a valid name!! 🖐️🖐️🖐️")
            else:
                return name.capitalize()

def welcome_message(player_name):
  """Get user name and print personalized welcome message"""
  return f"""🎮🎮 Welcome {player_name} to RPS Game! 🎮🎮
    The rules are simple:
      1. Paper 📜 beats Rock 🌋
      2. Rock 🌋 beats Scissors ✂️
      3. Scissors ✂️ beats Paper 📜
    
    
    Game Modes:
    1. Infinity ♾️ mode - Play as long as you want {player_name}
    2. Round 🏆 mode - Play a fixed number of rounds {player_name}
    
    Ready to challenge the computer? Let's see who wins! 🏆 """

# To import the functions in the main file
if __name__ == "__main__":
    pass
