import api.src.models as models
import api.src.db as db
import api.src.adapters as adapters
import psycopg2


class RequestAndBuild:
    def __init__(self):
        self.client = adapters.Client()
        self.builder = adapters.Builder()
        self.conn = psycopg2.connect(database = 'three_one_one_development', 
                user = 'robertsawyer')
        self.cursor = self.conn.cursor()

    def run(self, search_params):
        incidents = self.client.request_incidents(search_params) #hit api and retrieves json files
        open_data_ids = [incident['open_data_id'] for incident in incidents]
        incident_objs = []
        for open_data_id in open_data_ids:
            incident_details = self.client.request_incidents()
            incident_obj = self.builder.run(incident_details, self.conn, self.cursor)
            incident_objs.append(incident_obj)
        return incident_objs

