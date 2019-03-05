import sqlite3

conn = sqlite3.connect("./Chapt 11/CityTemperatures.db")
cursor = conn.cursor()
for row in cursor.execute('SELECT * FROM tblTemps ORDER BY temperature DESC'):
    print(row)
