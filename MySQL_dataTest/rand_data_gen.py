import mysql.connector
import random

mydb = mysql.connector.connect(
  host="",
  user="",
  password="",
  database=""
)

mycursor = mydb.cursor()
sql = "INSERT INTO my_table (TEMPERATURE, SMOKE, SOUNDLVL) VALUES (%s, %s, %s)"


temp = random.randint(-40, 40)
smoke = bool(random.randint(0, 1))
sound = random.randint(0, 60)


val = (temp, smoke, sound)

mycursor.execute(sql, val)

mydb.commit()

mydb.close()
