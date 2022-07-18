import json
from concurrent.futures import ThreadPoolExecutor

from crawlers.UdacityCrawler import UdacityCrawler
from NotionClient import NotionClient
from joblib import Parallel, delayed


class MyDashboard:
    students = {}
    students_progress = {}
    sessions = []

    def __init__(self, sessions: list[str]):
        self.notion_client = NotionClient()
        self.udacity_client = UdacityCrawler()
        self.sessions = sessions
        self.students = self.udacity_client.get_students_for_my_sessions(
            sessions)

        self.print_json(self.students)
        self.set_students_progress()

    def get_students(self):
        return self.students

    def get_student_completion_rate(self,  session_id: str, student_key: str):
        return self.udacity_client.get_student_completion_rate_for_part(
            session_id, student_key, 1)  # 1 is the part index

    def set_students_progress(self):

        for student_key in self.students:
            print(student_key)
            student_session_id = self.students[student_key]['enrollment']['session_id']
            self.students_progress[student_key] = self.get_student_completion_rate(student_session_id,
                                                                                   student_key)

    def get_student_progress(self, student_key: str):
        return self.students_progress[student_key]

    def get_students_progress(self):
        return self.students_progress

    def print_json(self, json_object: json):
        print(json.dumps(json_object, indent=4, ))
