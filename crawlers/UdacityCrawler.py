from json import JSONDecoder
from graphQLClient import GraphQLClient
from graphql.queries.me_query import me_query
from graphql.queries.session import session_query


class UdacityCrawler:
    client = GraphQLClient()

    def __init__(self):
        super(UdacityCrawler, self).__init__()

    def me(self):
        return self.client.run_query(me_query, {})  # execute query

    def session(self, id):
        return self.client.run_query(session_query, {'id': id})
