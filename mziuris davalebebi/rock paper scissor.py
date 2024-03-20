import random

user = 0
pc = 0

print("tamashi aris 3 qulamde")
while pc < 3 and user < 3:
    combinacia = ["Rock", "Paper", "Scissor"]
    pc_choice = random.choice(combinacia)
    user_choice = input("Rock, Paper, Scissor: ")

    print(f"pc: {pc_choice} vs user: {user_choice}")

    if pc_choice == "Rock" and user_choice == "Paper":
        user += 1
        print("You Win, 1 qula")
    elif pc_choice == "Paper" and user_choice == "Scissor":
        user += 1
        print("You Win, 1 qula")
    elif pc_choice == "Scissor" and user_choice == "Rock":
        user += 1
        print("You Win, 1 qula")
    elif pc_choice == user_choice:
        print("Tie, veravin ver aigo qula, shemdegi raundi")
    else:
        pc += 1
        print("pc Win, 1 qula")

if user > pc:
    print("YOU WIN!")
else:
    print("PC WINS!, YOU LOOSE")



