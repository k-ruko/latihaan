# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:24:25 2023

@author: ASUS
"""

import mysql.connector

kuydb = mysql.connector.connect( 
    host = "127.0.0.1",
    user = "root",
    passwd = "123",
    database = "klux"
    )

mycursor = kuydb.cursor()

mycursor.execute("CREATE TABLE users (nama VARCHAR(255), email VARCHAR(255), age INTEGER(10), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
mycursor.execute("SHOW TABLES")

for table in mycursor:
    print(table[0])