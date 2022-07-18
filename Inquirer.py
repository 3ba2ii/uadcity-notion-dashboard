import inquirer
from MyDashboard import MyDashboard

database_id = "eeee053ef4ec44e6a666382bd54a1b39"


class Inquirer:

    def __init__(self, dashboard: MyDashboard):
        self.dashboard = dashboard
        self.questions = [
            inquirer.List('command',
                          message="What do you want to do?",
                          choices=[
                              'I want to update my students\'s progress on notion'],
                          ),
        ]

        self.answers = inquirer.prompt(self.questions)

        self.commands_to_execute = {
            'I want to update my students\'s progress on notion':
                [{"fn": self.dashboard.set_page_id_to_students, "args": [database_id]},
                 {"fn": self.dashboard.update_students_progress, "args": []}]}

        self.execute_command(self.answers['command'])

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
