from player import Player
from black_jack_game import BlackjackGame

# Example usage:
if __name__ == "__main__":
    players = [Player("Player 1"), Player("Player 2")]
    game = BlackjackGame(players)

    while True:
        game.play_round()
        another_round = input("\nDo you want to play another round? (y/n):\n").lower()
        if another_round != "y":
            break
