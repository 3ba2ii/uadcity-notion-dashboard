import json
import os

import pandas as pd
import requests
from dotenv import load_dotenv

from graphql.queries.me_query import me_query
from graphql.queries.session import session_query
from graphQLClient import GraphQLClient

load_dotenv()


if __name__ == '__main__':
    client = GraphQLClient()

    client.session('4725')
