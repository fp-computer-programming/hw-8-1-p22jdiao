# Author: JD

"""
Create a program that determines if you are safe or bust in blackjack. 
Prompt the user for the value of their 2 cards and display if they are 
safe or busted. Note: Jack, Queen, and King are all worth 10, and if 
the sum of your cards is under 21, then you are safe.
"""

def blackjack(first_card, second_card):
    if first_card == "Jack" or first_card == "Queen" or first_card == "King":
        first_card = 10
        
    if second_card == "Jack" or second_card == "Queen" or second_card == "King":
        second_card = 10
        
    total = int(first_card) + int(second_card)
    if total < 21:
        return "safe"
    else:
        return "bust"
    
fc = input("The first card is: ")
sc = input("The second card is: ")

result = blackjack(fc,sc)

print("You are", result)

#test
print(blackjack(10, 10) == "safe")
print(blackjack("Jack", "Queen") == "safe")
print(blackjack("Queen", "King") == "safe")
    
