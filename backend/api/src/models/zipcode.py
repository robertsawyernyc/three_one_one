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

    @classmethod
    def find_by_code(self, code, cursor):
        query = f"""SELECT * FROM {self.__table__} WHERE code = %s """
        cursor.execute(query, (code,))
        record =  cursor.fetchone()
        obj = db.build_from_record(self, record)
        return obj

    def locations(self, cursor):
        query_str = "SELECT locations.* FROM locations WHERE zipcode_id = %s"
        cursor.execute(query_str, (self.id,))
        records = cursor.fetchall()
        return db.build_from_records(models.Location, records)

    def borough(self, cursor):
        query_str = "SELECT boroughs.* FROM boroughs WHERE id = %s"
        cursor.execute(query_str, (self.borough_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Borough, record)