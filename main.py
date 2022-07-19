
import json
import time

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

    print('--- Started the script ---')
    my_dashboard = MyDashboard(['4725', '4731', '4732'])
    # print(my_dashboard.print_json(my_dashboard.get_students()))
    student_key = my_dashboard.get_student_key_with_email(
        'abdelaty.magdi@gmail.com')
    print(student_key)
    #inq = Inquirer(my_dashboard)
    #inq.execute_command('I want to update my students\'s progress on notion')
