import random
import os
# import sqlite3 as sq
from salaries import clear, connector

def experemental_datas(db_name, random_person, all_person_or_not, project_num):
    db, cursor = connector(db_name)
    changes = "changes"

    if all_person_or_not == 0:

        for i in range(15):
            # -------------------
            cursor.execute("SELECT REPORT_NUMBER FROM REPORT ORDER BY REPORT_NUMBER DESC LIMIT 1")
            num_of_rep = cursor.fetchall()
            num_of_rep = clear(num_of_rep)

            if num_of_rep is None:
                rep_num = 1
            else:
                rep_num = int(num_of_rep)+1

            # ------------------
            hours = random.randint(0, 10)
            cursor.execute("INSERT INTO REPORT(REPORT_NUMBER, PROJECT_NUM, CHANGES, HOURS, PERSON_NUMBER) \
            VALUES(?, ?, ?, ?, ?)", (rep_num, project_num, changes, hours, random_person, ))
            db.commit()
    else:
        for i in range(1, 30):
            if i < 10:
                random_person = "300"+str(i)
            else:
                random_person = "30"+str(i)
            for _ in range(15):
                # -------------------
                cursor.execute("SELECT REPORT_NUMBER FROM REPORT ORDER BY REPORT_NUMBER DESC LIMIT 1")
                num_of_rep = cursor.fetchall()
                num_of_rep = clear(num_of_rep)

                if num_of_rep is None:
                    rep_num = 1
                else:
                    rep_num = int(num_of_rep)+1

                # ------------------
                hours = random.randint(0, 10)
                cursor.execute("INSERT INTO REPORT(REPORT_NUMBER, PROJECT_NUM, CHANGES, HOURS, PERSON_NUMBER) VALUES(?, ?, ?, ?, ?)", (rep_num, project_num, changes, hours, random_person))
                db.commit()

db_name = input("Enter database with .db: ")
random_person = input("Enter person (if you want all persons, press some key and enter): ")
all_persons_or_not = input("All persons(1) or not(0): ")
project_num = input("Enter project number: ")
experemental_datas(db_name, random_person, int(all_persons_or_not), int(project_num))
print("Datas added successfully!")