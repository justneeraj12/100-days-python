print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')
print("Welcome to Treasure island.\nYour mission is to find the treasure")
choice1 = input("You are at a crossroad, which way would you like to go?? Right  or Left?\n") #asks the user to choose a path

if choice1 == "left":
  choice2 = input('You\'ve come to a lake, would you to "wait" for a boat or "swim" to cross the lake?\n')
  if choice2 == 'wait':
      choice3 = input("You have arrived to the island unharmed, which room would you like to choice Red, Blue, Yellow??\n")
      if choice3 == "red":
          print("Its a room full of fire, GAME OVER!")
      elif choice3 == 'blue':
          print("Its a room full of monsters, GAME OVER!!")
      elif choice3 == 'yellow':
          print("You found the treasure!! You win!!")
      else:
          print("You chose a door that doesn't exist, GAME OVER!!")
  else:
       print("You've been attacked by a trout and lost")
else:
    print("You've fallen into a hole, you lose!\n")
    
    
    

   
    
