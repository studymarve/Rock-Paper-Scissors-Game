scoreboard = {"win": 0, "lose": 0, "tie": 0}

def reset_scoreboard():
    # Your code here - 3 lines max!
    scoreboard["win"] = 0
    scoreboard["lose"] = 0
    scoreboard["tie"] = 0
    return scoreboard
  
  
def score_update(outcome):
    if outcome == "win":
        scoreboard["win"] += 1
    elif outcome == "lose":
        scoreboard["lose"] += 1
    else:  # tie
        scoreboard["tie"] += 1
    return scoreboard  # Always return the scoreboard
    
    
def game_status():
    """Return who is winning overall"""
    player_score = scoreboard["win"]
    computer_score = scoreboard["lose"]
    
    if player_score > computer_score:
        return "player_winning"
    elif player_score < computer_score:
        return "computer_winning"
    else:
        return "tied"