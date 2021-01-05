import api.src.models as models
import api.src.db as db
import api.src.adapters as adapters
import psycopg2


class Builder:
    def run(self, incident_details, conn, cursor):
        incident = IncidentBuilder().run(incident_details, conn, cursor)
        if incident.exists:
            return {'incident': incident, 'location': incident.location(cursor), 
                    'complaint': incident.complaint(cursor)}
        else:
            location = LocationBuilder().run(incident_details, conn, cursor)
            complaint = ComplaintBuilder().run(incident_details, conn, cursor)
            return {'incident': incident, 'location': location, 'complaint': complaint}


class IncidentBuilder:
    attributes = ['open_data_id', 'date_time']

    def select_attributes(self, incident_details):
        open_data_id = incident_details['unique_key']
        date_time = incident_details['created_date']
        return dict(zip(self.attributes, [open_data_id, date_time]))

    def run(self, incident_details, conn, cursor):
        selected = self.select_attributes(incident_details)
        open_data_id = selected['unique_key']
        incident = models.Incident.find_by_open_data_id(open_data_id, cursor)
        if incident:
            incident_details.exists = True
            return incident_details
        else:
            incident_details = db.save(models.Incident(**selected), conn, cursor)
            incident.exists = False
            return incident


class LocationBuilder:
    attributes = ['setting', 'zip_code', 'incident_address', 'city', 
    'borough', 'latitude', 'longitude']

    def select_attributes(self, incident_details):
        setting = incident_details['location_type']
        zip_code = incident_details['incident_zip']
        incident_address = incident_details['incident_address']
        city = incident_details['city']
        borough = incident_details['borough']
        latitude = incident_details['latitude']
        longitude = incident_details['longitude']
        return dict(zip(self.attributes, [setting, zip_code, incident_address,
        city, borough, latitude, longitude]))

    def run(self, incident_details, conn, cursor):
        location_attributes = self.select_attributes(incident_details)
        location = models.Location(**location_attributes)
        location = db.save(location, conn, cursor)
        return location


class ComplaintBuilder:
    def select_attributes(self, incident_details):
        complaints = [complaint['complaint_type'] for complaint in incident_details]
        return complaints

    def run(self, incident_details, conn, cursor):
        complaint_types = self.select_attributes(incident_details)
        complaints = self.find_or_create_complaint_types(complaint_types, conn, cursor)

    def find_or_create_complaint_types(self, complaint_types, conn, cursor):
        type_of_complaints =[]
        for type in complaint_types:
            complaint_type = db.total_by_complaint_type(models.Complaint, conn, cursor
            type_of_complaints.append(complaint_type)
        return type_of_complaints
        

        

incident_json = {'unique_key': '42033602', 'created_date': '2019-03-24T00:00:00.000', 'closed_date': '2019-03-27T00:00:00.000',
 'agency': 'DOHMH', 'agency_name': 'Department of Health and Mental Hygiene', 'complaint_type': 'Rodent',
  'descriptor': 'Rat Sighting', 'location_type': '3+ Family Apt. Building', 'incident_zip': '11372',
   'incident_address': '91-11 34 AVENUE', 'street_name': '34 AVENUE', 'cross_street_1': '91 STREET',
    'cross_street_2': '92 STREET', 'address_type': 'ADDRESS', 'city': 'Jackson Heights', 'facility_type': 'N/A',
     'status': 'Closed', 'due_date': '2019-04-23T00:36:15.000',
      'resolution_description': 'The Department of Health and Mental Hygiene will review your complaint to determine appropriate action. Complaints of this type usually result in an inspection. Please call 311 in 30 days from the date of your complaint for status',
       'resolution_action_updated_date': '2019-03-27T00:00:00.000', 'community_board': '03 QUEENS', 'borough': 'QUEENS',
        'x_coordinate_state_plane': '1018477', 'y_coordinate_state_plane': '214237', 'open_data_channel_type': 'PHONE',
         'park_facility_name': 'Unspecified', 'park_borough': 'QUEENS', 'latitude': '40.7546413', 'longitude': '-73.8764607',
          'location': {'latitude': '40.7546413', 'longitude': '-73.8764607', 'human_address': '{"address": "", "city": "", "state": "", "zip": ""}'}} 

# python3 -i console.py
# >>> builder = IncidentBuiler()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'IncidentBuiler' is not defined
# >>> builder = IncidentBuilder()
# >>> builder.select_attributes(incident_json)
# {'unique_key': '42033602', 'created_date': '2019-03-24T00:00:00.000', 'closed_date': '2019-03-27T00:00:00.000'}          
