
num = 5
i = 3
while i>0:
    guess = int(input("Guess a number between 1-10: "))
    if guess == num:
        print('You found it!')
        break
    i=i-1
else:
    print('Sorry you failed! The number was: ',num)


