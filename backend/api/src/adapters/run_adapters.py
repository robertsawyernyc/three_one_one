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

    def run(self, begin_date, end_date, limit):
        incidents = self.client.request_incidents(begin_date, end_date, limit) #hit api and retrieve json files
        open_data_ids = [incident['unique_key'] for incident in incidents]
        incident_objs = []
        for open_data_id in open_data_ids:
            incident_details = self.client.request_incidents()
            incident_obj = self.builder.run(incident_details, self.conn, self.cursor)
            incident_objs.append(incident_obj)
        return incident_objs

    # def run(self, begin_date, end_date, limit):
    #     incidents = self.client.request_incidents(begin_date, end_date, limit) #hit api and retrieve json files
    #     open_data_ids = [incident['unique_key'] for incident in incidents]
    #     incident_objs = []
    #     for open_data_id in open_data_ids:
    #         for incident in incidents:
    #             incident_detail = incident.get(open_data_id)
    #             incident_obj = self.builder.run(incident_detail, self.conn, self.cursor)
    #             incident_objs.append(incident_obj)
    #     return incident_objs

