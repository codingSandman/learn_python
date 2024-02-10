from random import randint
import time

start = time.time()    
number = randint(1,100)

quess = int(input("quess a number between 1 and 100: "))
count = 1

while quess != number:
    if quess < number:
        print("Your number is too small.")
    elif quess > number:
        print("Die number is too big.")
    else:
        print("Strike!!")
        
    quess = int(input("quess a number between 1 and 100: "))
    count += 1

ende = time.time()
dauer = ende - start
    
print (f"You needed {count} tries. ")
print("The task was done in {:.2f} secounds.".format(dauer))