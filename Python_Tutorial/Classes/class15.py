secret = 9

chances = 3
guess_count = 0
while guess_count < chances:
    guess = int(input("Make a guess: "))
    guess_count += 1
    if guess == secret:
        print("You got it!")
        break
else:
    print("YOU failed ")
