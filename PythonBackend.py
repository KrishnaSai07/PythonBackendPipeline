from flask.json import jsonify
import mysql.connector
from mysql.connector import Error
from Models import Orders,FoodItems


def getPendingOrders():
    records = []
    try:
        connection = mysql.connector.connect(host='footballmadesimple.c18ndxpocyny.us-east-2.rds.amazonaws.com',port='3306',database='foodcourt',user='admin',password='JethroGibbs')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MYSQL Server version", db_Info)
            cursor = connection.cursor()
            cursor.execute("SELECT orderNumber as orderNumber,customerName as customerName,orderData as orderData,totalPrice as totalPrice,orderStatus as orderStatus FROM orders where orderStatus='PEND'")
            records = cursor.fetchall()
            

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return jsonify(records)        


def getFoodItemsOfCertainCategory(itemCategory):
    records = []
    try:
        connection = mysql.connector.connect(host='footballmadesimple.c18ndxpocyny.us-east-2.rds.amazonaws.com',port='3306',database='foodcourt',user='admin',password='JethroGibbs')

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MYSQL Server version", db_Info)
            cursor = connection.cursor()
            query = "SELECT itemId as itemId, itemName as itemName, price as price, itemCategory as itemCategory FROM fooditems WHERE itemCategory='"+itemCategory+"'"
            cursor.execute(query)
            records = cursor.fetchall()
            

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    return jsonify(records)

