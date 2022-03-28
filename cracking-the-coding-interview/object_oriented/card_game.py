import random
from collections import deque

class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    def display_form(self):
        return f"{self.suit} {self.number}"

DEFAULT_SUIT_ORDER = ["♣", "♢", "♡", "♠"]
DEFAULT_NUMBER_ORDER = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Game:
    # TODO 順番はインデックスでやったほうが楽そう
    def __init__(self, initial_hand_number, suit_order = DEFAULT_SUIT_ORDER, number_order = DEFAULT_NUMBER_ORDER):
        # TODO validation
        self.initial_hand_number = initial_hand_number
        self.suit_order = {suit: i for i, suit in enumerate(suit_order)}
        self.s = len(suit_order)
        self.number_order = {number: i for i, number in enumerate(number_order)}
        self.n = len(number_order)
        self.cards = dict()
        for (i, suit) in enumerate(suit_order):
            for (j, number) in enumerate(number_order):
                self.cards[i*self.n + j] = Card(suit, number)
        self.total = self.n * self.s
        self.order = []
    
    def get_card(self, p):
        return self.cards[p]

    def start(self, player_number):
        # TODO validation
        if player_number == 0:
            raise ValueError("at least one person")
        if player_number*self.initial_hand_number > self.total:
            raise ValueError("not enough deck of cards on hand")
        self.order = deque(random.sample([i for i in range(player_number)], player_number))
        self.deck = deque(random.sample([i for i in range(self.total)], self.total))
        self.used = [ False for _ in range(self.total)]
        self.hands = []
        for _ in range(player_number):
            hand = []
            for _ in range(self.initial_hand_number):
                x = self.deck.popleft()
                hand.append(x)
                self.used[x] = True
            self.hands.append(hand)
        turn = self.order[0]
        print(f"this turn {turn}")
        self.display_hand()

    def display_turn_hand(self, turn_order):
        turn = self.order[turn_order]
        print(f"hand: {' '.join(map(lambda x: self.cards[x].display_form(), self.hands[turn]))}")

    def display_hand(self):
        self.display_turn_hand(0)

    def next_turn(self):
        x = self.order.popleft()
        self.order.append(x)
    
    def clean_deck(self):
        if not self.deck:
            raise Exception("deck runs out")
        while self.used[self.deck[0]]:
            self.deck.popleft()
            if not self.deck:
                break        
        if not self.deck:
            raise Exception("deck runs out")

    def draw_one(self, turn):
        self.clean_deck()
        x = self.deck.popleft()
        self.used[x] = True
        self.hands[turn].append(x)

    def turn_draw(self, number):
        turn = self.order[0]
        for _ in range(number):
            self.draw_one(turn)
    
    def turn_discard(self, index):
        turn = self.order[0]
        if index < 0 or len(self.hands[turn]) <= index:
            raise Exception("wrong index")
        del self.hands[turn][index]



class Blackjack(Game):
    def __init__(self):
        super().__init__(2)
        self.number_mapping = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10, "A": -1}

    def display_all_hands_calcuration(self):
        for turn_order in range(len(self.order)):
            self.display_turn_hand(turn_order)
            print(f"score: {self.calcurate(self.order[turn_order])}")

    def calcurate(self, turn):
        hand = [self.number_mapping[self.cards[x].number] for x in self.hands[turn]]
        dp = [[False for _ in range(22)] for _ in range(len(hand)+1)]
        dp[0][0] = True
        for i, x in enumerate(hand):
            candidates = [1, 11] if x == -1 else [x]
            for t in candidates:
                for j in range(22-t):
                    dp[i+1][j+t] |= dp[i][j]
        for i in reversed(range(22)):
            if dp[-1][i]:
                return i
        return -1
    
    def draw_around(self):
        for _ in range(len(self.order)):
            self.display_hand()
            while True:
                self.display_hand()
                x = input("1 => draw")
                if x == "1":
                    self.turn_draw(1)
                else:
                    break
            self.next_turn()
    
    def winner(self):
        winner = -1
        score = -1
        for turn_order in range(len(self.order)):
            turn_score =  self.calcurate(self.order[turn_order])
            if turn_score == -1:
                continue
            if score < turn_score:
                winner = self.order[turn_order]
                score = turn_score
        if winner == -1:
            print("no winner")
            return
        print("winner:", winner, ", score:", score)
        self.display_turn_hand(winner)

def test_blackjack():
    game = Blackjack()
    # for (x, card) in game.cards.items():
    #     print(x, card.display_form())
    game.start(4)
    game.draw_around()
    game.winner()
    game.display_all_hands_calcuration()

if __name__=="__main__":
    test_blackjack()



def test_game():
    game = Game(3)
    game.start(4)
    game.turn_draw(2)
    game.display_hand()
    game.turn_discard(1)
    game.display_hand()
    game.next_turn()
    game.display_hand()

