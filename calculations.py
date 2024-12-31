import sqlite3 as sq
import os
from salaries import clear

def checking(db_name):
    way = os.path.join("..//mini_project//databases//"+db_name)
    db = sq.connect(way)
    cursor = db.cursor()
    cursor.execute("SELECT CUSTOMER_NUMBER FROM DEBTORS WHERE NON_PAYMENT_PER >= 3")
    all_ = cursor.fetchall()
    for i in all_:
        print(i)

# checking("projects.db")


