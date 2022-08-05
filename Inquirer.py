import os
from dotenv import load_dotenv
import inquirer
from MyDashboard import MyDashboard
load_dotenv()

script_env = os.environ['SCRIPT_ENV']
database_id = os.environ['DATABASE_ID']


class Inquirer:

    def __init__(self, dashboard: MyDashboard):
        self.dashboard = dashboard

        self.questions = [
            inquirer.List('command',
                          message="What do you want to do?",
                          choices=[
                              'I want to update my students\'s progress on notion',
                              'I want to set attendance for my students on udacity\'s dashboard'],
                          ),
        ]
        self.answers = {"command": "", "session_idx": "",
                        "file_path": "", "state": ""}

        self.commands_to_execute = {
            'I want to update my students\'s progress on notion':
                [{"fn": self.dashboard.set_page_id_to_students, "args": [database_id]},
                 {"fn": self.dashboard.update_students_progress, "args": []},
                 ],
            'I want to set attendance for my students on udacity\'s dashboard':
                [{"fn": self.get_file_path_from_user, "args": []}, ],
        }

        if script_env and script_env == 'dev':
            self.answers.update(inquirer.prompt(self.questions))
            self.execute_command(self.answers['command'])
        else:
            # update students progress on notion
            self.dashboard.set_page_id_to_students(database_id)
            self.dashboard.update_students_progress()

    def get_file_path_from_user(self):
        self.question = [
            inquirer.Text(
                'session_idx', message='Please enter the index of the sessions',),

            inquirer.List('state',
                          message="What state do you want to set for these students?",
                          choices=['present', 'absent', 'excused'],
                          ),
        ]

        answers = inquirer.prompt(self.question)
        self.answers.update(answers)
        self.dashboard.set_attendance_for_session(
            self.answers['session_idx'],  self.answers['state']),

    def add_question(self, question):
        '''
        Add a question to the list of questions
        '''
        self.questions.append(question)

    def execute_command(self, command):
        steps = self.commands_to_execute[command]
        for step in steps:
            fn = step['fn']
            args = step['args']
            fn(*args)
