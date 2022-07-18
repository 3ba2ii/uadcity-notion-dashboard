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
        response = requests.get(url, headers=self.headers)
        return response.json()

    def send_patch_request(self, url, payload):
        response = requests.patch(url, json=payload, headers=self.headers)
        return response.json()

    def send_post_request(self, url, payload):
        response = requests.post(url, json=payload, headers=self.headers)
        return response.json()

    def get_database(self, database_id: str):
        url = "https://api.notion.com/v1/databases/{database_id}".format(
            database_id=database_id)

        return self.send_get_request(url,)

    def get_pages_per_database(self, database_id: str, payload: dict):
        url = "https://api.notion.com/v1/databases/{database_id}/query".format(
            database_id=database_id)

        return self.send_post_request(url, payload)

    def get_page_data(self, page_id: str):
        url = "https://api.notion.com/v1/pages/{page_id}".format(
            page_id=page_id)

        return self.send_get_request(url)

    def get_block_data(self, block_id: str):
        url = "https://api.notion.com/v1/blocks/{block_id}".format(
            block_id=block_id)

        return self.send_get_request(url)

    def get_block_children_data(self, block_id: str):

        url = "https://api.notion.com/v1/blocks/{block_id}/children".format(
            block_id=block_id)

        return self.send_get_request(url)

    def get_property_data_per_page(self, page_id: str, property_id: str):

        url = "https://api.notion.com/v1/pages/{page_id}/properties/{property_id}".format(
            page_id=page_id, property_id=property_id)

        return self.send_get_request(url)

    def update_property(self, page_id, property: dict):
        url = "https://api.notion.com/v1/pages/{page_id}".format(
            page_id=page_id)

        return self.send_patch_request(url, property)
