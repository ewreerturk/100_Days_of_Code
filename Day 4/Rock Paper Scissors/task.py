import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS = [rock, paper, scissors]


computer_choose = random.choice(RPS)

choose = int((input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")))



if choose == 0 or choose == 1 or choose == 2:
    print("Yarisma basladi")

    if choose == 0 and computer_choose == rock:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("equal")
    elif choose == 0 and computer_choose == paper:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("computer win")
    elif choose == 0 and computer_choose == scissors:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("user win")
    elif choose == 1 and computer_choose == rock:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("user win")
    elif choose == 1 and computer_choose == paper:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("equal")
    elif choose == 1 and computer_choose == scissors:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("computer win")
    elif choose == 2 and computer_choose == rock:
        print("Computer Choose:", computer_choose)
        print("User choose", RPS[choose])
        print("computer win")
    elif choose == 2 and computer_choose == paper:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("user win")
    elif choose == 2 and computer_choose == scissors:
        print("Computer Choose:", computer_choose)
        print("User choose",RPS[choose])
        print("equal")
else:
    print("Yanlis deger  girdiniz")
