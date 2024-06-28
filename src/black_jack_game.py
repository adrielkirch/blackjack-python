from dealer import Dealer
from deck import SingletonDeck

class BlackjackGame:
    def __init__(self, players):
        self.players = players
        self.dealer = Dealer()
        self.deck = SingletonDeck()

    def deal_initial_cards(self):
        for _ in range(2):
            for participant in self.players + [self.dealer]:
                participant.add_card_to_hand(self.deck.cards.pop())

    def play_round(self):
        # Reset player hands
        for player in self.players:
            player.hand = []
        self.dealer.hand = []

        # Place bets
        for player in self.players:
            while True:
                try:
                    bet_amount = int(input(f"{player.name}, place your bet (current chips: {player.chips}): "))
                    player.place_bet(bet_amount)
                    break
                except ValueError as e:
                    print(f"Invalid input: {e}")

        # Deal initial cards
        self.deal_initial_cards()

        # Show one of the dealer's cards
        print(f"\nDealer's visible card: {self.dealer.hand[0]}")

        # Players' turns
        for player in self.players:
            print(f"\n{player.name}'s turn:")
            while True:
                print(f"Current hand: {player.hand}. Total value: {player.calculate_hand_value()}")
                action = input("Do you want to (h)it or (s)tand? ").lower()
                if action == "h":
                    player.add_card_to_hand(self.deck.cards.pop())
                    new_value = player.calculate_hand_value()
                    print(f"New hand: {player.hand}. New total value: {new_value}")
                    if new_value > 21:
                        print(f"{player.name} busted! Total value: {new_value}")
                        break
                elif action == "s":
                    break
                else:
                    print("Invalid input. Please enter 'h' or 's'.")

        # Dealer's turn
        print(f"\nDealer's turn:")
        print(f"Dealer's full hand: {self.dealer.hand}. Total value: {self.dealer.calculate_hand_value()}")
        while self.dealer.calculate_hand_value() < 17:
            self.dealer.add_card_to_hand(self.deck.cards.pop())
            print(f"Current hand: {self.dealer.hand}. Total value: {self.dealer.calculate_hand_value()}")

        # Determine winner
        self.determine_winner()

        # Rotate players for the next round
        self.players.append(self.players.pop(0))

    def determine_winner(self):
        dealer_value = self.dealer.calculate_hand_value()
        print(f"\nDealer's final hand: {self.dealer.hand}. Total value: {dealer_value}\n")

        for player in self.players:
            player_value = player.calculate_hand_value()
            print(f"{player.name}'s final hand: {player.hand}. Total value: {player_value}")

            if player_value > 21:
                print(f"{player.name} busted and loses the bet of {player.bet} chips.")
                chips_change = -player.bet
            elif dealer_value > 21 or player_value > dealer_value:
                player.chips += player.bet * 2
                chips_change = player.bet
                print(f"{player.name} wins and now has {player.chips} chips.")
            elif player_value == dealer_value:
                player.chips += player.bet
                chips_change = 0
                print(f"{player.name} ties with the dealer and retains the bet. Total chips: {player.chips}")
            else:
                print(f"{player.name} loses to the dealer and loses the bet of {player.bet} chips.")
                chips_change = -player.bet

            # Display chips change
            print(f"{player.name} change in chips: {chips_change}\n")

            # Reset bet
            player.bet = 0
