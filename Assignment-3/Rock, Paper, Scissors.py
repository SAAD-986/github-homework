p1 = input("Player 1 (rock, paper, scissors): ").lower()
p2 = input("Player 2 (rock, paper, scissors): ").lower()

if p1 == p2:
    print("Tie")
elif p1 == "rock":
    if p2 == "scissors":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif p1 == "paper":
    if p2 == "rock":
        print("Player 1 wins")
    else:
        print("Player 2 wins")
elif p1 == "scissors":
    if p2 == "paper":
        print("Player 1 wins")
    else:
        print("Player 2 wins")