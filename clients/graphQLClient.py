import os

import requests
from dotenv import load_dotenv

load_dotenv()


class GraphQLClient:

    headers = {"Authorization": "Bearer " + os.environ["JWT_TOKEN"]}
    url = os.environ.get("REQUEST_URL")

    """docstring for graph"""

    def __init__(self):
        super(GraphQLClient, self).__init__()

    # A simple function to use requests.post to make the API call. Note the json= section.
    def run_query(self, query, variables):
        request = requests.post(self.url,
                                json={'query': query, 'variables': variables}, headers=self.headers)
        if request.status_code == 200:
            return request.json()

        raise Exception("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))
