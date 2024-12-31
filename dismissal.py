import sqlite3 as sq
import os
from salaries import connector
import re

def clear1(position):
    array = []
    for i in position:
        s = str(i)
        clean_string = re.sub(r"[(),'']", "", s)
        array.append(clean_string)
    return array

def dismissal_person(db_name, per_num, new_per_num):
    try:
        db, cursor = connector(db_name)
        cursor.execute("SELECT POST, SKILL_LEVEL FROM ABOUT_COMPANY WHERE PERFORMER_NUMBER = (?)", (per_num, ))
        post = cursor.fetchall()
        post = clear1(post)
        for i in post:
            post = str(i)
        print(post)
        cursor.execute("DELETE FROM ABOUT_COMPANY WHERE PERFORMER_NUMBER = (?)",(per_num, ))
        cursor.execute("DELETE FROM PAYROLL WHERE PERFORMER_NUMBER = (?)", (str(per_num), ))
        cursor.execute("UPDATE PROJECTS_IN_PROGRESS SET PERFORMER_NUMBER = TRIM(REPLACE(REPLACE(PERFORMER_NUMBER, ?, ''), ?, '')) WHERE PERFORMER_NUMBER LIKE ?;",(f",{per_num}", f"{per_num},", f"%{per_num}%"))
        db.commit()
        diss = "dismissal"
        cursor.execute("INSERT INTO HISTORY (PERFORMER_NUMBER, POSITION, STATUS) VALUES(?, ?, ?)", (per_num, post, diss))
        db.commit()

        cursor.execute("SELECT PROJECT_MANAGER_NUM FROM PROJECTS")
        p_m_numbers = cursor.fetchall()
        array = []
        array = clear1(p_m_numbers)
        # print(p_m_numbers)
        for i in array:
            if per_num == i:
                cursor.execute("UPDATE PROJECTS SET PROJECT_MANAGER_NUM = REPLACE(PROJECT_MANAGER_NUM, (?), (?)) WHERE PROJECT_MANAGER_NUM LIKE (?)", (per_num, new_per_num, per_num))
                db.commit()
                # print("excelent")

        print("Person will be dismissal.")
        return f"Person will be dismissal."
    except Exception as e:
        print(f"Error: {e}")
        return f"Error: {e}"

def start_diss():
    db_name = input("Enter database with .db: ")
    person = input("Enter person number: ")
    new_person = input("Enter ew person for project_manager(if you want  delete project manager)")
    dismissal_person(db_name, person, new_person)
    print("Datas added!")
    return f"Datas added!"