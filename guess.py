import random

number = random.randint(1,100)
print("I'm thinking of a number 1 through 100")
guessed=False
temp=0
guessesTaken=0
while not guessed:
    t=input()
    t=int(t)
    if t!=temp:
        guessesTaken=guessesTaken+1
    temp=t
    if t>number:
        print("Guess lower")
    if t<number:
        print("Guess higher")
    if t==number:
        guessed=True
        guessesTaken=str(guessesTaken)
        print("You guessed my number in "+guessesTaken+" guesses.")
        





















