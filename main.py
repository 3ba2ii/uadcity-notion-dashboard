
import time

from dotenv import load_dotenv

from Inquirer import Inquirer
from MyDashboard import MyDashboard

load_dotenv()


if __name__ == '__main__':

    print('--- Started the script ---')

    start = time.process_time()
    my_dashboard = MyDashboard(['5025', '5026'])

    inq = Inquirer(my_dashboard)
    #inq.execute_command('I want to update my students\'s progress on notion')

    print('✅ Finished in: ', time.process_time() - start)
