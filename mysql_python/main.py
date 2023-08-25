import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="mydb")
    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print("Connection error:", err)

def insert_values(table, columns, values):
    try:
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, columns, values)
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Insertion error:", err)

def query(query):
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

with mydb as connection:
    insert_values("asignatura", "idAsignatura, Notas_idNotas, Notas_Notas_idNotas", "01001, 02323, 12312")
    query("SELECT * FROM asignatura")