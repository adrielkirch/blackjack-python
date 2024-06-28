class Player:
    def __init__(self, name, chips=1000):
        self.name = name
        self.chips = chips
        self.hand = []
        self.bet = 0

    def __str__(self):
        return f"{self.name} has {len(self.hand)} cards with total value: {self.calculate_hand_value()}"

    def add_card_to_hand(self, card):
        self.hand.append(card)

    def calculate_hand_value(self):
        value = 0
        num_aces = 0
        for card in self.hand:
            if card[0] in "JQK":
                value += 10
            elif card[0] == "A":
                num_aces += 1
                value += 11
            else:
                value += int(card[:-1])

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

    def place_bet(self, amount):
        if amount > self.chips:
            raise ValueError("Bet amount exceeds available chips.")
        self.bet = amount
        self.chips -= amount
