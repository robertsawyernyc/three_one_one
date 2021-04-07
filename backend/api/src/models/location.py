from api.src.db import db
import api.src.models as models

class Location:
    __table__ = 'locations'
    columns = ['id', 'setting', 'incident_address',
             'latitude', 'longitude', 'zipcode_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod    
    def total_incidents_by_setting(self, cursor):
        setting_query = """SELECT setting, COUNT(*) FROM locations 
        JOIN incidents ON locations.id = incidents.location_id
        GROUP BY setting"""
        cursor.execute(setting_query)
        records = cursor.fetchall()
        return records

    def incidents(self, cursor):
        query_str = "SELECT * FROM incidents WHERE id = %s"
        cursor.execute(query_str, (self.venue_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Incident, record)

    def zipcode(self, cursor):
        query_str = "SELECT * FROM zipcodes WHERE id = %s"
        cursor.execute(query_str, (self.zipcode_id,))
        record = cursor.fetchone()
        return db.build_from_record(models.Zipcode, record)





