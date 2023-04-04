import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="franek123",
  database="room_climate"
)

mycursor = mydb.cursor()
sql = "INSERT INTO my_table (TEMPERATURE, SMOKE, SOUNDLVL) VALUES (%s, %s, %s)"





val = (10, True, 11)

mycursor.execute(sql, val)

mydb.commit()

mydb.close()
