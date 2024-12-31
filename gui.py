from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QLabel, QFileDialog, QPushButton, QRadioButton,
    QButtonGroup, QStackedWidget, QWidget, QVBoxLayout, QTextEdit, QCheckBox
)
from PyQt6.QtGui import QGuiApplication, QFont, QKeySequence, QShortcut
import sys
import os
from query import add_into_project, add_into_about_company, add_into_projects_in_progress, add_into_coefficients,\
add_into_customers, add_into_payroll, add_into_debtors, add_into_payment, add_into_report, add_into_history, query, add_charge,\
finished_or_not
import sqlite3 as sq
from salaries import num_of_persons
from dismissal import start_diss
from report_for_debtors import report_for_dept
from report_of_all_projects import all_projects_report
from report_of_month import rep_of_month
class Page1(QWidget):
    def __init__(self):
        screen = QGuiApplication.primaryScreen()
        screen_g = screen.geometry()
        screen_width = screen_g.width()/1.1
        screen_height = screen_g.height()/1.1
        super().__init__()

        self.h3_font = QFont("Inter", 12)

        layout = QVBoxLayout(self)
        # ----------------------------------------------
        self.select_table1 = QRadioButton("Projects")
        self.select_table1.setFont(self.h3_font)

        self.name = QTextEdit(self)
        self.name.setPlaceholderText("Name of project")

        self.num_of_cus = QTextEdit(self)
        self.num_of_cus.setPlaceholderText("Number of customer")

        self.proj_men_num = QTextEdit(self)
        self.proj_men_num.setPlaceholderText("Number of project manager")

        self.dur_of_ex = QTextEdit(self)
        self.dur_of_ex.setPlaceholderText("Duration of execution")

        self.dif_cat = QTextEdit(self)
        self.dif_cat.setPlaceholderText("Difficulty category")

        self.beg_date = QTextEdit(self)
        self.beg_date.setPlaceholderText("Begin date")

        #------------------------------------------------

        self.select_table2 = QRadioButton("About company")
        self.select_table2.setFont(self.h3_font)

        self.per_num = QTextEdit(self)
        self.per_num.setPlaceholderText("Performer number")
        
        self.f_l_p = QTextEdit(self)
        self.f_l_p.setPlaceholderText("F.L.P.")

        self.post = QTextEdit(self)
        self.post.setPlaceholderText("Post name")
        
        self.skill_level = QTextEdit(self)
        self.skill_level.setPlaceholderText("Skill level")

        # -----------------------------------------------

        self.select_table3 = QRadioButton("Projects_in_progress")
        self.select_table3.setFont(self.h3_font)

        self.num_of_pr = QTextEdit(self)
        self.num_of_pr.setPlaceholderText("Number of project")

        self.per_num1 = QTextEdit(self)
        self.per_num1.setPlaceholderText("Performers number")

        self.price = QTextEdit(self)
        self.price.setPlaceholderText("Price")

        # ------------------------------------------------

        self.select_table4 = QRadioButton("Coefficients")
        self.select_table4.setFont(self.h3_font)

        self.dif_num = QTextEdit(self)
        self.dif_num.setPlaceholderText("Difficult number")

        self.proj_dif = QTextEdit(self)
        self.proj_dif.setPlaceholderText("Projects difficult")

        self.al_coef = QTextEdit(self)
        self.al_coef.setPlaceholderText("Allowance Coefficient")

        # -------------------------------------------------

        self.select_table5 = QRadioButton("Customers")
        self.select_table5.setFont(self.h3_font)

        self.cus_num = QTextEdit(self)
        self.cus_num.setPlaceholderText("Customers number")

        self.customer = QTextEdit(self)
        self.customer.setPlaceholderText("Customer")

        self.n_n_t = QTextEdit(self)
        self.n_n_t.setPlaceholderText("Non paying term")

        self.charge = QCheckBox(self)
        
        self.charge_text = QTextEdit(self)
        self.charge_text.setPlaceholderText("Charge")

        self.select_group = QButtonGroup(self)
        self.select_group.addButton(self.select_table1)
        self.select_group.addButton(self.select_table2)
        self.select_group.addButton(self.select_table3)
        self.select_group.addButton(self.select_table4)
        self.select_group.addButton(self.select_table5)

        layout.addWidget(self.select_table1)
        layout.addWidget(self.select_table2)
        layout.addWidget(self.select_table3)
        layout.addWidget(self.select_table4)
        layout.addWidget(self.select_table5)

        self.next = QPushButton("Next")
        self.next.setStyleSheet("QPushButton{border: 2px solid grey; border-radius: 8px}")
        self.next.setFixedSize(170, 30)
        self.next.move(int(screen_width / 2.5), int(screen_height / 5))
        layout.addWidget(self.next)

    def get_elements(self):
        return {"select_table1": self.select_table1, 
                "select_table2": self.select_table2, 
                "select_table3":self.select_table3, 
                "select_table4":self.select_table4, 
                "select_table5":self.select_table5,
                # "number":self.number, 
                "name":self.name,
                "num_of_cus":self.num_of_cus, 
                "proj_men_num":self.proj_men_num, 
                "dur_of_ex":self.dur_of_ex, 
                "dif_cat":self.dif_cat, 
                "beg_date":self.beg_date,

                "per_num": self.per_num,
                "f_l_p": self.f_l_p,
                "post": self.post,
                "skill_level": self.skill_level,

                "num_of_pr": self.num_of_pr,
                "per_num1": self.per_num1,
                "price": self.price,

                "dif_num": self.dif_num,
                "proj_dif": self.proj_dif,
                "al_coef": self.al_coef,

                "cus_num": self.cus_num,
                "customer": self.customer,
                "n_n_t": self.n_n_t,
                "charge": self.charge,
                "charge_text": self.charge_text
                }



class Page2(QWidget):
    def __init__(self):
        super().__init__()

        self.h3_font = QFont("Inter", 12)

        layout = QVBoxLayout(self)

        self.select_table6 = QRadioButton("Payroll")
        self.select_table6.setFont(self.h3_font)

        self.per_num2 = QTextEdit(self)
        self.per_num2.setPlaceholderText("Performers number")
        
        self.bank_num = QTextEdit(self)
        self.bank_num.setPlaceholderText("Bank account number")

        self.select_table7 = QRadioButton("Debtors")
        self.select_table7.setFont(self.h3_font)

        self.cuss_num = QTextEdit(self)
        self.cuss_num.setPlaceholderText("Customers number")

        self.am_of_deb = QTextEdit(self)
        self.am_of_deb.setPlaceholderText("Amount of debt")

        self.select_table8 = QRadioButton("Payment")
        self.select_table8.setFont(self.h3_font)

        self.post = QTextEdit(self)
        self.post.setPlaceholderText("Post")

        self.h_p_r = QTextEdit(self)
        self.h_p_r.setPlaceholderText("Hourly payment rate")

        self.all_r = QTextEdit(self)
        self.all_r.setPlaceholderText("Allowance ratio")

        self.select_table9 = QRadioButton("Report")
        self.select_table9.setFont(self.h3_font)
        
        self.project_num = QTextEdit(self)
        self.project_num.setPlaceholderText("Project number")

        self.changes = QTextEdit(self)
        self.changes.setPlaceholderText("Changes")

        self.hours = QTextEdit(self)
        self.hours.setPlaceholderText("Hours")

        self.num_per = QTextEdit(self)
        self.num_per.setPlaceholderText("Performers number")

        self.select_table10 = QRadioButton("History")
        self.select_table10.setFont(self.h3_font)

        self.per_num_3 = QTextEdit(self)
        self.per_num_3.setPlaceholderText("Performers number")

        self.position = QTextEdit(self)
        self.position.setPlaceholderText("Position")

        self.status = QTextEdit(self)
        self.status.setPlaceholderText("Status")

        self.select_group = QButtonGroup(self)
        self.select_group.addButton(self.select_table6)
        self.select_group.addButton(self.select_table7)
        self.select_group.addButton(self.select_table8)
        self.select_group.addButton(self.select_table9)
        self.select_group.addButton(self.select_table10)

        layout.addWidget(self.select_table6)
        layout.addWidget(self.select_table7)
        layout.addWidget(self.select_table8)
        layout.addWidget(self.select_table9)
        layout.addWidget(self.select_table10)

        self.back = QPushButton("Back")
        self.back.setStyleSheet("QPushButton{border: 2px solid grey; border-radius: 8px}")
        self.back.setFixedSize(170, 30)
        self.back.move(200, 300)
        layout.addWidget(self.back)

    def get_elements_2(self):
        return {
            "select_table6": self.select_table6,
            "per_num2": self.per_num2,
            "bank_num": self.bank_num,
            "select_table7": self.select_table7,
            "cuss_num": self.cuss_num,
            "am_of_deb": self.am_of_deb,
            "select_table8": self.select_table8,
            "post": self.post,
            "h_p_r": self.h_p_r,
            "all_r":self.all_r,
            "select_table9": self.select_table9,
            "project_num": self.project_num,
            "changes": self.changes,
            "hours": self.hours,
            "num_per": self.num_per,
            "select_table10": self.select_table10,
            "per_num_3": self.per_num_3,
            "position": self.position,
            "status": self.status
        }

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Projects Editor")
        screen = QGuiApplication.primaryScreen()
        screen_g = screen.geometry()
        screen_width = screen_g.width()/1.1
        screen_height = screen_g.height()/1.1

        self.h2_font = QFont("Inter", 20)

        self.setFixedSize(int(screen_width), int(screen_height))

        self.h3_font = QFont("Inter", 12)

        self.select = QPushButton("Select database", self)
        self.select.setStyleSheet("QPushButton{border: 2px solid grey; border-radius: 8px}")
        self.select.setFixedSize(170, 40)
        self.select.move(int(screen_width / 1.5), int(screen_height / 9))
        self.select.clicked.connect(self.select_file)

        self.select.setFont(self.h3_font)

        self.select_table_h2 = QLabel("Select table", self)
        self.select_table_h2.setFixedSize(400, 50)
        self.select_table_h2.setFont(self.h2_font)
        self.select_table_h2.move(int(screen_width / 10), int(screen_height / 8.5))

        self.pages = QStackedWidget(self)
        self.pages.setFixedSize(int(screen_width / 1), int(screen_height / 2))
        self.pages.move(int(screen_width/10), int(screen_height/5.5))

        self.page1 = Page1()
        self.page2 = Page2()

        self.pages.addWidget(self.page1)
        self.pages.addWidget(self.page2)

        self.page1.next.clicked.connect(self.next_page2)
        self.page2.back.clicked.connect(self.next_page1)


        self.page1_elements = self.page1.get_elements()

        self.page1_elements["name"].setParent(self)
        self.page1_elements["name"].move(int(screen_width/3), int(screen_height/4.8))
        self.page1_elements["name"].setFixedSize(170, 28)
        self.page1_elements["name"].setVisible(False)

        self.page1_elements["num_of_cus"].setParent(self)
        self.page1_elements["num_of_cus"].move(int(screen_width/2), int(screen_height/4.8))
        self.page1_elements["num_of_cus"].setFixedSize(170, 28)
        self.page1_elements["num_of_cus"].setVisible(False)

        self.page1_elements["proj_men_num"].setParent(self)
        self.page1_elements["proj_men_num"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page1_elements["proj_men_num"].setFixedSize(170, 28)
        self.page1_elements["proj_men_num"].setVisible(False)

        self.page1_elements["dur_of_ex"].setParent(self)
        self.page1_elements["dur_of_ex"].move(int(screen_width/3), int(screen_height/3.5))
        self.page1_elements["dur_of_ex"].setFixedSize(170, 28)
        self.page1_elements["dur_of_ex"].setVisible(False)

        self.page1_elements["dif_cat"].setParent(self)
        self.page1_elements["dif_cat"].move(int(screen_width/2), int(screen_height/3.5))
        self.page1_elements["dif_cat"].setFixedSize(170, 28)
        self.page1_elements["dif_cat"].setVisible(False)

        self.page1_elements["beg_date"].setParent(self)
        self.page1_elements["beg_date"].move(int(screen_width/1.5), int(screen_height/3.5))
        self.page1_elements["beg_date"].setFixedSize(170, 28)
        self.page1_elements["beg_date"].setVisible(False)

        self.button_1 = QPushButton("Submit", self)
        self.button_1.setFixedSize(170, 28)
        self.button_1.move(int(screen_width/3), int(screen_height/2.3))
        self.button_1.setVisible(False)
        self.button_1.clicked.connect(self.button_checked)   

        self.rep_month = QPushButton("Report of month", self)
        self.rep_month.setFixedSize(170, 28)
        self.rep_month.move(int(screen_width/3), int(screen_height/2))
        self.rep_month.setVisible(False)

        self.finish_button = QPushButton("Send datas", self)
        self.finish_button.move(int(screen_width/2), int(screen_height/2.3))
        self.finish_button.setFixedSize(170, 28)
        self.finish_button.setEnabled(False)
        self.finish_button.setVisible(False)
        self.finish_button.clicked.connect(self.send_finish_or_not)

        self.button_1_2 = QPushButton("Add experemental datas", self)
        self.button_1_2.setFixedSize(170, 28)
        self.button_1_2.move(int(screen_width/2), int(screen_height/2.3))
        self.button_1_2.setVisible(False)
        self.button_1_2.clicked.connect(self.experement)   

        self.button_2 = QPushButton("Calculation of salaries", self)
        self.button_2.setFixedSize(170, 28)
        self.button_2.move(int(screen_width/1.5), int(screen_height/2.3))
        self.button_2.setVisible(False)
        self.button_2.clicked.connect(self.press_report)

        self.button_report_debt = QPushButton("Report of debtors", self)
        self.button_report_debt.setFixedSize(170, 28)
        self.button_report_debt.move(int(screen_width/1.92), int(screen_height/2.3))
        self.button_report_debt.setVisible(False)
        # self.button_report_debt.clck
        self.button_report_debt.clicked.connect(self.creating_report)# /////////////
        self.button_report_debt.setEnabled(False)# ///////////

        self.date_checkbox = QCheckBox(self)
        self.date_checkbox.move(int(screen_width/2), int(screen_height/2.3))
        # self.date_checkbox.setFixedSize()
        self.date_checkbox.setVisible(False)
        self.date_checkbox.clicked.connect(self.some_f)

        self.date = QTextEdit("02.02.2025", self)
        self.date.setFixedSize(170, 28)
        self.date.setPlaceholderText("Set your date.")
        self.date.setVisible(False)


        self.date_debt = QTextEdit("02.02.2025", self)
        self.date_debt.setFixedSize(170, 28)
        self.date_debt.setPlaceholderText("Set your date.")
        self.date_debt.setVisible(False)
        self.date_debt.move(int(screen_width/1.45), int(screen_height/2.3))
        # self.date.setEnabled(False)


        self.dismissal = QPushButton("Dissmissal person", self)
        self.dismissal.setFixedSize(170, 28)
        self.dismissal.move(int(screen_width/2), int(screen_height/2))
        self.dismissal.setVisible(False)
        self.dismissal.clicked.connect(self.diss)

        # -------------------------------------------------

        self.page1_elements["per_num"].setParent(self)
        self.page1_elements["per_num"].move(int(screen_width/3), int(screen_height/4.8))
        self.page1_elements["per_num"].setFixedSize(170, 28)
        self.page1_elements["per_num"].setVisible(False)

        self.page1_elements["f_l_p"].setParent(self)
        self.page1_elements["f_l_p"].move(int(screen_width/2), int(screen_height/4.8))
        self.page1_elements["f_l_p"].setFixedSize(170, 28)
        self.page1_elements["f_l_p"].setVisible(False)

        self.page1_elements["post"].setParent(self)
        self.page1_elements["post"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page1_elements["post"].setFixedSize(170, 28)
        self.page1_elements["post"].setVisible(False)

        self.page1_elements["skill_level"].setParent(self)
        self.page1_elements["skill_level"].move(int(screen_width/3), int(screen_height/3.5))
        self.page1_elements["skill_level"].setFixedSize(170, 28)
        self.page1_elements["skill_level"].setVisible(False)
        
        # -------------------------------------------
        self.page1_elements["num_of_pr"].setParent(self)
        self.page1_elements["num_of_pr"].move(int(screen_width/3), int(screen_height/4.8))
        self.page1_elements["num_of_pr"].setFixedSize(170, 28)
        self.page1_elements["num_of_pr"].setVisible(False)

        self.page1_elements["per_num1"].setParent(self)
        self.page1_elements["per_num1"].move(int(screen_width/2), int(screen_height/4.8))
        self.page1_elements["per_num1"].setFixedSize(170, 28)
        self.page1_elements["per_num1"].setVisible(False)

        self.page1_elements['price'].setParent(self)
        self.page1_elements["price"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page1_elements["price"].setFixedSize(170, 28)
        self.page1_elements["price"].setVisible(False)

        self.finish_checkbox = QCheckBox(self)
        self.finish_checkbox.move(int(screen_width/3), int(screen_height/3.5))
        self.finish_checkbox.setVisible(False)
        self.finish_checkbox.clicked.connect(self.some_f_1)
        
        self.finish_text = QTextEdit(self)
        self.finish_text.setPlaceholderText("Finished or not")
        self.finish_text.move(int(screen_width/2.85), (int(screen_height/3.5)))
        self.finish_text.setFixedSize(170, 28)
        self.finish_text.setEnabled(False)
        self.finish_text.setVisible(False)

        self.report_all_pr = QPushButton("Report of all projects", self)
        self.report_all_pr.move(int(screen_width/1.5), int(screen_height/2.3))
        self.report_all_pr.setFixedSize(170, 28)
        self.report_all_pr.setVisible(False)
        self.report_all_pr.clicked.connect(self.send_report_for_all_pr)
        # --------------------------------------------

        self.page1_elements["dif_num"].setParent(self)
        self.page1_elements["dif_num"].move(int(screen_width/3), int(screen_height/4.8))
        self.page1_elements["dif_num"].setFixedSize(170, 28)
        self.page1_elements["dif_num"].setVisible(False)

        self.page1_elements["proj_dif"].setParent(self)
        self.page1_elements["proj_dif"].move(int(screen_width/2), int(screen_height/4.8))
        self.page1_elements["proj_dif"].setFixedSize(170, 28)
        self.page1_elements["proj_dif"].setVisible(False)

        self.page1_elements["al_coef"].setParent(self)
        self.page1_elements["al_coef"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page1_elements["al_coef"].setFixedSize(170, 28)
        self.page1_elements["al_coef"].setVisible(False)

        # --------------------------------------------

        self.page1_elements["cus_num"].setParent(self)
        self.page1_elements["cus_num"].move(int(screen_width/3), int(screen_height/4.8))
        self.page1_elements["cus_num"].setFixedSize(170, 28)
        self.page1_elements["cus_num"].setVisible(False)

        self.page1_elements["customer"].setParent(self)
        self.page1_elements["customer"].move(int(screen_width/2), int(screen_height/4.8))
        self.page1_elements["customer"].setFixedSize(170, 28)
        self.page1_elements["customer"].setVisible(False)

        self.page1_elements["n_n_t"].setParent(self)
        self.page1_elements["n_n_t"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page1_elements["n_n_t"].setFixedSize(170, 28)
        self.page1_elements["n_n_t"].setVisible(False)

        self.page1_elements["charge"].setParent(self)
        self.page1_elements["charge"].move(int(screen_width/3.2), int(screen_height/3.5))
        self.page1_elements["charge"].setFixedSize(170, 28)
        self.page1_elements["charge"].setVisible(False)
        self.page1_elements["charge"].stateChanged.connect(self.checking)

        self.page1_elements["charge_text"].setParent(self)
        self.page1_elements["charge_text"].move(int(screen_width/3), int(screen_height/3.5))
        self.page1_elements["charge_text"].setFixedSize(170, 28)
        self.page1_elements["charge_text"].setVisible(False)
        self.page1_elements["charge_text"].setEnabled(False)
        
        # --------------------------------------------

        self.operations_font = QFont("Inter", 12)

        self.page1_elements["select_table1"].clicked.connect(self.checker)
        self.page1_elements["select_table2"].clicked.connect(self.checker)
        self.page1_elements["select_table3"].clicked.connect(self.checker)
        self.page1_elements["select_table4"].clicked.connect(self.checker)
        self.page1_elements["select_table5"].clicked.connect(self.checker)

        self.operations = QTextEdit(self)
        self.operations.setPlaceholderText("For change something, use the terminal...")
        self.operations.setFixedSize(int(screen_width/1.7), int(screen_height/3.5))
        self.operations.move(int(screen_width/55), int(screen_height/1.5))
        self.operations.setFont(self.operations_font)
        self.operations.setStyleSheet("border: 3px solid grey; border-radius: 10px")

        # press for sending query
        self.shortcutCR = QShortcut(QKeySequence("Ctrl+Return"), self.operations)
        self.shortcutCR.activated.connect(self.some_function)
        
        self.shortcutCE = QShortcut(QKeySequence("Ctrl+Enter"), self.operations)
        self.shortcutCE.activated.connect(self.some_function)


        self.shortcutCO = QShortcut(QKeySequence("Ctrl+O"), self.select)
        self.shortcutCO.activated.connect(self.select_file)

        self.output = QLabel("Output", self)
        self.output.setWordWrap(True)
        self.output.setFixedSize(int(screen_width/3), int(screen_height/3.5))
        self.output.move(int(screen_width/1.58), int(screen_height/1.5))
        self.output.setFont(self.operations_font)
        self.output.setStyleSheet("border: 3px solid grey; border-radius: 10px; background-color: #FFFFFF")

        self.page2_elements = self.page2.get_elements_2()

        # ======================================================================

        self.page2_elements["per_num2"].setParent(self)
        self.page2_elements["per_num2"].move(int(screen_width/3), int(screen_height/4.8))
        self.page2_elements["per_num2"].setFixedSize(170, 28)
        self.page2_elements["per_num2"].setVisible(False)

        self.page2_elements["bank_num"].setParent(self)
        self.page2_elements["bank_num"].move(int(screen_width/2), int(screen_height/4.8))
        self.page2_elements["bank_num"].setFixedSize(170, 28)
        self.page2_elements["bank_num"].setVisible(False)
        
        # ======================================================

        self.page2_elements["cuss_num"].setParent(self)
        self.page2_elements["cuss_num"].move(int(screen_width/3), int(screen_height/4.8))
        self.page2_elements["cuss_num"].setFixedSize(170, 28)
        self.page2_elements["cuss_num"].setVisible(False)

        self.page2_elements["am_of_deb"].setParent(self)
        self.page2_elements["am_of_deb"].move(int(screen_width/2), int(screen_height/4.8))
        self.page2_elements["am_of_deb"].setFixedSize(170, 28)
        self.page2_elements["am_of_deb"].setVisible(False)

        # ------------------------------------------------------------

        self.page2_elements["post"].setParent(self)
        self.page2_elements["post"].move(int(screen_width/3), int(screen_height/4.8))
        self.page2_elements["post"].setFixedSize(170, 28)
        self.page2_elements["post"].setVisible(False)

        self.page2_elements["h_p_r"].setParent(self)
        self.page2_elements["h_p_r"].move(int(screen_width/2), int(screen_height/4.8))
        self.page2_elements["h_p_r"].setFixedSize(170, 28)
        self.page2_elements["h_p_r"].setVisible(False)

        self.page2_elements["all_r"].setParent(self)
        self.page2_elements["all_r"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page2_elements["all_r"].setFixedSize(170, 28)
        self.page2_elements["all_r"].setVisible(False)
    
        # ==========================================

        self.page2_elements["project_num"].setParent(self)
        self.page2_elements["project_num"].move(int(screen_width/3), int(screen_height/4.8))
        self.page2_elements["project_num"].setFixedSize(170, 28)
        self.page2_elements["project_num"].setVisible(False)

        self.page2_elements["changes"].setParent(self)
        self.page2_elements["changes"].move(int(screen_width/2), int(screen_height/4.8))
        self.page2_elements["changes"].setFixedSize(170, 28)
        self.page2_elements["changes"].setVisible(False)

        self.page2_elements["hours"].setParent(self)
        self.page2_elements["hours"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page2_elements["hours"].setFixedSize(170, 28)
        self.page2_elements["hours"].setVisible(False)

        self.page2_elements["num_per"].setParent(self)
        self.page2_elements["num_per"].move(int(screen_width/3), int(screen_height/3.5))
        self.page2_elements["num_per"].setFixedSize(170, 28)
        self.page2_elements["num_per"].setVisible(False)


        # ---------------------------------------------------------

        self.page2_elements["per_num_3"].setParent(self)
        self.page2_elements["per_num_3"].move(int(screen_width/3), int(screen_height/4.8))
        self.page2_elements["per_num_3"].setFixedSize(170, 28)
        self.page2_elements["per_num_3"].setVisible(False)

        self.page2_elements["position"].setParent(self)
        self.page2_elements["position"].move(int(screen_width/2), int(screen_height/4.8))
        self.page2_elements["position"].setFixedSize(170, 28)
        self.page2_elements["position"].setVisible(False)

        self.page2_elements["status"].setParent(self)
        self.page2_elements["status"].move(int(screen_width/1.5), int(screen_height/4.8))
        self.page2_elements["status"].setFixedSize(170, 28)
        self.page2_elements["status"].setVisible(False)
        
        
        self.page2_elements["select_table6"].clicked.connect(self.checker_for_page_2)
        self.page2_elements["select_table7"].clicked.connect(self.checker_for_page_2)
        self.page2_elements["select_table8"].clicked.connect(self.checker_for_page_2)
        self.page2_elements["select_table9"].clicked.connect(self.checker_for_page_2)
        self.page2_elements["select_table10"].clicked.connect(self.checker_for_page_2)

    def senf_rep_(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please")
        else:
            db_name = self.select.text()
            num_of_pr = self.page1_elements["num_of_pr"].text()
            response = rep_of_month(db_name, num_of_pr)
            self.output.setText(response)

    def send_report_for_all_pr(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please")
        else:
            db_name = self.select.text()
            response = all_projects_report(db_name)
            self.output.setText(response)

    def send_finish_or_not(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please")
        else:
            db_name = self.select.text()
            num_of_pr = self.page1_elements["num_of_pr"].toPlainText()
            fin = self.finish_text.toPlainText()
            response = finished_or_not(db_name, num_of_pr, fin)
            self.output.setText(response)

    def some_f_1(self):
        if self.finish_checkbox.isChecked():
            self.finish_text.setEnabled(True)
            # self.finish_text.setVisible(True)
            self.finish_button.setEnabled(True)
            self.finish_button.setVisible(True)
        else:
            self.finish_text.setEnabled(False)
            self.finish_button.setEnabled(False)

            # self.finish_text.setVisible(False)

    def some_f(self):
        if self.date_checkbox.isChecked():
            self.button_report_debt.setEnabled(True)
            # self.date.setEnabled(True)
            self.date_debt.setVisible(True)
        else:
            self.button_report_debt.setEnabled(False)
            # self.date.setEnabled(False)
            self.date_debt.setVisible(False)

    # def checkbox_on(self):

    def creating_report(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please")
        else:
            # os.system("python ../mini_project/dismissal.py")
            # int(screen_width/1.5), int(screen_height/2.3)
            db_name = self.select.text()
            date_debt = self.date_debt.toPlainText()
            response = report_for_dept(db_name, date_debt)
            self.output.setText(response)

    def checking(self):
        if self.page1_elements["charge"].isChecked():
            self.page1_elements["charge_text"].setEnabled(True)
        else:
            self.page1_elements["charge_text"].setEnabled(False)

    def diss(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please")
        else:
            # os.system("python ../mini_project/dismissal.py")
            response = start_diss()
            self.output.setText(response)
            
    def experement(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please")
        else:
            os.system("python ../mini_project/test_datas.py")

    def press_report(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please.")
        else:
            db_name = self.select.text()
            date = self.date.toPlainText()
            response = num_of_persons(db_name, date) 
            self.output.setText(str(response))

    def some_function(self):
        db_name = self.select.text()
        
        if self.operations.toPlainText() == "":
            self.output.setText("Enter query, please.")
        else:
            queries = self.operations.toPlainText()
            try:
                response = query(db_name, queries)
                self.output.setText(response)
            except sq.OperationalError as e:
                self.output.setText(f"Error: {str(e)}")
            except sq.IntegrityError as e:
                self.output.setText(f"Error: {str(e)}")
            except sq.InterfaceError as e:
                self.output.setText(f"Error: {str(e)}")
            except TypeError as e:
                self.output.setText(f"Error: type error!")
            except Exception as e:
                self.output.setText(f"Error: {str(e)}")

    def next_page1(self):
        self.pages.setCurrentIndex(0)

    def next_page2(self):
        self.pages.setCurrentIndex(1)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select database", "../mini_project/databases/", "DataBase(*.db)")
        if file_path:
            name = os.path.basename(file_path)
            self.select.setText(name)
    
    def button_checked(self):
        if self.select.text() == "Select database":
            self.output.setText("Select database, please.")
        else:
            db_name = self.select.text()
            if self.page1_elements["select_table1"].isChecked():

                # number = self.page1_elements["number"].toPlainText()
                name = self.page1_elements["name"].toPlainText()
                num_of_cus = self.page1_elements["num_of_cus"].toPlainText()
                proj_men_num = self.page1_elements["proj_men_num"].toPlainText()
                dur_of_ex = self.page1_elements["dur_of_ex"].toPlainText()
                dif_cat = self.page1_elements["dif_cat"].toPlainText()
                beg_date = self.page1_elements["beg_date"].toPlainText()
                response = add_into_project(db_name, name, num_of_cus, proj_men_num, dur_of_ex, dif_cat, beg_date)
                self.output.setText(str(response))
                print("All ok1")
                self.page1_elements["name"].clear()
                self.page1_elements["num_of_cus"].clear()
                self.page1_elements["proj_men_num"].clear()
                self.page1_elements["dur_of_ex"].clear()
                self.page1_elements["dif_cat"].clear()
                self.page1_elements["beg_date"].clear()

            elif self.page1_elements["select_table2"].isChecked():
                    
                per_num = self.page1_elements["per_num"].toPlainText()
                f_l_p = self.page1_elements["f_l_p"].toPlainText()
                post = self.page1_elements["post"].toPlainText()
                skill_level = self.page1_elements["skill_level"].toPlainText()
                response = add_into_about_company(db_name, per_num, f_l_p, post, skill_level)
                self.output.setText(str(response))
                print("All ok2")
                self.page1_elements["per_num"].clear()
                self.page1_elements["f_l_p"].clear()
                self.page1_elements["post"].clear()
                self.page1_elements["skill_level"].clear()
            
            elif self.page1_elements["select_table3"].isChecked():
                    num_of_pr = self.page1_elements["num_of_pr"].toPlainText()
                    per_num1 = self.page1_elements["per_num1"].toPlainText()
                    price = self.page1_elements["price"].toPlainText()
                    response = add_into_projects_in_progress(db_name, num_of_pr, per_num1, price)
                    self.output.setText(str(response))
                    print("All ok3")
                    self.page1_elements["num_of_pr"].clear()
                    self.page1_elements["per_num1"].clear()
                    self.page1_elements["price"].clear()
            elif self.page1_elements["select_table4"].isChecked():
                
                    dif_num = self.page1_elements["dif_num"].toPlainText()
                    proj_dif = self.page1_elements["proj_dif"].toPlainText()
                    al_coef = self.page1_elements["al_coef"].toPlainText()
                    response = add_into_coefficients(db_name, dif_num, proj_dif, al_coef)
                    self.output.setText(str(response))
                    print("All ok4")
                    self.page1_elements["dif_num"].clear()
                    self.page1_elements["proj_dif"].clear()
                    self.page1_elements["al_coef"].clear()

            elif self.page1_elements["select_table5"].isChecked():
                if self.page1_elements["charge"].isChecked():
                    charge_ = self.page1_elements["charge_text"].toPlainText()
                    customer_ = self.page1_elements["cus_num"].toPlainText()
                    response = add_charge(db_name, charge_, customer_)
                    self.output.setText(response)
                else:
                    cus_num = self.page1_elements["cus_num"].toPlainText()
                    customer = self.page1_elements["customer"].toPlainText()
                    n_n_t = self.page1_elements["n_n_t"].toPlainText()
                    # charge = self.page1_elements["charge"].toPlainText()
                    response = add_into_customers(db_name, cus_num, customer, n_n_t)
                    self.output.setText(str(response))
                    print("All ok5")
                    self.page1_elements["cus_num"].clear()
                    self.page1_elements["customer"].clear()
                    self.page1_elements["n_n_t"].clear()
                    # self.page1_elemetns["charge"].clear()
                
            elif self.page2_elements["select_table6"].isChecked():
                
                    per_num2 = self.page2_elements["per_num2"].toPlainText()
                    bank_num = self.page2_elements["bank_num"].toPlainText()
                    # wage = self.page2_elements["wage"].toPlainText()
                    response = add_into_payroll(db_name, int(per_num2), bank_num)
                    self.output.setText(str(response))
                    print("All ok6")
                    self.page2_elements["per_num2"].clear()
                    self.page2_elements["bank_num"].clear()
                
            elif self.page2_elements["select_table7"].isChecked():
                    self.date.move(int(self.screen_width/1.2), int(self.screen_height/2.3))
                    self.date.setVisible(True)
                    # num_of_deb = self.page2_elements["num_of_deb"].toPlainText()
                    cuss_num = self.page2_elements["cuss_num"].toPlainText()
                    am_of_deb = self.page2_elements["am_of_deb"].toPlainText()
                    response = add_into_debtors(db_name, cuss_num, am_of_deb)
                    self.output.setText(str(response))
                    print("All ok7")
                    self.page2_elements["cuss_num"].clear()
                    self.page2_elements["am_of_deb"].clear()

            
            elif self.page2_elements["select_table8"].isChecked():
                
                    post = self.page2_elements["post"].toPlainText()
                    h_p_r = self.page2_elements["h_p_r"].toPlainText()
                    all_r = self.page2_elements["all_r"].toPlainText()
                    response = add_into_payment(db_name, post, h_p_r, all_r)
                    self.output.setText(str(response))
                    print("All ok7")
                    self.page2_elements["post"].clear()
                    self.page2_elements["h_p_r"].clear()
                    self.page2_elements["all_r"].clear()



            
            elif self.page2_elements["select_table9"].isChecked():
                
                    project = self.page2_elements["project_num"].toPlainText()
                    changes = self.page2_elements["changes"].toPlainText()
                    hours = self.page2_elements["hours"].toPlainText()
                    num_per = self.page2_elements["num_per"].toPlainText()
                    if float(hours) > 10:
                        self.output.setText("Performer can`t report for more than 10 hours")
                    else:
                        response = add_into_report(db_name, project, changes, hours, num_per)
                        self.output.setText(str(response))
                        print("All ok8")
                        self.page2_elements["project_num"].clear()
                        self.page2_elements["changes"].clear()
                        self.page2_elements["hours"].clear()
                        self.page2_elements["num_per"].clear()



            elif self.page2_elements["select_table10"].isChecked():
                
                    per_num3 = self.page2_elements["per_num3"].toPlainText()
                    position = self.page2_elements["position"].toPlainText()
                    status = self.page2_elements["status"].toPlainText()
                    response = add_into_history(db_name, per_num3, position, status)
                    self.output.setText(str(response))
                    print("All ok9")
                    self.page2_elements["per3_num"].clear()
                    self.page2_elements["position"].clear()
                    self.page2_elements["status"].clear()


    def checker_for_page_2(self):
        if self.page2_elements["select_table6"].isChecked():
            
            self.page2_elements["per_num2"].setVisible(True)
            self.page2_elements["bank_num"].setVisible(True)
            # self.page2_elements["wage"].setVisible(True)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            # self.page1_elements["number"].setVisible(False)
            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)
            self.date_checkbox.setVisible(False)
            self.date_debt.setVisible(False)
            # self.update.setVisible(True)


        elif self.page2_elements["select_table7"].isChecked():

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(True)
            self.page2_elements["cuss_num"].setVisible(True)
            self.page2_elements["am_of_deb"].setVisible(True)
            # self.date_debt.setVisible(True)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)
            

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            # self.page1_elements["number"].setVisible(False)
            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)
            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)
            self.button_report_debt.setVisible(True)
            self.date_checkbox.setVisible(True)
            # self.update.setVisible(True)

        elif self.page2_elements["select_table8"].isChecked():

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(True)
            self.page2_elements["h_p_r"].setVisible(True)
            self.page2_elements["all_r"].setVisible(True)

            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)
            

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            # self.page1_elements["number"].setVisible(False)
            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)
            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

        elif self.page2_elements["select_table9"].isChecked():

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            self.page2_elements["project_num"].setVisible(True)
            self.page2_elements["changes"].setVisible(True)
            self.page2_elements["hours"].setVisible(True)
            self.page2_elements["num_per"].setVisible(True)
            self.rep_month.setVisible(True)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            # self.page1_elements["number"].setVisible(False)
            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(True)
            self.button_1_2.setVisible(True)
            self.dismissal.setVisible(True)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

        elif self.page2_elements["select_table10"].isChecked():

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(True)
            self.page2_elements["position"].setVisible(True)
            self.page2_elements["status"].setVisible(True)
            # self.page2_elements["num_per"].setVisible(True)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)
            

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            # self.page1_elements["number"].setVisible(False)
            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)


    def checker(self):
        if self.page1_elements["select_table1"].isChecked():

            # self.page1_elements["number"].setVisible(True)
            self.page1_elements["name"].setVisible(True)
            self.page1_elements["num_of_cus"].setVisible(True)
            self.page1_elements["proj_men_num"].setVisible(True)
            self.page1_elements["dur_of_ex"].setVisible(True)
            self.page1_elements["dif_cat"].setVisible(True)
            self.page1_elements["beg_date"].setVisible(True)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)
            

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            # self.page2_elements["rep_num"].setVisible(False)
            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)
            # self.page2_elements["num_per"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

        elif self.page1_elements["select_table2"].isChecked():

            self.page1_elements["per_num"].setVisible(True)
            self.page1_elements["f_l_p"].setVisible(True)
            self.page1_elements["post"].setVisible(True)
            self.page1_elements["skill_level"].setVisible(True)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            # self.page2_elements["rep_num"].setVisible(False)
            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)


            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

        elif self.page1_elements["select_table3"].isChecked():

            self.page1_elements["num_of_pr"].setVisible(True)
            self.page1_elements["per_num1"].setVisible(True)
            self.page1_elements['price'].setVisible(True)
            self.report_all_pr.setVisible(True)
            self.finish_checkbox.setVisible(True)
            self.finish_text.setVisible(True)
            self.finish_button.setVisible(True)

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            # self.page2_elements["rep_num"].setVisible(False)
            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)
            # self.page2_elements["num_per"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

        elif self.page1_elements["select_table4"].isChecked():

            self.page1_elements["dif_num"].setVisible(True)
            self.page1_elements["proj_dif"].setVisible(True)
            self.page1_elements["al_coef"].setVisible(True)

            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.page1_elements["cus_num"].setVisible(False)
            self.page1_elements["customer"].setVisible(False)
            self.page1_elements["n_n_t"].setVisible(False)
            self.page1_elements["charge"].setVisible(False)
            self.page1_elements["charge_text"].setVisible(False)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
        
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            # self.page2_elements["rep_num"].setVisible(False)
            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)
            # self.page2_elements["num_per"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

        elif self.page1_elements["select_table5"].isChecked():

            self.page1_elements["cus_num"].setVisible(True)
            self.page1_elements["customer"].setVisible(True)
            self.page1_elements["n_n_t"].setVisible(True)
            self.page1_elements["charge"].setVisible(True)
            self.page1_elements["charge_text"].setVisible(True)

            self.page1_elements["per_num"].setVisible(False)
            self.page1_elements["f_l_p"].setVisible(False)
            self.page1_elements["post"].setVisible(False)
            self.page1_elements["skill_level"].setVisible(False)

            self.page1_elements["num_of_pr"].setVisible(False)
            self.page1_elements["per_num1"].setVisible(False)
            self.page1_elements['price'].setVisible(False)
            self.report_all_pr.setVisible(False)
            
            self.finish_checkbox.setVisible(False)
            self.finish_text.setVisible(False)
            self.finish_button.setVisible(False)

            self.page1_elements["dif_num"].setVisible(False)
            self.page1_elements["proj_dif"].setVisible(False)
            self.page1_elements["al_coef"].setVisible(False)

            # self.page1_elements["number"].setVisible(False)
            self.page1_elements["name"].setVisible(False)
            self.page1_elements["num_of_cus"].setVisible(False)
            self.page1_elements["proj_men_num"].setVisible(False)
            self.page1_elements["dur_of_ex"].setVisible(False)
            self.page1_elements["dif_cat"].setVisible(False)
            self.page1_elements["beg_date"].setVisible(False)

            self.page2_elements["per_num2"].setVisible(False)
            self.page2_elements["bank_num"].setVisible(False)
            # self.page2_elements["wage"].setVisible(False)

            # self.page2_elements["num_of_deb"].setVisible(False)
            self.page2_elements["cuss_num"].setVisible(False)
            self.page2_elements["am_of_deb"].setVisible(False)
            self.button_report_debt.setVisible(False)
            self.date_checkbox.setVisible(False)

            self.page2_elements["post"].setVisible(False)
            self.page2_elements["h_p_r"].setVisible(False)
            self.page2_elements["all_r"].setVisible(False)

            # self.page2_elements["rep_num"].setVisible(False)
            self.page2_elements["project_num"].setVisible(False)
            self.page2_elements["changes"].setVisible(False)
            self.page2_elements["hours"].setVisible(False)
            self.page2_elements["num_per"].setVisible(False)
            self.rep_month.setVisible(False)

            self.page2_elements["per_num_3"].setVisible(False)
            self.page2_elements["position"].setVisible(False)
            self.page2_elements["status"].setVisible(False)
            # self.page2_elements["num_per"].setVisible(False)

            self.button_1.setVisible(True)
            self.button_2.setVisible(False)
            self.button_1_2.setVisible(False)
            self.dismissal.setVisible(False)

            self.date_debt.setVisible(False)
            # self.update.setVisible(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
