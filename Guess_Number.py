import random     # Importing random module
print("I am thinking of a number between 1 -100. You have five chances to guess it")
n = random.randint(1,100)  # Getting a random number between 1 and 100
count = 1
print("Guess", count, end ="")

guess = int(input("?"))

while n != guess:  # While loop
    if (count == 5 or guess == n):
        print("Sorry you have used all your chances. The correct number is", n)
        break;

    if guess < n:  # If statement that prints a low guess
        print(guess, "is too low")

        count = count + 1
        print("Guess", count, end="")

        guess = int(input(" ? "))

    elif guess > n:  # elif statement that prints a too high guess
           print(guess, "is too high")

           count = count + 1

           print("Guess", count, end ="")

           guess = int(input("? "))

    else:  # else statement that confirms the guess
           print("You are right ! I was thinking of ", guess, "!")

           break