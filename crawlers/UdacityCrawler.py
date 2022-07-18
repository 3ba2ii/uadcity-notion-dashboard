from json import JSONDecoder
from NotionClient import NotionClient
from graphQLClient import GraphQLClient
from graphql.queries.me_query import me_query
from graphql.queries.session import session_query


class UdacityCrawler:
    client = GraphQLClient()

    def __init__(self):
        super(UdacityCrawler, self).__init__()

    def me(self):
        return self.client.run_query(me_query, {})  # execute query

    def session(self, session_id):
        return self.client.run_query(session_query, {'id': session_id})

    def get_students_per_session(self, session_id):
        session = self.session(session_id)
        members = session['data']['session']['members']
        students = {member["student"]["key"]: member
                    for member in members}

        return students

    def get_students_per_session_with_email_key(self, session_id):
        session = self.session(session_id)
        members = session['data']['session']['members']
        students = {member["student"]["email"]: member
                    for member in members}
        return students

    def get_students_for_my_sessions(self, session_ids):
        students = {}
        for session_id in session_ids:
            students.update(
                self.get_students_per_session_with_email_key(session_id))
        return students

    def update_students_content_on_notion(self, notion_client: NotionClient, database_id: str, session_ids: list[str],):
        notion_db = notion_client.get_pages_per_database(
            database_id, {"page_size": 100})

        students = self.get_students_for_my_sessions(session_ids)

        for page in notion_db['results']:
            # get page data
            page_id = page['id']
            student_email = notion_client.get_property_data_per_page(
                page_id, 'Email')['email']
            if not student_email:
                continue
            student_key = students[student_email]['student']['key']
            updated_property_content = {"properties": {"ID": [
                {
                    "plain_text": "{key}".format(key=student_key),
                    "type": "text",
                    "text": {"content": "{key}".format(key=student_key)}

                }]}}
            res = notion_client.update_property(
                page_id, updated_property_content)
            print(res)
