
import time

from dotenv import load_dotenv
import inquirer

from Inquirer import Inquirer
from MyDashboard import MyDashboard
from utils.read_data_from_csv import read_emails_from_csv

load_dotenv()


if __name__ == '__main__':

    print('--- Started the script ---')

    start = time.process_time()
    '''  '''
    my_dashboard = MyDashboard(['4725', '4731', '4732'])

    ''' inquirer.Path('file_path', message='Please type the csv file path',
                  path_type=inquirer.Path.DIRECTORY)
    answers = inquirer.prompt([inquirer.Path('file_path', message='Please type the csv file path',
                                             path_type=inquirer.Path.DIRECTORY)]) '''

    # todo: add a method to create an attendance record if it doesn't exist
    inq = Inquirer(my_dashboard)
    #inq.execute_command('I want to update my students\'s progress on notion')

    print('Finished in: ', time.process_time() - start)
