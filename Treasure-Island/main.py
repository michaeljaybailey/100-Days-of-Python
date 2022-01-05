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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice_1 = input("While stepping off the boat, you are met with a fork in the road, where do you head? ENTER left OR right  \n").lower()
if choice_1 == "left":
  choice_2 = input("As you head up the path, you see a river with what seems to be a mysterious object floating towards you. Do you start swimming across or should you wait for the object to pass? ENTER swim OR wait  \n").lower()
  if choice_2 == "wait":
    choice_3 = input("As the object gets closer, you realize it was a pack of piranhas swimming by the whole time. You wait till its safe before swimming across. As you keep treading forward, you enter an abondoned temple and are met with 3 different color doors. Which one do you enter? ENTER red OR blue OR yellow  \n").lower() 
    if choice_3 == "red":
      print("You enter the room to realize you are locked in and flames closing in around you. There is no way out. GAME OVER")
    if choice_3 == "blue":
      print("Just as the door shuts behind you, the floor falls beneath you, sending you falling into a pool of water. You feel snakes slowly wrap around you as you realize there is no way out. GAME OVER")
    if choice_3 == "yellow":
      print("As you enter the room, you begin to see a sparkle at the other end. You have found the treasure and can safely leave with your riches. YOU WIN!")
  else:
    print("You start swimming across as the object gets close. Looking over you see it was a pack of pirhannas and it is too late to get out of the water. GAME OVER")
else:
  print("As you follow the path, you are ambushed by a local tribe, and are taken prisioner to live out your limited days. GAME OVER!")
