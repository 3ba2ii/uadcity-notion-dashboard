import json
from concurrent.futures import ThreadPoolExecutor

from crawlers.UdacityCrawler import UdacityCrawler
from NotionClient import NotionClient
from joblib import Parallel, delayed


class MyDashboard:
    students = {}
    sessions = []

    def __init__(self, sessions: list[str]):
        self.notion_client = NotionClient()
        self.udacity_client = UdacityCrawler()
        self.sessions = sessions
        print('--- Started loading students ---')
        self.students = self.udacity_client.get_students_for_my_sessions(
            sessions)

        self.set_students_progress()
        print('--- Finished loading students ---')

    def get_students(self):
        return self.students

    def get_student_completion_rate(self,  session_id: str, student_key: str):
        completion_rate = self.udacity_client.get_student_completion_rate_for_part(
            session_id, student_key, 1)
        return {student_key: completion_rate}  # 1 is the part index

    def set_students_progress(self):
        res = Parallel(-1)(delayed(self.get_student_completion_rate)(self.students[student_key]['enrollment']['session_id'],
                                                                     student_key)for student_key in self.students)
        for single_res in res:
            student_key = list(single_res.keys())[0]
            self.add_property_to_student(
                student_key, 'completion_rate', single_res[student_key])
            # self.students_progress.update(single_res)

    def get_student_progress(self, student_key: str):
        return self.students[student_key]['completion_rate']

    def add_property_to_student(self, student_key: str, property_name: str, property_value: str):
        self.students[student_key][property_name] = property_value

    def set_page_id_to_students(self, database_id: str):
        print('Started setting page id to students')
        all_pages_in_db = self.notion_client.get_pages_per_database(database_id, {})[
            'results']
        for page in all_pages_in_db:
            page_id = page['id']
            page_property_data = self.notion_client.get_property_value_per_page(
                page_id, 'ID')
            student_key = page_property_data['results'][0]['rich_text']['text']['content']
            self.add_property_to_student(student_key, 'page_id',  page_id)

        print('Finished setting page id to students')

    def update_student_progress(self, student: dict):
        page_id = student['page_id']
        completion_rate = student['completion_rate']
        completion_rate_payload = {"properties": {"Completion Rate":
                                                  {
                                                      "type": "number",
                                                      "number": completion_rate
                                                  }
                                                  }}
        self.notion_client.update_property(
            page_id, completion_rate_payload)

    def update_students_progress(self):
        print('Started updating students progress')

        Parallel(-1)(delayed(self.update_student_progress)(student)
                     for _, student in self.students.items())

        print('Finished updating students progress')

    def print_json(self, json_object: json):
        print(json.dumps(json_object, indent=4, ))
