import random
from time import sleep


class Roulette:
    def __init__(self,balance):
        self.balance = balance
        self.pick=None
        self.color_pick_red=(1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
        self.color_pick_black=(2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35)        
        self.number_pick_odd=(1,3,5,7,9,11,13,15,17,17,19,21,23,25,27,29,31,33,35)
        self.number_pick_even=(2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34)
        
    def rule(self):
        print("Hello! Welcome to Roulette Wheel")
        self.name=input("Enter your character name  ")
        print("Hello! ",str.upper(self.name) , "Welcome to Roulette Wheel")
        print("You have a reward of 40 Coins")
        sleep(1) 
        print("GAME RULE!")
        sleep(2) 
        print("ENTER YOUR BET BY TYPE IN THE NUMBER 0 TO 36  OR COLOR   OR black")
        sleep(2) 
        print("IF THE WINNING NUMBER AND YOUR NUMBER IS MATCHED! YOU WIN X36 OF YOUR BET")
        sleep(2) 
        print("IF YOUR PICKS AND THE WINNING NUMBER IS MATCHED! ")
            
        print("YOU DOUBLE YOUR BET")
    def  picking(self):
        while self.balance > 0:
            self.pick = input("PLACE YOUR PICK: ")
            if self.pick.upper()=="RED"  or self.pick.upper()=="BLACK":
                print("You picked",str.upper(self.pick) )
                self.bet()
                self.decicions()
                return  
            elif int(self.pick)>=0 and int(self.pick)<=36:
                print("You picked",str (self.pick))
                self.bet()
                self.decicions()
                return 
            else :
                print("Your have pick an invalid pick. Please try to enter your pick again.")
                continue   
 
    def bet(self):
        bet=int(input("How many coins you want to bet?" ))
        if bet <= self.balance :
            self.balance = self.balance - bet
            self.selected[self.pick]=bet
            print("You picked (number:bet): ", self.selected)
            return self.balance
        elif bet > self.balance:
            print("You don't have that much coins left!!")
            self.picking()

    def play(self):
        self.selected={}
        self.picking()
        winning_number= random.randint(-1,37)
        print("Winning Number ",str(winning_number))    
        if self.selected.keys==winning_number :
            print("YOU WON!!")
            print("You Total Coin is" ,str(self.balance))
            self.balance = (self.bet*36)+ self.balance
            return self.balance
        elif self.selected.keys =="red" and winning_number in self.color_pick_red:
            print("YOU WON!!")
            self.balance=(self.balance +(self.bet*2))
            print("Your Total Coin is" ,str(self.balance))
            return self.balance
        elif self.selected.keys=="black" and winning_number in self.color_pick_black:
            print("YOU WON!!")
            self.balance=self.balance +(self.bet*2)
            print("Your Total Coin is" ,str(self.balance))
            return self.balance
        else:
            print("YOU LOST!")
            self.check()
        
    def check(self):
        if self.balance == 0:
            self.ask()
        elif self.balance > 0:
            print("Your Current balance is:",self.balance)
            self.play()

    def decicions(self):
        print("         =======Roulette=======        ")
        print("-------------------------------------")
        print("|1. PLACE MORE PICK   |2.LET'S ROLL   ")
        print("---------------------------------------")
        decicion=int(input("Enter your decicion: "))
        if decicion == 1 :
            self.picking()
            return self.balance
        elif decicion == 2:
            return
        else:
            print("Invalid selection!")
            self.decicions()

    def ask(self):
        print("       ======Roulette======       ")
        print("----------------------------------")
        print("|1. PLAY AGAIN(Y)   |  2. QUIT(N) ")
        print("----------------------------------")
        choice=str(input("Do you want to give it another try?:"))
        if choice == "1" or choice.upper()== "YES" or choice.upper()=="Y":  
            self.balance = 40   
            self.play()
        elif choice == "2" or choice.upper()=="NO" or choice.upper()=="N":
            print("GOOD BYE", self.name)
            exit()
        else:
            print("Please Enter YES/NO or 1|2:")
            self.ask()
    



x=Roulette(40)
x.rule()
x.play()
