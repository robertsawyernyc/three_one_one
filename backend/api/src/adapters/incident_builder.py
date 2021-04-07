import api.src.models as models
import api.src.db as db
import api.src.adapters as adapters
import psycopg2


class Builder:
    def run(self, incident_details, conn, cursor): # takes in json details
        incident = IncidentBuilder().run(incident_details, conn, cursor)
        if incident.exists:
            return {'incident': incident, 'location': incident.location(cursor), 
                    'complaint': incident.complaint(cursor), 'agency' : incident.agency(cursor)}
        else:
            location = LocationBuilder().run(incident_details, conn, cursor)
            complaint = ComplaintBuilder().run(incident_details, conn, cursor)
            return {'incident': incident, 'location': location, 'complaint': complaint}


class IncidentBuilder:
    attributes = ['open_data_id', 'created_date', 'closed_date'] 
    
    def select_attributes(self, incident_details): 
        open_data_id = incident_details[0].get('unique_key', 'none')
        created_date = incident_details[0].get('created_date', 'none')
        closed_date = incident_details[0].get('closed_date', 'none')
        return dict(zip(self.attributes, [open_data_id, created_date, closed_date]))

    def run(self, incident_details, conn, cursor):
        selected = self.select_attributes(incident_details)
        open_data_id = selected[0].get('unique_key', 'none')
        incident = models.Incident.find_by_open_data_id(open_data_id, cursor)
        if incident:
            incident.exists = True
            return incident
        else:
            incident_details = db.save(models.Incident(**selected), conn, cursor)
            incident.exists = False
            return incident


class LocationBuilder:
    attributes = ['setting', 'incident_address',
             'latitude', 'longitude']

    def select_attributes(self, incident_details):
        setting = incident_details[0].get('location_type', 'none')
        incident_address = incident_details[0].get('incident_address', 'none')
        latitude = incident_details[0].get('latitude', 'none')
        longitude = incident_details[0].get('longitude', 'none')
        return dict(zip(self.attributes, [setting, incident_address,
                latitude, longitude]))

    def run(self, incident_details, conn, cursor):
        location_attributes = self.select_attributes(incident_details)
        location = models.Location(**location_attributes)
        location = db.save(location, conn, cursor)
        return location

    def find_or_create_by_borough_zip(self, borough_name = 'N/A', code = None, conn = None, cursor = None):
        if not borough_name: raise KeyError('must provide conn or cursor')
        borough = db.find_by_name(models.Borough, borough_name, cursor)
        zipcode = models.Zipcode.find_by_code(code, cursor)
        if not borough:
            borough = models.Borough(name = borough_name,)
            borough = db.save(borough, conn, cursor)
        if not zipcode:
            zipcode = models.Zipcode(code = code, borough_id = borough.id)
            zipcode = db.save(zipcode, conn, cursor)
        return borough, zipcode

    def build_location_borough_zip(self, location_attr, conn, cursor):
        borough_name = location_attr.pop('borough', 'N/A')
        code = location_attr.pop('incident_zip', None)
        borough, zipcode = self.find_or_create_by_borough_zip(borough_name, code, conn, cursor)
        location = models.Location(latitude = location_attr.get('latitude', None),
                longitude = location_attr.get('longitude', None),
                address = location_attr.get('incident_address', ''),
                zipcode_id = zipcode.id
                )
        return location


class ComplaintBuilder:
    def select_attributes(self, incident_details):
        complaints = [complaint['complaint_type'] for complaint in incident_details]
        return complaints

    def run(self, incident_details, conn, cursor):
        complaint_types = self.select_attributes(incident_details)
        complaints = self.find_or_create_complaint_types(complaint_types, conn, cursor)

    def find_or_create_complaint_types(self, incident_details, conn, cursor):
        type_of_complaints =[]
        for complaint_type in incident_details:
            named_complaint = db.total_by_complaint_type(models.Complaint, conn, cursor)
            type_of_complaints.append(named_complaint)
        return type_of_complaints