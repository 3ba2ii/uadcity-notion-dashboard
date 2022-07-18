
import json
import time

import pandas as pd
from dotenv import load_dotenv
from Inquirer import Inquirer


from MyDashboard import MyDashboard
from NotionClient import NotionClient
from joblib import Parallel, delayed

load_dotenv()


if __name__ == '__main__':

    # https://www.notion.so/9462e15053ff4bbc871ad7ab91d9f145?v=632479bcc69b41ce8ff355d5c72dcdfb
    # https://www.notion.so/812372d76eb4492f81089f79f3cddefa?v=aed9d7af707b4527a37fda7295ec7a34
    # https://www.notion.so/eeee053ef4ec44e6a666382bd54a1b39?v=2ad8662f2b2a465186d8854289950e9b
    # https://www.notion.so/812372d76eb4492f81089f79f3cddefa?v=aed9d7af707b4527a37fda7295ec7a34
    # https://www.notion.so/eeee053ef4ec44e6a666382bd54a1b39?v=2ad8662f2b2a465186d8854289950e9b
    database_id = "eeee053ef4ec44e6a666382bd54a1b39"

    ''' my_dashboard = MyDashboard(['4725', '4731', '4732'])

    start = time.process_time()

    print('Getting notion pages...')
    my_dashboard.set_page_id_to_student(database_id)

    print('Notion Pages loaded in: ', time.process_time() - start)

    students = my_dashboard.get_students()

    print('Updating student progress in notion...')
    my_dashboard.update_students_progress()
    print('Student progress updated in notion!')

    print("--- %s seconds ---" % (time.process_time() - start)) '''

    my_dashboard = MyDashboard(['4725', '4731', '4732'])
    Inquirer(my_dashboard)

    #print(json.dumps(students, indent=4))
