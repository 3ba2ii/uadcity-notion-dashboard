
import os
import json
import time
import pandas as pd
import requests
from dotenv import load_dotenv
from MyDashboard import MyDashboard
from NotionClient import NotionClient
from crawlers.UdacityCrawler import UdacityCrawler
from graphql.queries.me import me_query
from graphql.queries.session import session_query
from graphQLClient import GraphQLClient
import inquirer

load_dotenv()


def get_students_from_udacity_session(session_id: str):
    client = NotionClient()
    students = client.get_students()
    return students


if __name__ == '__main__':

    # https://www.notion.so/9462e15053ff4bbc871ad7ab91d9f145?v=632479bcc69b41ce8ff355d5c72dcdfb
    # https://www.notion.so/812372d76eb4492f81089f79f3cddefa?v=aed9d7af707b4527a37fda7295ec7a34
    # https://www.notion.so/eeee053ef4ec44e6a666382bd54a1b39?v=2ad8662f2b2a465186d8854289950e9b
    my_dashboard = MyDashboard(['4725', '4731', '4732'])

    start = time.process_time()

    students = my_dashboard.get_students_progress()

    print("--- %s seconds ---" % (time.time() - start))

    #print(json.dumps(students, indent=4))
