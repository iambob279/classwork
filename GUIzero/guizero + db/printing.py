#Program name: Ch 11 Exercise 1 Print tblFilms.py
#program prints all records in  tblfilms in database MyFilms.db with a label

import sqlite3

conn = sqlite3.connect("MyFilms.db")
cursor = conn.cursor()
for row in cursor.execute('SELECT filmID, title, yearReleased, rating, duration, genre FROM tblFilms'):
   print ("Id= {}, title = {}, year released = {}, rating = {}, duration = {}, genre = {}" .format(row[0], row[1], row[2], row[3], row[4], row[5]))

conn.close()