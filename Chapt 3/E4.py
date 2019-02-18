goodCost = float(input("Enter value of good: "))

if goodCost > 200:
    discount = round(goodCost * .1,2)
elif goodCost > 100:
    discount = round(goodCost * .05,2)
else:
    discount = 0

print("Value of good ${0:.2f}\tDiscount ${1:.2f}\tAmount owing ${2:.2f}".format(goodCost,discount,goodCost-discount))
