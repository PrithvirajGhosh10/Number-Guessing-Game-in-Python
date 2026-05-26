import random #to generate a random no.
n= random.randint(1,100) #guess a no. from 1 to 100
a=0
guesses = 0
while(a != n): #game loop
    guesses+=1
    a=int(input("Guess the number: "))
    if(a > n):
        print("Lower number please")
    elif(a < n):
        print("Higher number please")
print(f"You have guessed the number {n} correctly in {guesses} attempts")
