from api.src.db import db
import api.src.models as models

class Zipcode:
    __table__ = 'zipcodes'
    columns = ['id', 'code', 'borough_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)