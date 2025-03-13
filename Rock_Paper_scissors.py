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
your_choice = input("your choice: ").lower()
if your_choice == "rock":
    print(rock)
elif your_choice == "paper":
    print(paper)
elif your_choice != "rock" or your_choice != "paper" or your_choice != "scissors":
    print("Invalid Input!")
else:
    print(scissors)



import random
rock_paper_scissor = random.randint(0,2)
print("Computer Choice")
if rock_paper_scissor == 0:
    print(rock)
elif rock_paper_scissor == 1:
    print(paper)
else:
    print(scissors)

if rock_paper_scissor == 0:
    if your_choice == "rock":
        print("Draw")
    elif your_choice == "paper":
        print("You Loose")
    else:
        print("You Win")
elif rock_paper_scissor == 1:
    if your_choice == "rock":
        print("You Win")
    elif your_choice == "paper":
        print("Draw")
    else:
        print("You Loose")
else:
    if your_choice == "rock":
        print("You Loose")
    elif your_choice == "paper":
        print("You Win")
    else:
        print("Draw")