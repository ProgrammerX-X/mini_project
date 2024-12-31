import os
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from salaries import connector
from dismissal import clear1
from salaries import clear

def transform_in_date(date):
    old_date = date.split('.')
    day = old_date[0]
    mounth_new = old_date[1]
    year = old_date[2]
    return int(day), int(mounth_new), int(year)

def report_for_dept(db_name, date):
    db, cursor = connector(db_name)
    cursor.execute("SELECT CUSTOMER_NUMBER FROM DEBTORS")
    datas = cursor.fetchall()
    if datas == None:
        datas = 0
    datas = clear1(datas)
    
    all_reports = []
    try:
        for i in datas:
            customer = int(i)
            
            cursor.execute("SELECT DURATION_OF_EXECUTION FROM PROJECTS WHERE NUM_OF_CUSTOMER = (?)", (customer,))
            months1 = cursor.fetchall()
            months1 = clear(months1)
            months1 = int(months1)
            
            day, my_mounth, year = transform_in_date(date)
            old_date = datetime(year, my_mounth, day)
            new_date = old_date + relativedelta(months=months1)

            cursor.execute("SELECT NUMBER_OF_PROJECT FROM PROJECTS WHERE NUM_OF_CUSTOMER = (?)", (customer,))
            number_of_project = cursor.fetchall()
            number_of_project = clear(number_of_project)
            
            cursor.execute("SELECT PRICE FROM PROJECTS_IN_PROGRESS WHERE NUMBER_OF_PROJECT = (?)", (number_of_project,))
            price = cursor.fetchall()
            price = clear(price)
            price = float(price)

            cursor.execute("SELECT CHARGE FROM CUSTOMERS WHERE CUSTOMERS_NUMBER = (?)", (customer,))
            charges = cursor.fetchall()
            charges = clear(charges)
            charges = float(charges)

            cursor.execute("SELECT PERFORMER_NUMBER FROM PROJECTS_IN_PROGRESS WHERE NUMBER_OF_PROJECT = (?)", (number_of_project,))
            performers = cursor.fetchall()
            data_performers = clear(performers)
            performers = data_performers.split(" ")
            
            wages = 0
            for j in performers:
                cursor.execute("SELECT WAGE FROM PAYROLL WHERE PERFORMER_NUMBER = (?)", (j,))
                wage = cursor.fetchall()
                wage = clear(wage)
                wage = float(wage)
                wages += wage

            wages += price - charges
            print(wages)

            absolutely_date = new_date + relativedelta(months=1)

            new_date_str = new_date.strftime("%d-%m-%Y")
            absolutely_date_str = absolutely_date.strftime("%d-%m-%Y")

            data_ex1 = {"customer": customer, "begin_month": new_date_str, "debt": price}
            data_ex2 = {"charge": charges}
            data_ex3 = {"customer": customer, "before_month": absolutely_date_str, "absolutely_debt": wages}
            
            all_reports.append([data_ex1, data_ex2, data_ex3])

        report_dir = os.path.join("..", "mini_project", "reports")
        if not os.path.exists(report_dir):
            os.mkdir(report_dir)

        report_file = os.path.join(report_dir, "report_for_debtors.json")

        with open(report_file, "w") as file:
            json.dump(all_reports, file, indent=4)

        return f"Report successfully created in {report_file}!"
    except Exception as e:
        return f"Error: {e}"

# report_for_dept("projects.db", "01.01.2025")
