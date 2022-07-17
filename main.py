
import os
from turtle import title

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

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ["NOTION_INTEGRATION_API_KEY"]
    }

    notion_client = NotionClient()
    response = notion_client.send_post_request(url, payload)

    print(response) '''
    ''' notion_client = NotionClient(token_v2=os.environ["NOTION_TOKEN"])
    page = notion_client.get_block(
        "https://www.notion.so/6fb1272f6bdf43ffb0af8ae38ca4d43c?v=b1f9e0250e8a4f2b83a01a3400bdfaba")

    print("The old title is:", page.title) '''
    client = UdacityCrawler()
    print(client.me())
