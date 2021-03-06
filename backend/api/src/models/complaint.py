from api.src.db import db
import api.src.models as models

class Complaint:
    __table__ = 'complaints'
    columns = ['id', 'complaint_type', 'descriptor', 'agency_id']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise f'{key} not in {self.columns}' 
        for k, v in kwargs.items():
            setattr(self, k, v)


    @classmethod
    def find_by_complaint_type(self, name, cursor):
        complaint_query = """SELECT * FROM complaints 
        WHERE complaint_type = %s"""
        cursor.execute(complaint_query, (name,))
        complaint_records =  cursor.fetchall()
        complaints = db.build_from_records(self, complaint_records)
        return complaints 

    @classmethod
    def find_or_create_complaint_type(self, name, conn, cursor):
        complaints = self.find_by_complaint_type(name, cursor)
        if not complaints:
            new_complaint = models.Complaint()
            new_complaint.complaint_type = name
            db.save(new_complaint, conn, cursor)
            complaint = self.find_by_complaint_type(name, cursor)
        return complaint 

    #calculates complaint totals gourped by complaint type
    @classmethod
    def total_by_complaint_type(self, cursor):
        complaint_type_query = """SELECT complaint_type, COUNT(*) FROM complaints
        JOIN incidents ON complaints.id = incidents.complaint_id
        GROUP BY complaint_type"""
        cursor.execute(complaint_type_query)
        record = cursor.fetchall()
        return record

