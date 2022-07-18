
import os
import json
import pandas as pd
import requests
from dotenv import load_dotenv
from NotionClient import NotionClient
from crawlers.UdacityCrawler import UdacityCrawler
from graphql.queries.me_query import me_query
from graphql.queries.session import session_query
from graphQLClient import GraphQLClient

load_dotenv()


def get_students_from_udacity_session(session_id: str):
    client = NotionClient()
    students = client.get_students()
    return students


if __name__ == '__main__':
    ''' url = "https://api.notion.com/v1/pages/58e20b2462e7466b9457fde02fa4d04d"

    payload = {"properties": {"title": [
        {
            "plain_text": "Hello World",
            "type": "text",
            "text": {"content": "Project Walkthrough"}

        }
    ]}}



    notion_client = NotionClient()
    response = notion_client.send_post_request(url, payload)

    print(response) '''
    ''' notion_client = NotionClient(token_v2=os.environ["NOTION_TOKEN"])
    page = notion_client.get_block(
        "https://www.notion.so/6fb1272f6bdf43ffb0af8ae38ca4d43c?v=b1f9e0250e8a4f2b83a01a3400bdfaba")

    print("The old title is:", page.title) '''
    ''' client = UdacityCrawler()
    students = client.get_students_per_session('4725')

    df = pd.DataFrame(students)
    print(df) '''

    # https://www.notion.so/9462e15053ff4bbc871ad7ab91d9f145?v=632479bcc69b41ce8ff355d5c72dcdfb
    # https://www.notion.so/812372d76eb4492f81089f79f3cddefa?v=aed9d7af707b4527a37fda7295ec7a34
    # https://www.notion.so/eeee053ef4ec44e6a666382bd54a1b39?v=2ad8662f2b2a465186d8854289950e9b
    notion_client = NotionClient()
    udacity_client = UdacityCrawler()
    udacity_client.update_students_content_on_notion(
        notion_client, "eeee053ef4ec44e6a666382bd54a1b39", ['4725', '4731', '4732'])
