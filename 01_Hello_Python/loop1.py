import random
secret_number=random.randint(1,10)   
while True:
    user_number=int(input("Guess a number between 1 & 10"))
    if secret_number==user_number:
        print ("You have guessed it right")
    elif user_number>secret_number:
        print("Too High")
    elif user_number<secret_number:
        print("Too Low")
    else:
        print("You have entered wrong information")
    