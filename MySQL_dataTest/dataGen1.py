import mysql.connector
mydb = mysql.connector.connect(
  #CONFIG
  host="***",
  user="***",
  password="***",
  database="***"
)

mycursor = mydb.cursor()
sql = "INSERT INTO my_table (TEMPERATURE, SMOKE, SOUNDLVL) VALUES (%s, %s, %s)"


#test values
temp = random.randint(-40, 40)
smoke = bool(random.randint(0, 1))
sound = random.randint(0, 60)


val = (temp, smoke, sound)

mycursor.execute(sql, val)

mydb.commit()

mydb.close()
