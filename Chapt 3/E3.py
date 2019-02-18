import random

die1 = random.randint(1,6)
die2 = random.randint(1,6)

print("Die 1:", die1, "Die 2:", die2)

if die1 == die2:
    print("You threw double. Your score:", (die1+die2)*2)
else:
    print("Your score:", die1 + die2)