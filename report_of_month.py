from salaries import connector
import json
import os
from salaries import first_project, clear

def num_of_persons(db_name):
    _, cursor = connector(db_name)
    cursor.execute("SELECT PERFORMER_NUMBER FROM PAYROLL")
    all_performers = cursor.fetchall()
    for i in all_performers:
        i = clear(i)
        i = int(i)
    return i

def rep_of_month(db_name, project_num):
    try:
        _, cursor = connector(db_name)
        num_of_per = num_of_persons(db_name)
        count_of_reports, proj_num = first_project(db_name, num_of_per)
        if count_of_reports <= 31:
            cursor.execute("SELECT * FROM REPORT WHERE PROJECT_NUM = ?", (project_num, ))
            data = cursor.fetchall()
            way = os.path.join("../mini_project/reports/report_of_mon.json")
            with open(way, "w") as file:
                json.dump(data, file, indent=4)
            return f"Report successfully added!"
    except Exception as e:
        return f"Error: {e}"
# rep_of_month("projects.db", 1)