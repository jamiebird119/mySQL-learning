import os
import pymysql

# Get username
username = os.getenv('C9_USER')


# Connect to database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = 'SELECT * from Artist'
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    connection.close()
