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
        placeholders = ', '.join(['%s'] * len(values))
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, columns, placeholders)
        mycursor.execute(sql,values)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Insertion error:", err)

def delete_recordById(table,id):
    try:
        sql = "DELETE FROM {} WHERE id=({})".format(table,id)
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.Error as err:
        print("Insertion error:", err)

def update_recordById(table, id, columns, values):
        try:
            sql = "UPDATE {} SET {} WHERE id={}".format(table, columns, id)
            mycursor.execute(sql,values)
            print(sql,values)
            mydb.commit()
        except mysql.connector.Error as err:
            print("Insertion error:", err)

def querry(querry:str):
    mycursor.execute(querry)
    data = mycursor.fetchall()
    return data
    
def get_all_table(table:str):
    return querry("SELECT * FROM "+table)




