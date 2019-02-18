import time

parkingHours = int(input("Enter number of hours for parking: "))

if parkingHours < 2:
    cost = 3.5
elif parkingHours < 4:
    cost = 5.0
else:
    cost = 10.0

currentTime = time.time()
expirationTime = currentTime + parkingHours * 3600

print("Time now:\t", time.ctime(currentTime))
print("Expires:\t", time.ctime(expirationTime))
print("Charge = ${0:.2f}".format(cost))