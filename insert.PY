import sqlite3
import csv

conn = sqlite3.connect('phonepe.db')
cursor = conn.cursor()

with open('data/map_user.csv','r') as file:
    no_record = 0 
    for row in file:
        cursor.execute("INSERT INTO map_user VALUES (?, ?, ?, ?, ?)", row.split(","))
        conn.commit()
        no_record +=1
conn.close()
print('/n{} Record Transferre'.format(no_record))

