#import module for handling two decimal place rounding
from decimal import *

#Dictionaries have been used to allow easy addition of various elements
#The printing methods have been designed to print each element regardless of length

#To add an item please follow form {#: {'name': '%s', 'price': #.##}
itemArray_2d = {1: {'name': 'chocolate bar', 'price': 1.50}, 
                2: {'name': 'energy bar', 'price':1.00},
                3: {'name': 'can of soda', 'price':1.25},
                4: {'name': 'pack of lollies', 'price':0.50},
                5: {'name': 'apple', 'price':0.75}}
               
#To add an item please follow form {#: {'name': '%s', 'value':#}                
menuArray_2d = {1: {'name': 'Insert Coin', 'value':1}, 
                2: {'name': 'Buy Item', 'value':2},
                3: {'name': 'Return Change', 'value':3}}

#To add an item please follow form {#: {'name': '%s', 'value': #.##, 'quantity':0}
#NOTE: Quantity is only displayed during returnChange(). Serves no other purpose
coinArray_2d = {1: {'name': 'penny', 'value':0.01, 'quantity':0},
                2: {'name': 'dime', 'value':0.05, 'quantity':0},
                3: {'name': 'nickel', 'value':0.10, 'quantity':0},
                4: {'name': 'quarter', 'value':0.25, 'quantity':0},
                5: {'name': 'dollar', 'value':1.00, 'quantity':0}}

invalidInput = "Invalid input, please try again"
insufficientFunds = "You have insufficient funds, please try again"
itemMenuBanner = "-----------------\n|   Item Menu   |\n-----------------"
coinMenuBanner = "-----------------\n|   Coin Menu   |\n-----------------"
mainMenuBanner = "-----------------\n|   Main Menu   |\n-----------------"

class vendingMachine():
    
    credit = 0

    def printExitMsg(self):
        print()
        print('Thank you for using my vending machine, enjoy your purchase!')
        input('Press key to exit')
        return

    def printWelcomeMsg(self):
        print('Welcome to the vending machine.\n ------------------------------')
        return

    def printCredit(self):
        #To avoid floating point errors method rounds to 2 decimal places
        TWOPLACES = Decimal(10) ** -2 #same as Decimal(0.01)
        
        value = Decimal(self.credit).quantize(TWOPLACES)
        print('Credit remaining: ', value)
        return

    def returnChange(self):
        #Method cycles through coin dictionary (highest denomination --> lowest) checking the coin value 
        #against the current credit amount, subtracting it and adding one to the quantity if credit>coin value
        #prints summary of coins returned. Pretty ugly formatting, feel free to change it. 
        
        
        print("You were returned: ")
        for coin in coinArray_2d:
            while(self.credit >= coinArray_2d[len(coinArray_2d)-coin+1]['value']):
                self.credit -= coinArray_2d[len(coinArray_2d)-coin+1]['value']
                coinArray_2d[len(coinArray_2d)-coin+1]['quantity'] += 1   
            #ignore error, still works fine
            print(coinArray_2d[len(coinArray_2d)-coin+1]['quantity'],coinArray_2d[len(coinArray_2d)-coin+1]['name'],end=' ')
        print()
        return    
        
    def checkCredit(self, selection):
        #Checks the price of the item passed, with the current credit amount
        index = int(selection)
        
        if self.credit >= itemArray_2d[index]['price']:
            return 1
        else:  
            return 0    
        
    def getItemMenuSelection(self):
        #Gets user selection, checks the item price against the current credit amount. 
        
        exit = False
        #Loop to allow continuous selection
        while(exit != True):
            self.displayItemMenu()
            self.printCredit()
            selection = input("Your selection: ")
            #Check if input is valid
            if selection.isdigit() and int(selection) <= len(itemArray_2d):
                userSelection = int(selection)
                if userSelection == 0:
                    exit = True
                else:
                    if self.checkCredit(userSelection):
                        self.credit -= itemArray_2d[userSelection]['price']
                        print("You have bought a", itemArray_2d[userSelection]['name'])
                    else:
                        print(insufficientFunds)

            else:
                print(invalidInput)
        return
        
        
    def getMainMenuSelection(self):
        
        exit = False
        while(exit != True):
            self.displayMainMenu()
            self.printCredit()
            selection = input("Your selection: ")
            if selection.isdigit() and int(selection) <= len(menuArray_2d):
                userSelection = int(selection)
                if userSelection == 0:
                    self.printExitMsg()
                    exit = True
                elif userSelection == 1:
                    self.getCoinSelection()
                elif userSelection == 2:
                    self.getItemMenuSelection()
                elif userSelection == 3:
                    self.returnChange()
            else:
                print(invalidInput)
        return


    def getCoinSelection(self):
        
        exit = False
        while(exit != True):
            self.displayCoinMenu()
            self.printCredit()
            selection = input("Your selection: ")
            if selection.isdigit() and int(selection) <= len(coinArray_2d):
                userSelection = int(selection)
                if userSelection == 0:
                    exit = True
                else: 
                    self.credit += coinArray_2d[userSelection]['value']
            else:
                print(invalidInput)
        return


    def displayItemMenu(self):
        #general item printing method, allows for additional items to be appended by adding them to the 
        #to the 'itemArray_2d' dictionary
        print()
        print(itemMenuBanner)
        counter = 1
        for item in itemArray_2d:
            print("{}. {} ${}".format(counter, itemArray_2d[item]['name'].capitalize(), itemArray_2d[item]['price']))
            counter += 1
        print('0. Return to main menu')
        return

    def displayCoinMenu(self):
        #general coin printing method, allows for additional coins to be appended by adding them to the
        #to the 'coinArray_2d' dictionary
        print()
        print(coinMenuBanner)
        counter = 1
        for item in coinArray_2d:
            print("{}. {} ${}".format(counter, coinArray_2d[item]['name'].capitalize(), coinArray_2d[item]['value']))
            counter += 1
        print('0. Return to main menu')
        return

    def displayMainMenu(self):
        #general menu printing method, allows for extension of main menu by adding different options
        #to the 'menuArray_2d' dictionary
        print()
        print(mainMenuBanner)
        for item in menuArray_2d:
            print("{}. {}".format(menuArray_2d[item]['value'], menuArray_2d[item]['name']))
        print('0. EXIT vending machine')
        return

    #                       #
    #   START OF PROGRAMM   #
    #                       #

def main():
    vend = vendingMachine()
    vend.printWelcomeMsg()
    vend.getMainMenuSelection()
    return;

if __name__ == "__main__":
    main()
