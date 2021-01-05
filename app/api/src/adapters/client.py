import requests
class Client:
    ROOT_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    

    def full_url(self, begin_date, end_date):
        url = f"""{Client.ROOT_URL}?$where=created_date
         between '{begin_date}' and '{end_date}'"""
        return url

    def request_incidents(self, begin_date = '2019-03-24', end_date = '2019-03-31'):
        url = self.full_url(begin_date, end_date)
        response = requests.get(url)
        return response.json()

# {'unique_key': '42033602', 'created_date': '2019-03-24T00:00:00.000', 'closed_date': '2019-03-27T00:00:00.000',
#  'agency': 'DOHMH', 'agency_name': 'Department of Health and Mental Hygiene', 'complaint_type': 'Rodent',
#   'descriptor': 'Rat Sighting', 'location_type': '3+ Family Apt. Building', 'incident_zip': '11372',
#    'incident_address': '91-11 34 AVENUE', 'street_name': '34 AVENUE', 'cross_street_1': '91 STREET',
#     'cross_street_2': '92 STREET', 'address_type': 'ADDRESS', 'city': 'Jackson Heights', 'facility_type': 'N/A',
#      'status': 'Closed', 'due_date': '2019-04-23T00:36:15.000',
#       'resolution_description': 'The Department of Health and Mental Hygiene will review your complaint to determine appropriate action. Complaints of this type usually result in an inspection. Please call 311 in 30 days from the date of your complaint for status',
#        'resolution_action_updated_date': '2019-03-27T00:00:00.000', 'community_board': '03 QUEENS', 'borough': 'QUEENS',
#         'x_coordinate_state_plane': '1018477', 'y_coordinate_state_plane': '214237', 'open_data_channel_type': 'PHONE',
#          'park_facility_name': 'Unspecified', 'park_borough': 'QUEENS', 'latitude': '40.7546413', 'longitude': '-73.8764607',
#           'location': {'latitude': '40.7546413', 'longitude': '-73.8764607', 'human_address': '{"address": "", "city": "", "state": "", "zip": ""}'}}

# import requests
# from flask import Flask

# class Client:
#     APP_TOKEN = '1tNkT6rxKKvprTlBlhQWK3t2V'
#     ROOT_URL ="https://data.cityofnewyork.us/resource/2fra-mtpn.json"

#     def auth_params(self):
#         return {'$$app_token':self.APP_TOKEN}

#     def full_params(self, query_params = {'$limit':100000,'BORO_NM': 'MANHATTAN', 'OFNS_DESC': 'PETIT LARCENY'}):
#         params = self.auth_params().copy()
#         params.update(query_params)
#         return params

#     def request_incidents(self, query_params = {'$limit':100000,'BORO_NM': 'MANHATTAN', 'OFNS_DESC': 'PETIT LARCENY'}):
#         return requests.get(f'{self.ROOT_URL}', self.full_params(query_params)).json()