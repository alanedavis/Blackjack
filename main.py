import random
import time

class Card:
    def __init__(self, val, suit):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value,self.suit))

class Deck:
    def __init__(self):
        self.discards = []
        self.cards = []
        self.build()
    def build(self):
        suitArr = ["Hearts","Spades","Clubs","Diamonds"]
        valueArr = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
        for i in suitArr:
            for j in valueArr:
                self.cards.append(Card(j,i))
    def show(self):
        for i in self.cards:
            i.show()
    def shuffleCards(self):
        random.shuffle(self.cards)
    def drawCard(self):
        poppedCard = self.cards.pop()
        self.discards.append(poppedCard)
        return poppedCard

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.money = 100; self.totalBet = 0; self.totalHand = 0
    def hitPlayer(self, deck):
        self.hand.append(deck.drawCard())
    def handTotal(self):
        global vict, bust

        faceCards = ["Jack","Queen","King"]
        self.totalHand = total = ace1 = ace2 = 0

        for i in self.hand:
            if i.value in faceCards:
                total += 10
            elif i.value == "Ace":
                if ace1 == 0:
                    ace1 = 11
                elif ace1 > 0:
                    ace2 = 1
                elif ace2 > 0:
                    total += 1
            else:
                total += int(i.value)

        self.totalHand = ace1+ace2+total
        
        if ace1 > 0:
            if self.totalHand > 21:
                ace1 = 1
                self.totalHand = ace1+ace2+total
                print("{}'s current hand is worth {}.".format(self.name, self.totalHand))
            else:
                print("{}'s current hand is worth {} or {}.".format(self.name, self.totalHand-11,self.totalHand))
        else:
            print("{}'s current hand is worth {}.".format(self.name, self.totalHand))

    def show(self):
        print("\n------------------\n{}'s Hand:\n------------------".format(self.name))
        for i in self.hand:
            i.show()
    def showName(self):
        print(self.name)
    def showMoney(self):
        print("You have ${} left.".format(self.money))
    def betMoney(self,bet):
        while True:
            if bet == "" or str(bet).isalpha():
                print("Please enter a numeric value.\n")
                bet = input("How much would you like to bet: ")
            elif int(bet) <= 0:
                print("You need to bet more than 0 dollars\n")
                bet = input("How much would you like to bet: ")
            elif self.money < int(bet):
                print("You have less than ${} left.\n".format(bet))
                bet = input("How much would you like to bet: ")
            else:
                self.totalBet += int(bet)
                self.money -= int(bet)
                print("\n${} were added to the pot. The total bet is ${}.".format(bet,self.totalBet))
                print("You now have ${} left.".format(self.money))
                break

class Computer:
    def __init__(self):
        self.compHand = []
        self.totalHand = 0
    def hitComp(self, deck):
        self.compHand.append(deck.drawCard())
    def showStart(self):
        print("\n------------------\nComputers' Hand:\n------------------")
        count = 0
        for i in self.compHand:
            if count > 0:
                break
            else:
                i.show()
                count += 1
    def showInitial(self):
        print("\n------------------\nComputers' Hand:\n------------------")
        count = 0
        for i in self.compHand:
            if count > 0:
                break
            else:
                i.show()
                count += 1
        print("*Face Down Card*")
    def showAll(self):
        print("\n------------------\nComputers' Hand:\n------------------")
        for i in self.compHand:
            i.show()
    def compHandTotal(self):
        faceCards = ["Jack","Queen","King"]
        total = ace1 = ace2 = 0

        for i in self.compHand:
            if i.value in faceCards:
                total += 10
            elif i.value == "Ace":
                if ace1 == 0:
                    ace1 = 11
                elif ace1 > 0:
                    ace2 = 1
                elif ace2 > 0:
                    total += 1
            else:
                total += int(i.value)
        
        self.totalHand = ace1+ace2+total
        
        if ace1 > 0:
            if self.totalHand > 21:
                ace1 = 1
                self.totalHand = ace1+ace2+total
                print("The House hand is worth {}.".format(self.totalHand))
            else:
                print("The house hand is worth {} or {}.".format(self.totalHand-11,self.totalHand))
        else:
            print("The House hand is worth {}.".format(self.totalHand))
 
def welcomeMesg():
    global player
    print('''Welcome to Blackjack!!!\n\nThe object of the blackjack game is to accumulate cards with point totals as close to 21 without going over 21.\nFace cards (Jacks, Queens and Kings) are worth 10 points.\nAces are worth 1 or 11, whichever is preferable. Other cards are represented by their number.\nIf player and the House tie, it is a push and no one wins.\nAce and 10 (Blackjack) on the first two cards dealt is an automatic player win at 1.5 to 1, unless the house ties. A player may stand at any time.\n''')
    player = Player(setName().title())
    return player

def setName():
    playerName = ""
    while playerName == "":
        playerName = input("Type Player Name: ")
        if playerName == "":
            print("Please Enter Something.\n")
    return playerName

def shuffle(deck):
    deck.build()
    deck.shuffleCards()
    return deck

def dealCards(player, comp, deck):
    player.hand = []
    comp.compHand = []
    player.hitPlayer(deck); time.sleep(1); player.show()
    comp.hitComp(deck); time.sleep(1); comp.showStart()
    player.hitPlayer(deck); time.sleep(1); player.show()
    comp.hitComp(deck); time.sleep(1)
    comp.showInitial(); time.sleep(1); print("\n"); player.handTotal()

def minBet():
    global player
    player.totalBet = 0; time.sleep(1)
    print("\n*Automatic Transaction*")
    player.betMoney(15); time.sleep(1)
    return player

def initialBet():
    global player
    while True:
        initialDecision = input("\n1. Bet\n2. Pass\nInput: ")
        if initialDecision == "1" or initialDecision.lower() == "Bet":
            amount = input("How much would you like to bet: ")
            player.betMoney(amount)
            break
        elif initialDecision == "2" or initialDecision.lower() == "Pass":
            break
        else:
            print("\nPlease pick 1 of the 2 options.")
    return player

def showStatus():
    global player, comp, deck, bust, vict, compBust, compVict

    playing = True
    compTurn = True
    count = 0

    while playing == True:
        if count == 0 and player.totalHand != 21:
            initialBet()
            dealCards(player, comp, deck)
        if count == 1:
            comp.showInitial(); time.sleep(1)
            player.show(); time.sleep(1)
            player.handTotal(); time.sleep(1)

        if player.totalHand < 21:
            count = 1
            decision = input("\n1. Stay\n2. Hit\nInput: ")
            if decision == "1" or decision.lower() == "stay":
                while compTurn == True:
                    comp.showAll(); time.sleep(1)
                    comp.compHandTotal(); time.sleep(1)
                    if comp.totalHand > 21:
                        finalMessage()
                        playing = compTurn = False
                    elif comp.totalHand == 21:
                        victMessage()
                        playing = compTurn = False
                    elif comp.totalHand < player.totalHand:
                        comp.hitComp(deck)
                        time.sleep(1)
                    elif comp.totalHand > player.totalHand:
                        finalMessage()
                        playing = compTurn = False
                    elif comp.totalHand == player.totalHand:
                        if abs(comp.totalHand - 21) > 4:
                            comp.hitComp(deck)
                            time.sleep(1)
                        else:
                            victMessage()
                            playing = compTurn = False
            elif decision == "2" or decision.lower() == "hit":
                player.hitPlayer(deck)
            else:
                print("\nPlease pick 1 of the 2 options.")
                count = 2
        elif player.totalHand == 21:
            victMessage()
            break
        elif player.totalHand > 21:
            bustMessage()
            break

def bustMessage():
    global player, comp
    player.show()
    print("You went over with a hand of {}. The House wins ${} of your money!\nYou have ${} left.".format(player.totalHand,player.totalBet,player.money))
    print("--\n--\n--\n--\n--\n");time.sleep(1)

def victMessage():
    global player, comp
    if player.totalHand == comp.totalHand:
        print("Draw! No one wins.")
        player.money += player.totalBet + 15
    elif comp.totalHand == 21:
        print("Blackjack! But not for you. The House wins ${} of your money!.".format(player.totalBet))
    elif player.totalHand == 21:
        print("Blackjack! {} adds ${} to their total money! Congrats.".format(player.name,30))
        player.totalHand = 0
        if len(player.hand) == 2:
            player.money += (player.totalBet*2)+30
        else:
            player.money += (player.totalBet*2)+30
    print("--\n--\n--\n--\n--\n"); time.sleep(1)

def finalMessage():
    global player, comp
    if player.totalHand == comp.totalHand:
        print("Draw! No one wins.")
        player.money += player.totalBet + 15
    elif comp.totalHand > 21:
        print("{} has won because The House busted! ${} has been added to your total money! Congrats.".format(player.name,player.totalBet))
        player.money += (player.totalBet*2)+15
    elif (player.totalHand > comp.totalHand and player.totalHand < 21) or (comp.totalHand < player.totalHand):
        print("{} has won by {}, and ${} has been added to your total money! Congrats.".format(player.name,player.totalHand-comp.totalHand,player.totalBet))
        player.money += (player.totalBet*2)+15
    elif (player.totalHand < comp.totalHand) or (comp.totalHand > player.totalHand and comp.totalHand < 21):
        print("The House wins by {}, and takes ${} of your money!".format((comp.totalHand-player.totalHand),player.totalBet))
    else:
        print("{} for House. {} for you".format(comp.totalHand,player.totalHand))
    print("--\n--\n--\n--\n--\n"); time.sleep(1)


if __name__ == '__main__':
    #Important Variables
    player = 0; comp = Computer(); deck = Deck(); vict = False; bust = False; compBust = False; compVict = False; playing = True; playLoop = True
    # Welcome & Rules
    welcomeMesg()
    # Shuffle Deck
    count = 0
    shuffle(deck)
    # Game
    while True:
        if playLoop == True:
            while player.money > 15:
                # Reset
                if len(deck.discards) > 40:
                    deck.cards = []
                    deck.discards = []
                    shuffle(deck)
                # 15 Dollar Bet
                minBet()
                # Game Start
                initialBet()
                dealCards(player, comp, deck)
                showStatus()
            # Game Over
            while True:
                playAgain = input("The House has taken all of your money...\nWould you like to buy back in?\n'Y' or 'N': ")
                if playAgain.upper() == 'Y':
                    player.money = 100
                    break
                elif playAgain.upper() == 'N':
                    playLoop = False
                    break
                else:
                    print("\nInvalid Entry.\n")
        break
