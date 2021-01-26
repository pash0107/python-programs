import random

#Tuples variable
suits = (
    'Hearts', 
    'Diamonds', 
    'Spades', 
    'Clubs'
)

ranks = (
    'Two', 
    'Three', 
    'Four', 
    'Five', 
    'Six', 
    'Seven', 
    'Eight', 
    'Nine', 
    'Ten', 
    'Jack', 
    'Queen', 
    'King', 
    'Ace'
)

#Dictionary variable
values = {
    'Two'  : 2,
    'Three': 3,
    'Four' : 4,
    'Five' : 5,
    'Six'  : 6,
    'Seven': 7,
    'Eight': 8,
    'Nine' : 9,
    'Ten'  : 10,
    'Jack' : 10,
    'Queen': 10,
    'King' : 10,
    'Ace'  : 11
}

playing = True

class Card:

    def __init__(self, suits, ranks):
        #can be use the following attributes
        self.suit = suits
        self.rank = ranks

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = [] #empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    
    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The Deck has: "+ deck_composition
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def show_all(player, dealer):
    print("Dealers HAND: ")
    print("AI: One card is HIDDEN")
    print(dealer.cards[1])
    print('\n')
    print('Player HAND: ')
    for card in player.cards:
        print(card)

def show_some(player, dealer):
    print('Dealer HAND: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Player HAND: ')
    for card in player.cards:
        print(card)

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet? "))

        except:
            print("Provide an integer")
            
        else:
            if chips.bet > chips.total:
                print('Not enough chips. You have: {}'.format(chips.total))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing

    while True:
        inputTry = input('Hit or Stand? Enter H or S: ')

        if inputTry[0].lower() == 'h':
            hit(deck, hand)
        
        elif inputTry[0].lower() == 's':
            print("Player stands Dealer's Turn")
            playing = False
        
        else:
            print('User Error.. Please enter H or S: ')
            continue
        
        break

def player_fail(player, dealer, chips):
    print('Bust Player!')
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player Win!')
    chips.win_bet()

def dealer_fail(player, dealer, chips):
    print('Dealer Bust!')
    chips.lose_bet()

def dealer_wins(player, dealer, chips):
    print('Dealer Win!')
    chips.win_bet()

def push(player, dealer):
    print('Tie GAME! PUSH')


#Game Phase
while True:

    print("BLACKJACK!")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:

        hit_or_stand(deck, dealer_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_fail(player_hand, dealer_hand, player_chips)
        break
    
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)
        
        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_fail(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        
        else:
            push(player_hand, dealer_hand)

    print("\n Player Total chips are at: {}".format(player_chips.total))
    new_game = input('Play again? y/n: ')

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing!')
        print('Your Chips: {}'.format(player_chips.total))
        break
        