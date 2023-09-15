import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="tasksDB")
    mycursor = mydb.cursor()
except mysql.connector.Error as err:
    print("Connection error:", err)

def insert_values(table, columns, values):
    try:
        print("guardando")
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, columns, values)
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Insertion error:", err)

def querry(querry:str):
    mycursor.execute(querry)
    data = mycursor.fetchall()
    return data
    
def get_all_table(table:str):
    return querry("SELECT * FROM "+table)





