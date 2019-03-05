tempsFile = open("./Chapt 9/temperatures.txt","a")
print("This program writes temprature data to \n temperatures.txt")
print("If the file does not exist, it will be created")
city = input("Enter city name, xxx to end: ")

while city != "xxx":
    temperature = input("Enter termperature: ")
    localTime = input("Enter local time: ")
    tempsFile.write(city + "," + temperature + "," + localTime + "," + "\n")
    city = input("Enter city name, xxx to end: ")

tempsFile.close()