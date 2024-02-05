# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import mysql.connector

kuydb = mysql.connector.connect( 
    host = "127.0.0.1",
    user = "root",
    passwd = "123",
    )

mycursor = kuydb.cursor()
mycursor.execute("CREATE DATABASE klux")

mycursor.execute("SHOW DATABASES")
 
print(mycursor)
for db in mycursor:
    print(db[0])