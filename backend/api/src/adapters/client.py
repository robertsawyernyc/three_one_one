import requests
from settings import APP_TOKEN, ROOT_URL

class Client:
    APP_TOKEN = APP_TOKEN
    ROOT_URL = ROOT_URL
    
    def auth_params(self):
        return {'$$app_token':self.APP_TOKEN}

    def full_params(self, begin_date = '2019-03-24', end_date = '2019-03-31', limit = 1000):
        params = self.auth_params().copy()
        query_params = {'$where': f"created_date between '{begin_date}' and '{end_date}'",
         '$limit': limit}
        params.update(query_params)
        return params

    def request_incidents(self, begin_date = '2019-03-24', end_date = '2019-03-31', limit = 1000):
        params = self.full_params(begin_date, end_date, limit)
        response = requests.get(Client.ROOT_URL, params)
        return response.json()

    

