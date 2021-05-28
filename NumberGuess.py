import random
number = random.randint(1,9)
name= input("Hi what's your name?")
chance=0

while chance < 5:
    guess=int(input(name + ", enter your guess between 1 and 9:"))
    if guess==number:
        print("Congratulations!" + name + " Your guess is right.")
        break
    elif guess<number:
        print(name + ", your guess was too low. Hint: The number is higher than ",guess)
    else:
        print(name + ", your guess was too high. Hint: The number is lower than ",guess)
    

if not chance<5:
    print( "Oh no! You lose. The number was ", number )