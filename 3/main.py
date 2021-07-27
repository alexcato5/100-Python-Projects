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
input("<< PRESS ENTER TO START THE GAME >>")

print('''
    First story
''')

first_choice = input("Do you want to go LEFT or RIGHT?\n\t>")

if first_choice.lower() != "left":
    print("You fell into a hole and died.\nX  G A M E  O V E R  X")
else:    
    print('''
        Second story
    ''')
    
    second_choice = input("Do you want to SWIM or to WAIT?\n\t>")
    
    if second_choice.lower() != "wait":
        print("You were attacked by an enormous trout and died.\nX  G A M E  O V E R  X")
    else:    
        print('''
            Third story
        ''')
        
        third_choice = input("Which door do you choose (RED/BLUE/YELLOW)?\n\t>")

        if third_choice.lower() == "red":
            print("You encountered a fire and burned.\nX  G A M E  O V E R  X")
        elif third_choice == "blue":
            print("This room was full of wild beasts. They ate you and you died.\nX  G A M E  O V E R  X")
        elif third_choice == "yellow":
            print("(Final Story).\n\n\t>>YOU WON!!!") 