#MAIN GAME
def treasureHunt():
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
        *******************************************************************************''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    direction=input("you are at a crossroad!! where do you want to go??\nleft or right??\n")
    if direction=='left':
        print("you fell into a trap")
        print("would you like to retry??")
        again=input("type yes or no\n")
        if again=='yes':
            treasureHunt()
        else:
            print("thanks for playing")
    else:
        print("you notice a figure in the distance...\ndo you want to keep going in this direction???")
        b=input("yes or no\n")
        if b=='no':
            change=input("would you like to go in the left direction???\nyes or no\n")
            if change=='yes':
                print("you died to a trap")
                print("would you like to retry??")
                again = input("type yes or no\n")
                if again == 'yes':
                    treasureHunt()
                else:
                    print("thanks for playing")
        else:
            print("luck is on you side today,the distant figure was your guide")
        print("the guide guides you through the route...\nafter a while you have reached an unknown river")
        river=input("would you swim to the other side or wait for a boat???\ntype swim or boat\n")
        if river=='swim':
            print("you were killed by crocodiles")
            print("would you like to retry??")
            again = input("type yes or no\n")
            if again == 'yes':
                treasureHunt()
            else:
                print("thanks for playing")
        else:
            print("are you sure???\nwaiting for a boat would take time and someone else might take the treasure")
            c=input("yes or no\n")
            if c=='no':
                print("you got greedy\nyou chose to swim and died to crocodiles")
                print("would you like to retry??")
                again = input("type yes or no\n")
                if again == 'yes':
                    treasureHunt()
                else:
                    print("thanks for playing")
            else:
                    print("a very wise decision")
                    print("you have reached the final destination...\nbut there is a slight problem...\nthere are 3 different colored crosses on ground in which 2 are traps and only 1 has treasure in it ")
                    print("there 3 colored crosses that are red,black and white")
                    color=input("choose red/black/white\n")
                    if color=='red':
                        print("unlucky,You died to a landmine")
                        print("would you like to retry??")
                        again = input("type yes or no\n")
                        if again == 'yes':
                            treasureHunt()
                        else:
                            print("thanks for playing")
                    elif color=='black':
                        print("unlucky,You died to a landmine")
                        print("would you like to retry??")
                        again = input("type yes or no\n")
                        if again == 'yes':
                            treasureHunt()
                        else:
                            print("thanks for playing")
                    else:
                        print("CONGRATULATIONS YOU HAVE FOUND THE TREASURE\n")

treasureHunt()
