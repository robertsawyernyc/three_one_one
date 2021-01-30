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


