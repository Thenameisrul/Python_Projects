print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
begin = input("Type Left or Right: ")
if begin == "left" or begin == "Left":
   swim_wait = input("""You've come to a lake. There is an island in the middle of the lake.Type "wait" to wait for a boat.
    Type "swim" to swim across""")
   if swim_wait == "wait" or swim_wait == "Wait":
     color = input("You arrive at the island unharmed. There is a house with 3 doors."
                   "One red, one yellow and one blue. Which colour do you choose?")
     if color == "red" or color == "Red":
         print("Burned by Fire and game over")
     elif color == "yellow" or color == "Yellow":
         print("You Win")
     elif color == "blue" or color == "Blue":
         print("Eaten by beast and Game Over")
     else:
         print("Game Over")
   elif swim_wait == "swim" or swim_wait == "Swim":
       print("Attacked by Trout and Game Over")
   else:
       print("Game Over")
elif begin == "right" or begin == "Right":
    print("Fall into a Hole and Game Over")
else:
    print("Game Over")


