import random
#Tailre customer Welcome
name = input("Hello Sir/Madame, may i have your name please?: ")
answer = input(f"Hello {name}, Welcome to 'Guess a Number', do you know how to play the game?(Y/N)")
secret_number_easy = random.randint(1, 10)
secret_number_normal = random.randint(1, 50)
secret_number_hard = random.randint(1,100)
attempts_easy = 5
attempts_normal = 20
attempts_hard = 25
count = 0
#Show instruction if they choose yes
# if answer.lower() == 'n':
#     print("#"*30)
#     print("The game is simple.")
#     print("I will choose a number")
#     print("And you will have to guess it")
#     print("="*30)
#     print("There are 3")
#     print("#"*30)
level = int(input("Please choose a level: "))

if level == 1:
    for attempt in range(attempts_easy):
        count = count + 1
        guess = int(input("Input a number: "))
        if guess < secret_number_easy:
            print("The secret number is higher")
        elif guess > secret_number_easy:
            print("The secret number is lower")
        else:
            print("\n")
            print("You guessed the secret number. The number was: {}".format(secret_number_easy))
            print("You guessed it in {} attempts".format(count))
    if guess != secret_number_easy:
        print("sorry you reached the maximum number of attempts......looser!!:)")
        print("The secret number was {}".format(secret_number_easy))

elif level == 2:
    for attempt in range(attempts_normal):
        count = count + 1
        guess = int(input("Input a number: "))
        if guess < secret_number_normal:
            print("The secret number is higher")
        elif guess > secret_number_normal:
            print("The secret number is lower")
        else:
            print("\n")
            print("You guessed the secret number. The number was: {}".format(secret_number_normal))
            print("You guessed it in {} attempts".format(count))
    if guess != secret_number_normal:
        print("sorry you reached the maximum number of attempts......looser!!:)")
        print("The secret number was {}".format(secret_number_normal))

elif level == 3:
    for attempt in range(attempts_hard):
        count = count + 1
        guess = int(input("Input a number: "))
        if guess < secret_number_hard:
            print("The secret number is higher")
        elif guess > secret_number_hard:
            print("The secret number is lower")
        else:
            print("\n")
            print("You guessed the secret number. The number was: {}".format(secret_number_hard))
            print("You guessed it in {} attempts".format(count))
    if guess != secret_number_hard:
        print("sorry you reached the maximum number of attempts......looser!!:)")
        print("The secret number was {}".format(secret_number_hard))
