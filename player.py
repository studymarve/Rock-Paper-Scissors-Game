# player.py - OOP Implementation
"""Player class to encapsulate player properties and behaviors"""

class Player:
    """Represents a player in the Rock Paper Scissors game"""
    
    def __init__(self, name, is_computer=False):
        """Initialize player with name and score tracking"""
        self.name = name
        self.is_computer = is_computer
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_rounds = 0
        self.win_rate = 0.0
    
    def record_win(self):
        """Record a win for this player"""
        self.wins += 1
        self.total_rounds += 1
        self._update_win_rate()
    
    def record_loss(self):
        """Record a loss for this player"""
        self.losses += 1
        self.total_rounds += 1
        self._update_win_rate()
    
    def record_tie(self):
        """Record a tie for this player"""
        self.ties += 1
        self.total_rounds += 1
        self._update_win_rate()
    
    def _update_win_rate(self):
        """Calculate win rate (wins / total rounds)"""
        if self.total_rounds > 0:
            self.win_rate = (self.wins / self.total_rounds) * 100
        else:
            self.win_rate = 0.0
    
    def reset_game_stats(self):
        """Reset stats for a new game session"""
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.total_rounds = 0
        self.win_rate = 0.0
    
    def get_stats(self):
        """Return player statistics as a dictionary"""
        return {
            'name': self.name,
            'wins': self.wins,
            'losses': self.losses,
            'ties': self.ties,
            'total_rounds': self.total_rounds,
            'win_rate': round(self.win_rate, 2)
        }
    
    def display_stats(self):
        """Display player statistics in a formatted way"""
        stats = self.get_stats()
        return (f"\n📊 {stats['name']}'s Stats:\n"
                f"   Wins: {stats['wins']}\n"
                f"   Losses: {stats['losses']}\n"
                f"   Ties: {stats['ties']}\n"
                f"   Total Rounds: {stats['total_rounds']}\n"
                f"   Win Rate: {stats['win_rate']}%")
    
    def __str__(self):
        """String representation of player"""
        return f"Player({self.name}, W: {self.wins}, L: {self.losses}, T: {self.ties})"