from dotenv import load_dotenv
import os
import requests
load_dotenv()


class NotionClient:

    headers = {
        "Accept": "application/json",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + os.environ["NOTION_INTEGRATION_API_KEY"]
    }

    def __init__(self):
        super(NotionClient, self).__init__()

    def send_get_request(self, url):
        response = requests.patch(url, headers=self.headers)
        return response.json()

    def send_post_request(self, url, payload):
        response = requests.patch(url, json=payload, headers=self.headers)
        return response.json()
