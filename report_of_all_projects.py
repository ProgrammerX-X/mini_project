import os
import json
from dismissal import connector

def all_projects_report(db_name):
    way_to_save = "../mini_project/reports"
    try:
        _, cursor = connector(db_name)

        cursor.execute("""
        SELECT 
            PIP.PERFORMER_NUMBER AS "Performer Number",
            PR.DIFFICULTY_CATEGORY AS "Difficulty Category",
            COUNT(PIP.NUMBER_OF_PROJECT) AS "Project Count by Category",
            'Total finished projects: ' || SUM(COUNT(PIP.NUMBER_OF_PROJECT)) OVER (PARTITION BY PIP.PERFORMER_NUMBER) AS "Total Finished Projects (Text)",
            GROUP_CONCAT(PIP.NUMBER_OF_PROJECT) AS "Finished Projects",
            'Performer ' || PIP.PERFORMER_NUMBER || ' completed ' || COUNT(PIP.NUMBER_OF_PROJECT) || 
            ' projects in category ' || PR.DIFFICULTY_CATEGORY AS "Summary Text"
        FROM 
            PROJECTS_IN_PROGRESS AS PIP
        JOIN 
            PROJECTS AS PR
        ON 
            PIP.NUMBER_OF_PROJECT = PR.NUMBER_OF_PROJECT
        WHERE 
            PIP.FINISH = 'Finished'
        GROUP BY 
            PIP.PERFORMER_NUMBER, PR.DIFFICULTY_CATEGORY;
        """)


        data = cursor.fetchall()

        # if not os.path.exists(data):
        #     os.mkdir(data)

        report_file = os.path.join(way_to_save, "all_projects_report.json")
        with open (report_file, "w") as file:
            json.dump(data, file, indent=4)
        return f"Report created correctly!"
    except Exception as e:
        return f"Error: {e}"

# response = 
all_projects_report("projects.db")
# print(response)
    # НАДХОДЖЕННЯ ОПЛАТИ + ГРУПУВАННЯ ЗА КАТЕГОРІЄЮ ВАЖКОСТІ