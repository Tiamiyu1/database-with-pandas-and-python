# Import Library

import psycopg2
from psycopg2 import Error

# Create Connection
def getConnection():
    connection = psycopg2.connect(
    host= 'localhost', password='Ti@miyu1', user='postgres', database='postgres')
    return connection   
    print('Database connected')

# close connection
def closeConnection(connection):
    connection.close()
    print('Connection closed')

#  Read customer records 
def getCustomer(customer_id):
    try:
        connection = getConnection()

        #create a cursor object
        cursor = connection.cursor()

        query = 'Select * from customer where customer_id = %s'


        # Execute query
        cursor.execute(query,(customer_id,))
        records = cursor.fetchall()

        print('Printing Records')

        for row in records:
            print('Customer_id:', row[0])
            print('Store id:', row[1])
            print('First name:', row[2])
            print('Last name:', row[3])
            print('Email:', row[4])
            print('Address id:', row[5])
            print('Active bool:', row[6])
            print('Date created:', row[7])
            print('Last update:', row[8])
            print('Active:', row[9], '\n')

        closeConnection(connection)
    except Error as e:
        print("Error: Reading Record")
    
# Using the getCustomer function, print out the customer information for customer_id = 34
getCustomer(34)

        