from api.src.db import db
import api.src.models as models

class Agency:
    __table__ = 'agencies'
    columns = ['id', 'agency', 'agency_name']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)

    #calculates total complaints managed by each agency
    @classmethod
    def total_complaints_by_agency(self, cursor):
        agency_query = """SELECT agency_name, COUNT(*) FROM complaints 
        JOIN incidents ON complaints.id = incidents.complaint_id 
        GROUP BY agency_name"""
        cursor.execute(agency_query)
        record = cursor.fetchall()
        return record

    #calculates total by complaint type, example: NYPD -> will return {'name': 'NYPD', 'complaint_total': 500}
    @classmethod
    def complaint_type_total_by_agency(self, agency_name, cursor):
        complaint_total_query = """SELECT complaint_type, COUNT(*) FROM complaints 
        JOIN incidents ON complaints.id = incidents.complaint_id
        GROUP BY (complaint_type, agency_name) HAVING agency_name = %s"""
        cursor.execute(complaint_total_query,(agency_name,))
        record = cursor.fetchall()
        return record

    @classmethod
    def get_agency_name(self, name, cursor):
        agency_name_query = """SELECT * FROM complaits
        WHERE agency_name = %s"""
        cursor.execute(agency_name_query, (name,))
        agency_name_record = cursory.fetchone()
        agency_name = db.build_from_records(self, agency_name_record)
        return agency_name