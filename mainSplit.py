import random
import time
import itertools
import threading
import sys

class Card:
    def __init__(self, val, suit):
        self.suit = suit
        self.value = val
    def show(self):
        print("{} of {}".format(self.value,self.suit))

# Deck Class and Functions
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

def shuffling(redo):
    done = False

    if redo == True:
        sys.stdout.write('\n')
    else:
        print('\n')
    def animateShuffle():
        for c in itertools.cycle(['.', '..', '...',' ','  ','   ']):
            if done:
                break
            sys.stdout.write('\rShuffling Deck' + c)
            time.sleep(0.17)
        sys.stdout.write('\nDeck Shuffled!')

    b = threading.Thread(target=animateShuffle)
    b.start()

    #Process Length
    time.sleep(1)
    done = True

def building():
    done = False

    print('\n')
    def animateBuild():
        for c in itertools.cycle(['.', '..', '...',' ','  ','   ']):
            if done:
                break
            sys.stdout.write('\rBuilding Deck' + c)
            time.sleep(0.17)
        sys.stdout.write('\nDeck Built!     ')
    
    s = threading.Thread(target=animateBuild)
    s.start()

    #Process Length
    time.sleep(1)
    done = True

def addingMoney():
    done = False

    def animateMoney():
        for c in itertools.cycle(['.', '..', '...',' ','  ','   ']):
            if done:
                break
            sys.stdout.write('\rAdding Money' + c)
            time.sleep(0.17)
        sys.stdout.write('\n$100 Added!     ')
    
    m = threading.Thread(target=animateMoney)
    m.start()

    #Process Length
    time.sleep(1)
    done = True

def shuffle(deck, auto, redo):
    #if auto == False:
    if redo == True:
        deck.build()
        deck.shuffleCards()
        print('Deck has run out of Cards.'); time.sleep(1)
        print('Reshuffle required.'); time.sleep(1)
        shuffling(redo); time.sleep(1)
        sys.stdout.write('\n')
    else:
        deck.build()
        deck.shuffleCards()
        addingMoney(); time.sleep(1)
        building(); time.sleep(1)
        shuffling(redo); time.sleep(1)
        sys.stdout.write('\n')
    #else:
    #    deck.build()
    #    deck.shuffleCards()

    return deck



# Player Class and Functions
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.splitHand = []
        self.money = 100; self.totalBet = 0; self.totalSplitBet = 0
    def hitPlayer(self, deck):
        self.hand.append(deck.drawCard())
    def hitSplit(self,deck):
        self.splitHand.append(deck.drawCard())
    def handTotal(self, splitTurn):
        global vict, bust

        faceCards = ["Jack","Queen","King"]
        total = ace1 = ace2 = 0

        if splitTurn == False:
            self.totalHand = 0
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
                    print("\n{}'s current hand is worth {}.".format(self.name, self.totalHand))
                else:
                    print("\n{}'s current hand is worth {} or {}.".format(self.name, self.totalHand-11,self.totalHand))
            else:
                print("\n{}'s current hand is worth {}.".format(self.name, self.totalHand))
        
        if splitTurn == True:
            self.totalSplitHand = 0
            for i in self.splitHand:
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

            self.totalSplitHand = ace1+ace2+total
        
            if ace1 > 0:
                if self.totalSplitHand > 21:
                    ace1 = 1
                    self.totalHand = ace1+ace2+total
                    print("\n{}'s second hand is worth {}.".format(self.name, self.totalSplitHand))
                else:
                    print("\n{}'s second hand is worth {} or {}.".format(self.name, self.totalSplitHand-11,self.totalSplitHand))
            else:
                print("\n{}'s second hand is worth {}.".format(self.name, self.totalSplitHand))

    def show(self):
        print("\n------------------\n{}'s Hand:\n------------------".format(self.name))
        for i in self.hand:
            i.show()
    def showSplit(self):
        print("\n------------------\n{}'s Second Hand:\n------------------".format(self.name))
        for i in self.splitHand:
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
            elif int(bet) > 0 and int(bet) < 15:
                print("The minimum bet is 15 dollars.\n")
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

def playerTurn(comp, player):
    count = 0
    splitTurn = False
    playing = True
    
    while playing == True:
        if count == 1:
            comp.showInitial(); time.sleep(1)
            player.show(); time.sleep(1)
            player.handTotal(splitTurn); time.sleep(1)

        if player.totalHand < 21:
            count = 1
            decision = input("\n1. Stay\n2. Hit\nInput: ")
            if decision == "1" or decision.lower() == "stay":
                computerTurn(comp, player)
                playing = False
            elif decision == "2" or decision.lower() == "hit":
                player.hitPlayer(deck)
            else:
                print("\nPlease pick 1 of the 2 options.")
        elif player.totalHand == 21:
            victMessage()
            break
        elif player.totalHand > 21:
            bustMessage()
            break

def playerTurnSplit(comp, player):
    global playing, playingSplit

    count = 0
    splitTurn = False
    decision = ""
    decision2 = ""

    while playing == True:
        if count == 1:
            comp.showInitial(); time.sleep(1)
            player.show(); time.sleep(1)
            player.handTotal(splitTurn); time.sleep(1)
            if player.totalHand >= 21:
                decision = "1"
        elif count == 0:
            count = 1

        if decision != "1":
            decision = input("\n1. Stay\n2. Hit\nInput: ")
        else:
            pass
        
        if decision == "1" or decision.lower() == "stay":
            count = 0
            splitTurn = True
            comp.showInitial(); time.sleep(1)
            player.showSplit(); time.sleep(1)
            player.hitSplit(deck)
            player.showSplit(); time.sleep(1)
            player.handTotal(splitTurn); time.sleep(1)
            while playingSplit == True:
                if count == 1:
                    comp.showInitial(); time.sleep(1)
                    player.showSplit(); time.sleep(1)
                    player.handTotal(splitTurn); time.sleep(1)
                    if player.totalSplitHand >= 21:
                        decision2 = "1"
                elif count == 0:
                    count = 1

                if decision2 != "1":
                    decision2 = input("\n1. Stay\n2. Hit\nInput: ")
                else:
                    pass

                if decision2 == "1" or decision2.lower() == "stay":
                    computerTurnSplit(comp, player)
                    playing = False
                    playingSplit = False
                elif decision2 == "2" or decision2.lower() == "hit":
                    player.hitSplit(deck)
                else:
                    print("\nPlease pick 1 of the 2 options.")
                if player.totalSplitHand >= 21:
                    decision2 = "1"
        elif decision == "2" or decision.lower() == "hit":
            player.hitPlayer(deck)
        else:
            print("\nPlease pick 1 of the 2 options.")

def setName():
    playerName = ""
    while playerName == "":
        playerName = input("\nType your player's name: ")
        if playerName == "":
            print("Please Enter Something.\n")
    sys.stdout.write('\n')
    
    return playerName



# Computer Class and Functions
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

def computerTurnSplit(comp, player):
    compTurn = True

    while compTurn == True:
        comp.showAll(); time.sleep(1)
        comp.compHandTotal(); time.sleep(1)
        if comp.totalHand > 21:
            splitMessage()
            compTurn = False
        elif comp.totalHand == 21:
            splitMessage()
            compTurn = False
        elif comp.totalHand >= 17:
            splitMessage()
            compTurn = False
        elif comp.totalHand < 17:
            if comp.totalHand < player.totalHand or comp.totalHand < player.totalSplitHand:
                comp.hitComp(deck)
                time.sleep(1)
            else:
                splitMessage()
                compTurn = False

def computerTurn(comp, player):
    comp.totalHand = 0
    compTurn = True

    while compTurn == True:
        comp.showAll(); time.sleep(1)
        comp.compHandTotal(); time.sleep(1)
        if comp.totalHand > 21:
            finalMessage()
            compTurn = False
        elif comp.totalHand == 21:
            victMessage()
            compTurn = False
        elif comp.totalHand >= 17:
            finalMessage()
            compTurn = False
        elif comp.totalHand < 17:
            if comp.totalHand < player.totalHand:
                comp.hitComp(deck)
                time.sleep(1)
            else:
                finalMessage()
                compTurn = False



# Message Functions
def welcomeMesg():
    print(
    '''
    Welcome to Blackjack!!!
    
    The object of the blackjack game is to accumulate cards with point totals as close to 21 without going over 21.
    Face cards (Jacks, Queens and Kings) are worth 10 points. Aces are worth 1 or 11, whichever is preferable.
    Other cards are represented by their number. If player and the House tie, it is a push and no one wins.
    Ace and 10 (Blackjack) on the first two cards dealt is an automatic player win at 1.5 to 1, unless the house ties.
    A player may stay at any time.
    '''
    )

def bustMessage():
    global player, comp
    player.show()
    print("You went over with a hand of {}. The House wins ${} of your money!\nYou have ${} left.".format(player.totalHand,player.totalBet,player.money))
    print("--\n--\n--\n--\n--\n");time.sleep(1)

def victMessage():
    global player, comp
    if player.totalHand == comp.totalHand:
        print("The House had 21 as well. Draw! No one wins.")
        player.money += player.totalBet
    elif comp.totalHand == 21:
        print("Blackjack! But not for you. The House wins ${} of your money!.".format(player.totalBet))
    elif player.totalHand == 21:
        print("Blackjack! {} adds ${} to their total money! Congrats.".format(player.name,player.totalBet*1.5))
        player.totalHand = 0
        player.money += (player.totalBet)+player.totalBet*1.5
    print("--\n--\n--\n--\n--\n"); time.sleep(1)

def finalMessage():
    global player, comp

    if player.totalHand == comp.totalHand:
        print("Draw! No one wins.")
        player.money += player.totalBet
    elif comp.totalHand > 21:
        print("{} has won because The House busted! ${} has been added to your total money! Congrats.".format(player.name,player.totalBet))
        player.money += player.totalBet*2
    elif (player.totalHand > comp.totalHand and player.totalHand < 21) or (comp.totalHand < player.totalHand):
        print("{} has won by {}, and ${} has been added to your total money! Congrats.".format(player.name,player.totalHand-comp.totalHand,player.totalBet))
        player.money += player.totalBet*2
    elif (player.totalHand < comp.totalHand) or (comp.totalHand > player.totalHand and comp.totalHand < 21):
        print("The House wins by {}, and takes ${} of your money!".format((comp.totalHand-player.totalHand),player.totalBet))
    print("--\n--\n--\n--\n--\n"); time.sleep(1)

def splitMessage():
    global player, comp

    hand1 = "first Hand"
    hand2 = "second Hand"
    compBlackjack = False
    blackjack1 = False
    blackjack2 = False
    
    if comp.totalHand == 21:
        compBlackjack = True
    
    if player.totalHand == 21:
        blackjack1 = True
    
    if player.totalSplitHand == 21:
        blackjack2 = True
    
    if blackjack1 or blackjack2 or compBlackjack:
        if compBlackjack and blackjack1 and blackjack2:
            print("Everyone got blackjack... THATS INSANE! But you don't win any money.")
            player.money += player.totalBet
        elif compBlackjack and blackjack1 and comp.totalHand > player.totalSplitHand:
            print("The House tied the {}'s blackjack, but beat your {}. You get ${} added to your money.".format(hand1,hand2,player.totalBet*1.5))
            player.money += player.totalBet+player.totalBet*1.5
        elif compBlackjack and blackjack2 and comp.totalHand > player.totalHand:
            print("The House tied the {}'s blackjack, but beat your {}. You get ${} added to your money.".format(hand2,hand1,player.totalBet*1.5))
            player.money += player.totalBet+player.totalBet*1.5
        elif compBlackjack and not blackjack1 and not blackjack2:
            print("The House beat both of your hands with blackjack! You gave the house ${}.".format(player.totalBet*2))
            player.money -= player.totalBet*2
        elif blackjack1 and blackjack2 and not compBlackjack:
            print("Both your hands got blackjack. You win ${}".format((player.totalBet*2)*1.5))
            player.money += (player.totalBet*2)+player.totalBet*1.5
        elif blackjack1 and not blackjack2 and not compBlackjack:
            print("Your {} got blackjack, but not your {}. But your {} beat The House. Good win.\nYou get ${} back.".format(hand1,hand2,hand2,player.totalBet*1.5+player.totalBet))
            player.money += player.totalBet+player.totalBet*1.5
        elif not blackjack1 and blackjack2 and not compBlackjack:
            print("Your {} got blackjack, but not your {}. But your {} beat The House. Good win.\nYou get ${} back.".format(hand2,hand1,hand1,player.totalBet*1.5+player.totalBet))
            player.money += player.totalBet+player.totalBet*1.5
        elif (blackjack1 and not blackjack2 and not compBlackjack) and player.totalSplitHand < comp.totalHand:
            print("Your {} got blackjack, but not {}. Your {} lost to The House.\nYou get ${}.".format(hand1,hand2,hand2,player.totalBet*1.5))
            player.money += player.totalBet+player.totalBet*1.5
        elif (blackjack2 and not blackjack1 and not compBlackjack) and player.totalHand < comp.totalHand:
            print("Your {} got blackjack, but not {}. Your {} lost to The House.\nYou get ${}.".format(hand2,hand1,hand1,player.totalBet*1.5))
            player.money += player.totalBet+player.totalBet*1.5
    else:
        if player.totalHand > 21 and player.totalSplitHand > 21:
            print("Both of your hands busted. You give the house all ${}!".format(player.totalBet*2))
            player.money -= player.totalBet
        elif comp.totalHand > 21 and player.totalHand < 21 and player.totalSplitHand < 21:
            print("{} has won because The House busted! ${} has been added to your total money! Congrats.".format(player.name,player.totalBet))
            player.money += player.totalBet*3
        elif player.totalHand > 21 and player.totalSplitHand == comp.totalHand:
            print("Your {} busted. But your {} tied with The House. No winnings.".format(hand1,hand2))
            player.money += player.totalBet*2
        elif player.totalSplitHand > 21 and player.totalHand == comp.totalHand:
            print("Your {} busted. But your {} tied with The House. No winnings.".format(hand2,hand1))
            player.money += player.totalBet*2
        elif player.totalHand > 21 and player.totalSplitHand < comp.totalHand and player.totalSplitHand < 21:
            print("Your {} busted. But your {} beat The House. You gain {} back!".format(hand1,hand2,player.totalBet*2))
            player.money += (player.totalBet*2)+player.totalBet
        elif player.totalSplitHand > 21 and player.totalHand < comp.totalHand and player.totalHand < 21:
            print("Your {} busted. But your {} beat The House. You gain {} back!".format(hand2,hand1,player.totalBet*2))
            player.money += (player.totalBet*2)+player.totalBet

        elif player.totalHand == player.totalSplitHand == comp.totalHand:
            print("The House pushed with both of your hands!")
            player.money += player.totalBet*2
        elif comp.totalHand > player.totalHand and comp.totalHand > player.totalSplitHand:
            print("The House beat both of your hands! You gave The House ${}.".format(player.totalBet))
            player.money -= player.totalBet
        elif comp.totalHand > player.totalHand and comp.totalHand < player.totalSplitHand:
            print("The House beat your {} with {}, and lost to your {}. You gain {} back!".format(hand1,comp.totalHand,hand2,player.totalBet))
            player.money += player.totalBet*2
        elif comp.totalHand > player.totalHand and comp.totalHand < player.totalSplitHand:
            print("The House beat your {} with {}, and lost to your {}. You gain {} back!".format(hand2,comp.totalHand,hand1,player.totalBet))
            player.money += player.totalBet*2
        elif (player.totalHand > comp.totalHand and player.totalSplitHand > comp.totalHand) and (player.totalHand < 21 and player.totalSplitHand < 21):
            print("Both of your hands beat the house! You get ${}.".format(player.totalBet*2))
            player.money += player.totalBet*3


    print("--\n--\n--\n--\n--\n"); time.sleep(1)



# Splitting Functions
def checkSplit(split):
    splitList = []
    count = 0

    for i in player.hand:
        splitList.append(i.value)
        if splitList[1:] == splitList[:-1] and count == 1:
            split = True
        count += 1

    return split

def splitDecision(player, comp, deck, split, auto):
    while split and not auto:
        splitChance = input("\nWould you like to split?\n'Y' or 'N': ")
        if splitChance.upper() == 'Y':
            player.splitHand.append(player.hand.pop())
            player.show(); time.sleep(1)
            player.hitPlayer(deck)
            player.show(); time.sleep(1)
            player.handTotal(splitTurn)
            showStatus(player, comp, deck, split)
            split = False
            skip = True
        elif splitChance.upper() == 'N':
            showStatus(player, comp, deck, split)
            split = False
            skip = True
        else:
            print("\nInvalid Entry.\n")

    compDecision = random.randint(0,1)

    if auto == True and split == True:
        if compDecision == 1:
            print("\n*Computer Chose To Split*\n"); time.sleep(1)
            player.splitHand.append(player.hand.pop())
            player.show(); time.sleep(1)
            player.hitPlayer(deck)
            player.show(); time.sleep(1)
            player.handTotal(splitTurn)
            showStatusAuto(player, comp, deck, split)
        else:
            print("\n*Computer Chose To Not Split*\n"); time.sleep(1)
            split = False
            skip = False
            showStatusAuto(player, comp, deck, split)



# Automatic Game
def gameAutoSplit(comp, player):
    count = 0
    player.totalHand = 0
    playerTurn = True
    playerSplitTurn = True
    splitTurn = False

    while playerTurn == True:
        if count == 1:
            player.show(); time.sleep(1)
            player.handTotal(splitTurn); time.sleep(1)
        count = 1
        if player.totalHand > 21:
            playerTurn = False
        elif player.totalHand == 21:
            playerTurn = False
        elif player.totalHand >= 17:
            playerTurn = False
        elif player.totalHand < 17:
            player.hitPlayer(deck)
            time.sleep(1)
    
    while playerSplitTurn == True:
        splitTurn = True
        if count == 1:
            player.showSplit(); time.sleep(1)
            player.handTotal(splitTurn); time.sleep(1)
        count = 1
        if player.totalSplitHand > 21 and player.totalHand > 21:
            splitMessage()
            playerSplitTurn = False
        elif player.totalSplitHand > 21:
            computerTurnSplit(comp,player)
            playerSplitTurn = False
        elif player.totalSplitHand == 21:
            computerTurnSplit(comp,player)
            playerSplitTurn = False
        elif player.totalSplitHand >= 17:
            computerTurnSplit(comp,player)
            playerSplitTurn = False
        elif player.totalSplitHand < 17:
            player.hitSplit(deck)
            time.sleep(1)

def gameAuto(comp, player):
    player.totalHand = 0
    playerTurn = True
    splitTurn = False
    count = 0

    while playerTurn == True:
        if count == 1:
            player.show(); time.sleep(1)
        count = 1
        player.handTotal(splitTurn); time.sleep(1)
        if player.totalHand > 21:
            bustMessage()
            playerTurn = False
        elif player.totalHand == 21:
            victMessage()
            playerTurn = False
        elif player.totalHand >= 17:
            computerTurn(comp,player)
            playerTurn = False
        elif player.totalHand < 17:
            player.hitPlayer(deck)
            time.sleep(1)

def showStatusAuto(player, comp, deck, split):
    global bust, vict, compBust, compVict

    skip = True

    if split:
        gameAutoSplit(comp, player)
        skip = False

    if skip:
        gameAuto(comp, player)



# Normal Game
def dealCards(player, comp, deck, auto):
    splitTurn = False
    player.hand = []
    comp.compHand = []
    player.hitPlayer(deck); time.sleep(1); player.show()
    comp.hitComp(deck); time.sleep(1); 
    comp.showStart()
    player.hitPlayer(deck); time.sleep(1); player.show()
    comp.hitComp(deck); time.sleep(1)
    comp.showInitial(); time.sleep(1); 
    if auto == False:
        player.handTotal(splitTurn)

def initialBet(auto):
    global player
    while True:
        if auto:
            player.totalBet = 0
            print("\nMinimum bet is $15."); time.sleep(0.5)
            print("\nYour current balance is ${}.".format(player.money)); time.sleep(0.5)
            amount = 15
            player.betMoney(amount)
        else:
            player.totalBet = 0
            print("\nMinimum bet is $15."); time.sleep(0.5)
            print("\nYour current balance is ${}.".format(player.money)); time.sleep(0.5)
            amount = input("How much would you like to bet: ")
            player.betMoney(amount)
        return player

def showStatus(player, comp, deck, split):
    global bust, vict, compBust, compVict

    skip = True

    if split:
        playerTurnSplit(comp, player)
        skip = False

    if skip:
        playerTurn(comp, player)

def gameOver(auto):
    global playLoop

    playAgain = True

    if auto:
        player.money = 100
    else:
        while playAgain == True:
            playAgainInput = input("The House has taken all of your money...\nWould you like to buy back in?\n'Y' or 'N': ")
            if playAgainInput.upper() == 'Y':
                player.money = 100
                break
            elif playAgainInput.upper() == 'N':
                playLoop = False
                break
            else:
                print("\nInvalid Entry.\n")
    
    return playLoop


# Main Program
if __name__ == '__main__':
    #Important Variables
    comp = Computer(); deck = Deck(); vict = False; bust = False; compBust = False; compVict = False; playing = True; playLoop = True; split = False; skip = False; splitTurn = False; autoLoop = True; playing = True; playingSplit = True; redo = False; test = False

    # Welcome & Rules
    welcomeMesg()

    # Autoplay
    while autoLoop == True:
        auto = input("You can either play the game or watch it. Which one?\n1. Play\n2. Automate\n\nInput: ")
        if auto == "1" or auto.lower() == "play":
            auto = False
            autoLoop = False
        elif auto == "2" or auto.lower() == "automate":
            print("\n*Automation Has Begun*\n")
            auto = True
            autoLoop = False
        else:
            print("\nPlease pick 1 of the 2 options.\n")

    if auto == False:
        player = Player(setName().title())
    elif auto == True:
        player = Player("Test")

    # Shuffle Deck
    count = 0
    shuffle(deck, auto, redo)

    # Game Start
    while True:
        if playLoop == True:
            while player.money > 15:

                # Reset
                if len(deck.discards) > 40:
                    redo = True
                    deck.cards = []
                    deck.discards = []
                    shuffle(deck, auto, redo)

                # Game Start
                if test == False:
                    initialBet(auto)
                dealCards(player, comp, deck, auto)

                # Possible Split
                split = False
                split = checkSplit(split)
                splitDecision(player, comp, deck, split, auto)

                if skip == False and auto == False:
                    showStatus(player, comp, deck, split)
                elif skip == False and auto == True:
                    gameAuto(comp, player)

            # Game Over
            gameOver(auto)
        
        # Final Check
        if playLoop == True:
            pass
        else:
            break
