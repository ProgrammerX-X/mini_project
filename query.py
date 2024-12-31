import sqlite3 as sq
import os
from salaries import clear, connector

def add_into_project(db_name, name, num_of_cus, proj_men_num, dur_of_ex, dif_cat, beg_date):
    db, cursor = connector(db_name)

    cursor.execute("SELECT NUMBER_OF_PROJECT FROM PROJECTS ORDER BY NUMBER_OF_PROJECT DESC LIMIT 1")
    pr_num = cursor.fetchall()
    pr_num = clear(pr_num)

    if pr_num is None:
        project_number = 1
    else:
        project_number = int(pr_num)+1

    try:
        cursor.execute("SELECT NON_PAYING_TERM FROM CUSTOMERS WHERE CUSTOMERS_NUMBER = (?)", (num_of_cus, ))
        debtors_or_not = cursor.fetchall()
        debtors_or_not = clear(debtors_or_not)
        debtors_or_not = int(debtors_or_not)

        if debtors_or_not <=3:
            cursor.execute("INSERT INTO PROJECTS (NUMBER_OF_PROJECT, NAME, NUM_OF_CUSTOMER, PROJECT_MANAGER_NUM, \
            DURATION_OF_EXECUTION, DIFFICULTY_CATEGORY, BEGIN_DATE) VALUES(?, ?, ?, ?, ?, ?, ?)", (project_number, name, num_of_cus, \
            proj_men_num, dur_of_ex, dif_cat, beg_date, ))
            db.commit()
            
            return f"Insert into *projects* successfull."
        else:
            return f"This customer has unpaying accounts, you can`t add it in projects."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

# add_into_project("projects.db", 2, "some", 2, 3, 3, 3, "01.01.2025")

def add_into_about_company(db_name, per_num, f_l_p, post, skill_level):
    db, cursor = connector(db_name)

    hiring = "accepted"
    try:
        cursor.execute("INSERT INTO ABOUT_COMPANY (PERFORMER_NUMBER, F_L_P, POST, SKILL_LEVEL) VALUES(?, ?, ?, ?)", (per_num, f_l_p, post, skill_level, ))
        cursor.execute("INSERT INTO HISTORY (PERFORMER_NUMBER, POSITION, STATUS) VALUES(?, ?, ?)", (per_num, post+" "+skill_level, hiring))
        db.commit()
        
        return f"Insert into *about company* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

def add_into_projects_in_progress(db_name, num_of_pr, per_num1, price):
    db, cursor = connector(db_name)
    try:
        cursor.execute("INSERT INTO PROJECTS_IN_PROGRESS (NUMBER_OF_PROJECT, PERFORMER_NUMBER, PRICE) VALUES(?, ?, ?)", (num_of_pr, per_num1, price, ))
        db.commit()
        
        return f"Insert into *projects in progress* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

def add_into_coefficients(db_name, dif_num, proj_dif, al_coef):
    db, cursor = connector(db_name)
    try:
        cursor.execute("INSERT INTO COEFFICIENTS (DIFFICULTY_NUMBER, PROJECTS_DIFFICULTY, ALLOWANCE_COEFFICIENT) \
        VALUES (?, ?, ?)", (dif_num, proj_dif, al_coef, ))
        db.commit()
        
        return f"Insert into *coefficients* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e


def add_into_customers(db_name, cus_num, customer, n_n_t):
    db, cursor = connector(db_name)
    try:
        if int(n_n_t) <= 1:
            cursor.execute("INSERT INTO CUSTOMERS (CUSTOMERS_NUMBER, CUSTOMER_NAME, NON_PAYING_TERM) VALUES(?, ?, ?)", (cus_num, customer, n_n_t))
            db.commit()
        else:
            cursor.execute("INSERT INTO CUSTOMERS (CUSTOMERS_NUMBER, CUSTOMER_NAME, NON_PAYING_TERM) VALUES(?, ?, ?)", (cus_num, customer, n_n_t))
            db.commit()
            cursor.execute("SELECT NUMBER_OF_DEBTORS FROM DEBTORS ORDER BY NUMBER_OF_DEBTORS DESC LIMIT 1")
            num_of_deb = cursor.fetchall()
            num_of_deb = clear(num_of_deb)

            if num_of_deb is None:
                deb_num = 1
            else:
                deb_num = int(num_of_deb)+1
            cursor.execute("INSERT INTO DEBTORS (NUMBER_OF_DEBTORS, CUSTOMER_NUMBER, NON_PAYMENT_PER) VALUES(?, ?, ?)", (deb_num, cus_num, n_n_t))
            db.commit()
        return f"Insert into *customers* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e


def add_into_payroll(db_name, per_num2, bank_num):
    db, cursor = connector(db_name)
    try:
        cursor.execute("INSERT INTO PAYROLL (PERFORMER_NUMBER, BANK_ACCOUNT_NUMBER) VALUES (?, ?)", (per_num2, bank_num, ))
        db.commit()
        
        return f"Insert into *payroll* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

# ALL WAGES

def add_into_debtors(db_name, cuss_num, am_of_deb, n_p_p):
    db, cursor = connector(db_name)

    cursor.execute("SELECT NUMBER_OF_DEBTORS FROM DEBTORS ORDER BY NUMBER_OF_DEBTORS DESC LIMIT 1")
    num_of_deb = cursor.fetchall()
    num_of_deb = clear(num_of_deb)

    if num_of_deb is None:
        deb_num = 1
    else:
        deb_num = int(num_of_deb)+1

    try:
        cursor.execute("INSERT INTO DEBTORS (NUMBER_OF_DEBTORS, CUSTOMER_NUMBER, AMOUNT_OF_DEBT, NON_PAYMENT_PER) VALUES (\
        ?, ?, ?, ?)", (deb_num, cuss_num, am_of_deb, n_p_p))
        db.commit()
        
        return f"Insert into *debtors* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

def add_into_payment(db_name, post, h_r_p, all_r):
    db, cursor = connector(db_name)
    try:
        cursor.execute("INSERT INTO PAYMENT (POST, HOURLY_RATE_PAYMENT, ALLOWANCE_RATIO) VALUES (?, ?, ?)", (post, h_r_p, all_r, ))
        db.commit()
        
        return f"Insert into *payment* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

# response = add_into_payment("projects.db", "Product Manager Junior", 8.1, 14.5)
# print(str(response))

def add_into_report(db_name, project_num, changes, hours, per_num):
    db, cursor = connector(db_name)
    cursor.execute("SELECT REPORT_NUMBER FROM REPORT ORDER BY REPORT_NUMBER DESC LIMIT 1")
    rep_num = cursor.fetchall()
    rep_num = clear(rep_num)

    if rep_num is None:
        report_number = 1
    else:
        report_number = int(rep_num)+1

    try:
        cursor.execute("INSERT INTO REPORT (REPORT_NUMBER, PROJECT_NUM, CHANGES, HOURS, PERSON_NUMBER) VALUES (?, ?, ?, ?, ?)", (report_number, project_num, changes, hours, per_num, ))
        db.commit() 
        return f"Insert into *report* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e
# add_into_report("projects.db")

def add_into_history(db_name, per_num_3, position, status):
    db, cursor = connector(db_name)
    try: 
        cursor.execute("INSERT INTO HISTORY (PERFORMER_NUMBER, POSITION, STATUS) VALUES (?, ?, ?)", (per_num_3, position, status, ))
        db.commit()
        return f"Insert into *history* successfull."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

def query(db_name, query):
    db, cursor = connector(db_name)
    try:
        cursor.execute(f"{query}")
        db.commit()
        
        return f"Query complete successfully."
    except sq.OperationalError as e:
        return e
    except sq.IntegrityError as e:
        return e
    except sq.InterfaceError as e:
        return e
    except Exception as e:
        return e

def add_charge(db_name, charge, customer):
    db, cursor = connector(db_name)
    try:
        cursor.execute("SELECT CHARGE FROM CUSTOMERS WHERE CUSTOMERS_NUMBER = (?)", (customer,))
        data = cursor.fetchall()
        data = clear(data)
        data = float(data)
        data += float(charge)
        cursor.execute("UPDATE CUSTOMERS SET CHARGE = ? WHERE CUSTOMERS_NUMBER LIKE ?", (data, customer))
        db.commit()
        return f"Charge added into customers!"
    except Exception as e:
        return f"Error: {e}"

def finished_or_not(db_name, number_of_project, finish):

    try:
        finish = finish.capitalize()

        db, cursor = connector(db_name)

        cursor.execute(
            "UPDATE PROJECTS_IN_PROGRESS SET FINISH = ? WHERE NUMBER_OF_PROJECT = (?)", (finish, number_of_project)
        )
        db.commit()
        return f"Datas added successfully!"
    except Exception as e:
        return f"Error: {e}"

# finished_or_not("projects.db", 3, "Finished")