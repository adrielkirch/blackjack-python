import random

class SingletonDeck:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.cards = [
                "A\u2660", "2\u2660", "3\u2660", "4\u2660", "5\u2660", "6\u2660", "7\u2660", "8\u2660", "9\u2660", "10\u2660", "J\u2660", "Q\u2660", "K\u2660",
                "A\u2661", "2\u2661", "3\u2661", "4\u2661", "5\u2661", "6\u2661", "7\u2661", "8\u2661", "9\u2661", "10\u2661", "J\u2661", "Q\u2661", "K\u2661",
                "A\u2662", "2\u2662", "3\u2662", "4\u2662", "5\u2662", "6\u2662", "7\u2662", "8\u2662", "9\u2662", "10\u2662", "J\u2662", "Q\u2662", "K\u2662",
                "A\u2663", "2\u2663", "3\u2663", "4\u2663", "5\u2663", "6\u2663", "7\u2663", "8\u2663", "9\u2663", "10\u2663", "J\u2663", "Q\u2663", "K\u2663"
            ]
            random.shuffle(cls._instance.cards)
        return cls._instance