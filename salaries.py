import sqlite3 as sq
import json
import os
import re
# from calculations import first_project

def clear(position):
    for i in position:
        s = str(i)
        clean_string = re.sub(r"[(),'']", "", s)
        position = clean_string
        return position

def connector(db_name):
    way = os.path.join("..//mini_project//databases//"+db_name)
    db = sq.connect(way)
    cursor = db.cursor()
    return db, cursor

def first_project(db_name, num_of_pr):
    _, cursor = connector(db_name)
    cursor.execute("SELECT PROJECT_NUM, COUNT(PROJECT_NUM) FROM REPORT WHERE PERSON_NUMBER = (?) ORDER BY PERSON_NUMBER DESC LIMIT 1", (num_of_pr, ))
    last_proj = cursor.fetchall()
    last_proj = clear(last_proj)
    # print(last_proj)
    if last_proj == "None 0" or last_proj == "[]":
        count_of_reports = 0
        proj_num = 0
    else:
        count_of_reports = ""

        proj_num = last_proj[0]
        for i in last_proj[2:4]:
            count_of_reports+=i

        count_of_reports = int(count_of_reports)
        proj_num = int(proj_num)
    return count_of_reports, proj_num

# c, p = first_project("projects.db", 3007)
# print(c, p)

def find_coef(db_name, num_of_per):
    _, cursor = connector(db_name)
    try:
        _, proj_num = first_project(db_name, num_of_per)
        cursor.execute("SELECT ALLOWANCE_COEFFICIENT FROM COEFFICIENTS WHERE DIFFICULTY_NUMBER = (SELECT DIFFICULTY_NUMBER FROM PROJECTS WHERE NUMBER_OF_PROJECT = (?))", (proj_num, ))
        data = cursor.fetchall()
        data = clear(data)
        # cursor.execute("SELECT PROJECT_NUM FROM REPORT WHERE PERSON_NUMBER = (?) ORDER BY PERSON_NUMBER DESC LIMIT 1", (num_of_per, ))
        # project_nums = cursor.fetchall()
        # project_nums = clear(project_nums)
        # project_nums = int(project_nums)
        # print(project_nums)
        # cursor.execute("SELECT PRICE FROM PROJECTS_IN_PROGRESS WHERE PERFORMER_NUMBER LIKE ? OR NUMBER_OF_PROJECT = ?", (f"%{num_of_per}%", project_nums, ))

        # price = cursor.fetchall()
        # price = clear(price)
        # price = int(price)

        if data == None:
            data = 0

        if data == []:
            data = 0

        # if price == None:
        #     price = 0

        # if price == []:
        #     price = 0
        
        # cursor.execute("SELECT PERFORMER_NUMBER FROM PROJECTS_IN_PROGRESS WHERE NUMBER_OF_PROJECT = (?)", (project_nums, ))
        # counter = cursor.fetchall()
        # counter = clear(counter)
        # counter = counter.split()
        # counter = len(counter)
        # price /= counter
        # print(price, counter)

        return float(data)
    # , float(price)

    except Exception as e:
        return f"Error: {e}"

# data, price = find_coef("projects.db", 3005)
# print(data, price)

def find_position(db_name, num_of_per):
    _, cursor = connector(db_name)
    try:
        cursor.execute("SELECT POST, SKILL_LEVEL FROM ABOUT_COMPANY WHERE PERFORMER_NUMBER = (?)", (num_of_per, ))
        position = cursor.fetchall()

        position = clear(position)
        cursor.execute("SELECT HOURLY_RATE_PAYMENT, ALLOWANCE_RATIO FROM PAYMENT WHERE POST = (?)", (position, ))
        # print(position)
        h_a_r = cursor.fetchall()
        # print(h_a_r)
        if h_a_r == None:
            h_a_r = 0
        if h_a_r == []:
            h_a_r = 0
        
        if isinstance(h_a_r, list):
            h_a_r = clear(h_a_r)
            h_a_r = re.search(r'(\S+)\s+(.*)', h_a_r)
            hourly_rate = h_a_r[1]
            allowance_ratio = h_a_r[2]
        else:
            hourly_rate = 0
            allowance_ratio = 0

        return float(hourly_rate), float(allowance_ratio)
    except Exception as e:
        return f"Error: {e}", 0

# h, a = find_position("projects.db", 3005)
# print(h,a)

# find_position("projects.db", 3001)

def select_hours(db_name, num_of_per):
    _, cursor = connector(db_name)
    try:
        cursor.execute("SELECT HOURS FROM REPORT WHERE PERSON_NUMBER  = (?)", (num_of_per, ))
        hours = cursor.fetchall()
        if hours == None:
            hours = []
            hours = 0
        if hours == []:
            hours = 0
        new_str = 0
        if isinstance(hours, list):
            for i in hours:
                i = clear(i)
                new_str+=float(i)
        return float(new_str)
    except Exception as e:
        return f"Error: {e}"

# hour = select_hours("projects.db", 3001)
# print(hour)

def salaries(allowance_coeficient, hourly_rate_payment, allowance_ratio, hours):
    try:
        salary = (float(allowance_coeficient)*((float(hourly_rate_payment)+allowance_ratio)*hours))
        return salary
    except Exception as e:
        return(f"Error: {e}")

# resp = salaries(data, h, a, hour, price)
# print(data, h, a, hour, price)


def wage(db_name, salary, num_of_per):
    db, cursor = connector(db_name)
    cursor.execute("UPDATE PAYROLL SET WAGE = (?) WHERE PERFORMER_NUMBER = (?)", (salary, num_of_per))
    db.commit()

def report(db_name, date):

    try:
        _, cursor = connector(db_name)
        cursor.execute("SELECT * FROM PAYROLL")
        data = cursor.fetchall()
        data_with_date = [row + (date,) for row in data]
        report_dir = os.path.join("..", "mini_project", "reports")
        if not os.path.exists(report_dir):
            os.mkdir(report_dir)
        report_file = os.path.join(report_dir, "report.json")
        with open(report_file, "w") as file:
            json.dump(data_with_date, file, indent=4)
        return f'Report successfully added if reports folder!'
    except Exception as e:
        return f"Error: {e}"


def report_(db_name, num_of_per, date):
    try:
        count_of_reports, proj_num = first_project(db_name, num_of_per)
        if count_of_reports >= 15:
            coef = find_coef(db_name, num_of_per)
            hour, ratio = find_position(db_name, num_of_per)
            # print(hour)
            hours = select_hours(db_name, num_of_per)
            salary = salaries(coef, hour, ratio, hours)
            wage(db_name, salary, num_of_per)
            response = report(db_name, date)
            #     print(f"coef, price = {coef}, {price}\nhour, ratio = {hour}, {ratio}\nhours = {hours}\nsalary = {salary}\
            # \nwage = {wage}")
            return response
        
        else:
            return f"Worker with id {num_of_per} do not have 30 reports:", f"{count_of_reports}"
    except Exception as e:
        return f"Error: {e}"
    
# --------------- Use this function -----------------
def deleter(db_name, num_of_per):
        db, cursor = connector(db_name)
        cursor.execute("DELETE FROM REPORT WHERE PERSON_NUMBER = (?)", (num_of_per, ))
        db.commit()
    
def num_of_persons(db_name, date):
    try:
        _, cursor = connector(db_name)
        cursor.execute("SELECT PERFORMER_NUMBER FROM PAYROLL")
        all_performers = cursor.fetchall()
        for i in all_performers:
            i = clear(i)
            i = int(i)
            response = report_(db_name, i, date)
            deleter(db_name, i)
        return response
    except Exception as e:
        return f"Error: {e}"
    
# ----------------------------------------------------
# response = num_of_persons("projects.db", "02.02.2025")
# print(response)