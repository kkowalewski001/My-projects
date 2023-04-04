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
val = (10, True, 11)

mycursor.execute(sql, val)

mydb.commit()

mydb.close()
