
import json
import time

import pandas as pd
from dotenv import load_dotenv


from MyDashboard import MyDashboard
from NotionClient import NotionClient

load_dotenv()


if __name__ == '__main__':

    # https://www.notion.so/9462e15053ff4bbc871ad7ab91d9f145?v=632479bcc69b41ce8ff355d5c72dcdfb
    # https://www.notion.so/812372d76eb4492f81089f79f3cddefa?v=aed9d7af707b4527a37fda7295ec7a34
    # https://www.notion.so/eeee053ef4ec44e6a666382bd54a1b39?v=2ad8662f2b2a465186d8854289950e9b
    # https://www.notion.so/812372d76eb4492f81089f79f3cddefa?v=aed9d7af707b4527a37fda7295ec7a34
    start = time.process_time()
    database_id = "812372d76eb4492f81089f79f3cddefa"

    my_dashboard = MyDashboard(['4725', '4731', '4732'])
    notion_client = NotionClient()

    my_dashboard.set_page_id_to_student(database_id)
    students = my_dashboard.get_students()

    #students_progress = my_dashboard.get_students_progress()
    ''' notion_db = notion_client.get_property_value_per_page(
        "1a5d64eae4e74b78bff334e6d3733282", "Completion Rate")

    # https://www.notion.so/Abdallah-1a5d64eae4e74b78bff334e6d3733282
    add_completion_rate_payload = {"properties": {"Completion Rate":
                                                  {
                                                      "type": "number",
                                                      "number": 4
                                                  }
                                                  }}
    notion_client.update_property(
        "1a5d64eae4e74b78bff334e6d3733282", add_completion_rate_payload)
    print(json.dumps(notion_db, indent=4)) '''

    #print(json.dumps(all_pages_in_db, indent=4,))

    print(json.dumps(students, indent=4))

    print("--- %s seconds ---" % (time.process_time() - start))

    #print(json.dumps(students, indent=4))
