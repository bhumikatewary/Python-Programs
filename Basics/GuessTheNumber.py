secretNumber = 9;
count = 0
limit = 3
while count<limit:
    guessedNumber = int(input("Enter your guess: "))
    count=count+1
    if guessedNumber == secretNumber:
        print("You won!")
        break
else:
    print("You lost!")
