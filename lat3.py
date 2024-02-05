# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 20:41:35 2023

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
masukinData = "INSERT INTO users (nama, email, age) VALUES (%s, %s, %s)"
masukinNama = ("patrick", "patrickkun@gmail.com", 22)

mycursor.execute(masukinData, masukinNama)
kuydb.commit()