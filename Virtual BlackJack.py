# Virtual BlackJack

import random

card_numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
card_values = {'2' :2, '3' :3, '4' :4, '5' :5, '6' :6, '7' :7, '8' :8, '9' :9, '10' :10, 'J' :10, 'Q' :10, 'K' :10, 'A' :11}
card_suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

playing = True

class bettingchips():
    def __init__ (self, total = 1000):
        self.total = total
        self.bet = 0

    def betwin(self):
        self.total += self.bet

    def betloss(self):
        self.total -= self.bet

def abet(chip):
    while True:
        try:
            chip.bet = int(input("How many chips do you want to bet out of 1000?: "))
        except ValueError:
            print("Invalid. A bet must be a number")
        else:
            if chip.bet > chip.total:
                print("Invalid. Your bet exceeds the amount you have")
            else:
                break

def revealcards(user, dealer):
    print("\nDealer turn: ")
    print(" **CARD HIDDEN** ")
    print(' ', dealer.cards[1])
    print("\nUser turn: ", *user.cards, sep = '\n ')

def results(user, dealer):
    print("\nDealer turn: ", *dealer.cards, sep = '\n ')
    print("Dealer turn = ", dealer.value)
    print("\nUser turn: ", *user.cards, sep = '\n ')
    print("User turn = ", user.value)

def userBust(user, dealer, bettingchips):
    print("\n>>User busts, Dealer wins<<")
    bettingchips.betloss()

def userWin(user, dealer, bettingchips):
    print("\n>>USER WINS<<")
    bettingchips.betwin()

def dealerBust(user, dealer, bettingchips):
    print("\n>>DEALER BUSTS, USER WINS<<")
    bettingchips.betwin()

def dealerWin(user, dealer, bettingchips):
    print("\n>>Dealer wins<<")
    bettingchips.betloss()

def Tie(user, dealer):
    print("\n>>It's a push(tie)<<")



class card():
    def __init__ (self, card_suit, card_number):
        self.card_number = card_number
        self.card_suit = card_suit

    def __str__ (self):
        return self.card_number + " of " + self.card_suit

class Deck():
    def __init__ (self):
        self.deck = []
        for card_suit in card_suits:
            for card_number in card_numbers:
                self.deck.append(card(card_suit,card_number))

    def __str__ (self):
        comp = ' '
        for card in self.deck:
            comp += '\n' + card.b()
        return "The deck has: " + comp

    def shuffle(self):
        random.shuffle(self.deck)

    def carddeal(self):
        acard = self.deck.pop()
        return acard

class playercards():
    def __init__ (self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def newcard(self, card):
        self.cards.append(card)
        self.value += card_values [card.card_number]
        if card.card_number == 'A':
            self.ace += 1
            
    def aces(self):
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1

def hit(deck, playercards):
    playercards.newcard(deck.carddeal())
    playercards.aces()

def decision(deck, playercards):
    global playing
    
    while True:
        z = input(" Hit or Stay. Enter h or s : ")

        if z[0].lower() == 'h':
            hit(deck, playercards)

        elif z[0].lower() == 's':
            print("Dealer is now drawing cards")
            playing = False

        else:
            print("Invalid")
            continue
        break


while True:
    print("Welcome to Virtual BlackJack")
    print("The goal is to get as close to 21 as possible without going over (Bust). \n")
    print("The dealer will show one of their cards dealt and won't start playing until the user stands or busts. \n")
    print("Cards 1 through 10 are worth their value, face cards are worth 10, and Aces can be worth 1 or 11. \n")

    deck = Deck()
    deck.shuffle()

    userhand = playercards()
    userhand.newcard(deck.carddeal())
    userhand.newcard(deck.carddeal())

    dealerhand = playercards()
    dealerhand.newcard(deck.carddeal())
    dealerhand.newcard(deck.carddeal())

    userchips = bettingchips()
    abet(userchips)

    revealcards(userhand, dealerhand)

    while playing:
        decision(deck, userhand)

        revealcards(userhand, dealerhand)

        if userhand.value > 21:
            userBust(userhand, dealerhand, userchips)

            break

    if userhand.value <= 21:
        while dealerhand.value < userhand.value:
            hit(deck, dealerhand)

        results(userhand, dealerhand)

        if dealerhand.value > 21:
            dealerBust(userhand, dealerhand, userchips)
            
        elif dealerhand.value > userhand.value:
            dealerWin(userhand, dealerhand, userchips)

        elif dealerhand.value < userhand.value:
            userWin(userhand, dealerhand, userchips)

        else:
            Tie(userhand, dealerhand)

    print("\n Player chips are at: {}" .format(userchips.total))

    newGame = input("Do you want to reset with 1000 chips? y/n: ")

    if newGame[0].lower() == 'y':
        playing = True
        continue

    else:
        print("Thanks for playing")
        break
                
    

            
                           
















        
    
        
    
