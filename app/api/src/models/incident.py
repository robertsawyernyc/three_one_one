from api.src.db import db
import api.src.models as models

class Incident:
    __table__ = 'incidents'
    columns = ['id', 'open_data_id', 'date_time', 'location_id', 'complaint_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def total_complaints(self, cursor):
        complaint_query = """SELECT COUNT(*) FROM complaints"""
        cursor.execute(complaint_query)
        record = cursor.fetchall()
        return record

    @classmethod
    def find_by_open_data_id(self, cursor):
        open_data_id_query = """SELECT * FROM incidents WHERE open_data_id = %s"""
        cursor.execute(open_data_id_query, ('open_data_id', ))
        record =  cursor.fetchone()
        return db.build_from_record(models.Incident, record)



