# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 21:43:26 2023

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
masukinNama = [
    ("patrick", "patrickkun@gmail.com", 22),
    ("lalu", "lalu@gmail.com", 21),
    ("kuka", "kakiku@gmail.com", 18),
    ]

mycursor.executemany(masukinData, masukinNama)
kuydb.commit()