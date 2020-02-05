import random
#======================================================
#VARIABLE FIELD
#STRUCTURE: THE GAME COSIST IN 3 DIFFICULT LEVELS
#LEVEL 1 = RANGE BETWEEN 1 AND 10 AND 5 ATTEMPTS
#LEVEL 2 = RANGE BETWEEN 1 AND 50 AND 10 ATTEMPTS
#LEVEL 3 = RANGE BETWEEN 1 AND 100 AND 15 ATTEMPTS
#======================================================
secret_number_easy = random.randint(1, 10)
secret_number_normal = random.randint(1, 50)
secret_number_hard = random.randint(1,100)
attempts_easy = 5
attempts_normal = 10
attempts_hard = 15
count = 0

name = input("Hello Sir/Madame, may i have your name please?: ")
answer = input(f"Hello {name}, Welcome to 'Guess a Number', do you know how to play the game?(Y/N)")
level = int(input("Please choose a level: "))

#======================================================
#CORE GAME CODE
#======================================================
if level == 1:
    for attempt in range(attempts_easy):
        count = count + 1
        guess = int(input("Input a number: "))
        if guess < secret_number_easy:
            print("The secret number is higher")
        elif guess > secret_number_easy:
            print("The secret number is lower")
        else:
            print("="*50)
            print("You guessed the secret number. The number was: {}".format(secret_number_easy))
            print("You guessed it in {} attempts".format(count))
            print("=" * 50)
            break
    if guess != secret_number_easy:
        print("sorry you reached the maximum number of attempts......looser!!:)")
        print("The secret number was {}".format(secret_number_easy))

elif level == 2:
    for attempt in range(attempts_normal):
        count = count + 1
        guess = int(input("Please input a number: "))
        if guess < secret_number_normal:
            print("The secret number is higher")
        elif guess > secret_number_normal:
            print("The secret number is lower")
        else:
            print("=" * 50)
            print("You guessed the secret number. The number was: {}".format(secret_number_normal))
            print("You guessed it in {} attempts".format(count))
            print("=" * 50)
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
            print("=" * 50)
            print("You guessed the secret number. The number was: {}".format(secret_number_hard))
            print("You guessed it in {} attempts".format(count))
            print("=" * 50)
    if guess != secret_number_hard:
        print("sorry you reached the maximum number of attempts......looser!!:)")
        print("The secret number was {}".format(secret_number_hard))
