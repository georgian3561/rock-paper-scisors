list = ["rock", "paper", "scissors"]
import random
your_point = 0
my_point = 0
no_of_chances = 0
chance = 10
while no_of_chances<10:
    clients =input((f"Choose one of these {list}\n"))
    rand = random.choice(list)
    print(rand)
    if clients == rand:
        print("draw both get 0 points")
    # if clients choice is  s
    elif clients == "scissors" and rand == "rock":
        my_point = my_point + 1
        print(f"i won\nMy point is {my_point} and Your point is {your_point} ")
    elif clients == "scissors" and rand == "paper":
        your_point = your_point + 1
        print(f"you won one point\nMy point is {my_point} and Your point is {your_point} ")
    elif clients == "paper" and rand == "scissors":
        my_point = my_point + 1
        print(f"i won \nMy point is {my_point} and Your point is {your_point} ")
    elif clients == "paper" and rand == "rock":
        your_point = your_point + 1
        print(f"you won one point\nMy point is {my_point} and Your point is {your_point} ")
    elif clients == "rock" and rand == "paper":
        my_point = my_point + 1
        print(f"you won one point\nMy point is {my_point} and Your point is {your_point} ")
    elif clients == "rock" and rand == "scissors":
        your_point = your_point + 1
        print(f"you won one point\nMy point is {my_point} and Your point is {your_point} ")
    no_of_chances = no_of_chances + 1
    print(f"{chance - no_of_chances} is left out of{chance}")
print("game over")
if my_point > your_point:
    print("i won")
elif my_point < your_point:
    print("you won")
print(f"your score is{your_point} and my is{my_point}\n Congratulations")

