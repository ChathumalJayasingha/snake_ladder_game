

import random

ladder={1:5,4:14,10:20,12:15}
snack={3:1,9:2,14:6}

pos1=0
pos2=0

def move(pos):
    dice=random.randint(1,6)
    print(f"Dice:{dice}")
    pos=pos+dice
    if pos in snack:
        print("Bitten snack")
        pos=snack[pos]
        print(f"Position:{pos}")
    elif pos in ladder:
        print("Climbed by ladder")
        pos=ladder[pos]
        print(f"Position:{pos}")
    else:
        print(f"Position:{pos}")
    print("\n")
    return pos

while True:
    A=input("Player 1 Enter \"A\" to throw dice")
    pos1=move(pos1)
    if pos1>=20:
        print("Game over \n Player 1 wins")
        break
    B=input("Player 2 Enter \"A\" to throw dice")
    pos1=move(pos1)
    if pos2>=20:
        print("Game over \n Player 2 wins")
        break
    