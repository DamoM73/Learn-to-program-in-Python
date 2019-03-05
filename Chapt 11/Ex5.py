import sqlite3

conn = sqlite3.connect("./Chapt 11/CityTemperatures.db")
cursor = conn.cursor()

# print headings
print("%-15s%20s%20s" %("City","Temperature","Local time"))
for row in cursor.execute('SELECT * FROM tblTemps ORDER BY temperature DESC LIMIT 5'):
    city, temperature, location = row
    print("%-15s%20s%20s" %(city, temperature, location)) 