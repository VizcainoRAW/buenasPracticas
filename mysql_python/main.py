import mysql.connector

def insertValues(table:str, columns:str, values:str):
    mycursor.execute("INSERT INTO "+table+"("+columns+") VALUES("+values+")")

def querry(query:str):
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb")
    mycursor = mydb.cursor()
except:
    print("connection error")

insertValues("asignatura","idAsignatura,Notas_idNotas,Notas_Notas_idNotas","01001,02323,12312")
querry("SELECT * FROM asignatura")

mydb.close()
