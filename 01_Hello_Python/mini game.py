secret_number=7

while True:
    user_number=int(input("Guess a number between 1 & 10"))
    if secret_number==user_number:
        print("Congratulations !\nYou have guessed it correctly")
        break
    elif secret_number>user_number:
        print("The number you have entered is Too Low")
    elif secret_number<user_number:
        print("The number you have entered is Too High")
    else:
        print("you have entered a wrong information")

