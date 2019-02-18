num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second nubmer: "))
numOfPlace = int(input("Enter the number of decimal places: "))

numsum = round(num1 + num2, numOfPlace)
product = round(num1 * num2, numOfPlace)

print("The sum of", num1, "and", num2, "is", numsum)
print("The product of", num1, "and", num2, "is", product)