from opcua import Server
from random import randint
from datetime import datetime
import time
import json
import requests


def kodPogody(w):
    n = [0,1,2,3,45,48,51,53,55,56,57,61,63,65,66,67,71,73,75,77,80,81,82,85,86,95,96,99]
    p = ["Bezchmurne niebo","Prawie bezchmurne niebo","Częsciowe zachmurzenie","Zachmurzone niebo","Mgła","Osadzanie się mgły szronowej","Lekka mżawka","Średnia mżawka","Silna Mżawka","Marznąca mżawka","Silna marznąca mżawka",\
        "Lekki deszcz","Średni deszcz","Silny descz","Zamarzający deszcz","Silny zamarzający deszcz","Lekki opad śniegu","Średni opad śniegu",\
        "Mocny opad śniegu","Grad","Lekka ulewa","Średnia ulewa","Silna ulewa","Lekka śnieżyca","Śnieżyca","Burza","Burza z lekkim gradem","Burza z silnym gradem"]
    for i in range(len(n)):
        if int(w) == int(n[i]):
            return(p[i])
    else:
        return "błąd kodu pogodowego"



server=Server()

url="opc.tcp://192.168.1.10:4840"
server.set_endpoint(url)

name= "SERVER_OPCUA"
addspace=server.register_namespace(name)

node=server.get_objects_node()

Param=node.add_object(addspace,"Parametry")

Temp = Param.add_variable(addspace,"Temperatura", 0)
Rad= Param.add_variable(addspace,"Promieniowanie", 0)
Czas= Param.add_variable(addspace,"Czas",0)
Zach= Param.add_variable(addspace,"Zachmurzenie",0)
Rain= Param.add_variable(addspace,"Opady",0)
w_code= Param.add_variable(addspace,"Stan",0)

Temp.set_writable()
Rad.set_writable()
Czas.set_writable()
Zach.set_writable()
Rain.set_writable()
w_code.set_writable()

server.start()
print("Server started at {}",format(url))

while True:

    r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=50.30&longitude=18.68&hourly=temperature_2m,diffuse_radiation,cloudcover,rain,weathercode')
    o = r.json()
    a=[]
    now = datetime.now()
    dt_string = now.strftime("%Y-%m-%d"+"T"+"%H:00")

    for value in o["hourly"]["time"]:
        if value == dt_string:
            czas = value
            index = o["hourly"]["time"].index(value)

    tempp = o["hourly"]["temperature_2m"][index]
    radd = o["hourly"]["diffuse_radiation"][index]
    cloud = o["hourly"]["cloudcover"][index]
    rainn = o["hourly"]["rain"][index]
    w_codee = kodPogody(o["hourly"]["weathercode"][index])

    print("\n")
    print("Data i czas: ",czas)
    print("Temperatura: ",tempp)
    print("Radiacja rozproszona: ",radd)
    print("Zachmurzenie totalne [%]: ",cloud)
    print("Opady [mm/h]: ",rainn)
    print("Kod pogodowy: ",w_codee)




    
    TIME=datetime.datetime.now()
    

    Temp.set_value(tempp)
    Rad.set_value(radd)
    Czas.set_value(TIME)
    Zach.set_value(cloud)
    Rain.set_value(rainn)
    w_code.set_value(w_codee)

    time.sleep(5)