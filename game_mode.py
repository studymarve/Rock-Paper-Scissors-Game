# game_mode.py (enhanced)
from game_logic import get_user_choice
from get_computer_choice import get_computer_choice
from utils import get_yes_or_no
from display import display_choices
from winner import determine_the_winner
from result import scoreboard, score_update, reset_scoreboard
from messages import get_personality_message, get_final_message
from history import save_game_history

def play_single_round(player_name):
    """Play one round of the game with personality messages"""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    display_choices(user_choice, computer_choice)
    
    outcome = determine_the_winner(user_choice, computer_choice)
    
    # Display round result
    if outcome == "win":
        print("🎉 You win this round!")
    elif outcome == "lose":
        print("💻 Computer wins this round!")
    else:
        print("🤝 It's a tie!")
    
    # Update score and display
    score_update(outcome)
    
    # Show personality message based on current game state
    personality_msg = get_personality_message(player_name)
    print(f"💬 {personality_msg}")
    
    print(f"📊 Current Score: You {scoreboard['win']} - Computer {scoreboard['lose']} - Ties {scoreboard['tie']}\n")

def play_game(rounds=None, player_name="Player"):
    """Main game function with history saving"""
    reset_scoreboard()
    mode_name = "Infinity ♾️" if rounds is None else f"Rounds 🏆 ({rounds} rounds)"
    
    print(f"\n🎮 Starting {mode_name} for {player_name}!")
    
    if rounds is None:  # Infinity mode
        round_count = 0
        while True:
            round_count += 1
            print(f"🔁 Round {round_count}")
            play_single_round(player_name)
            
            if not get_yes_or_no("Do you want to play another round? (y/n): "):
                break
    else:  # Fixed rounds mode
        for i in range(rounds):
            print(f"🔁 Round {i+1} of {rounds}")
            play_single_round(player_name)
    
    # Display final results and save history
    final_score = get_final_message(
        scoreboard['win'], 
        scoreboard['lose'], 
        scoreboard['tie'], 
        player_name
    )
    print(f"\n🏁 {final_score}")
    
    # Save game history
    save_game_history(
        player_name,
        scoreboard['win'],
        scoreboard['lose'], 
        scoreboard['tie'],
        mode_name
    )