import psycopg2
from api.src.db import *
from api.src.models import *

cursor = conn_dev.cursor()
drop_all_tables(conn_dev, cursor)

agency_one = save(Agency(agency = 'NYPD', agency_name = 'New York Police Department'), conn_dev, cursor)
agency_two = save(Agency(agency = 'DOHMH', agency_name = 'Department of Health and Mental Hygiene'), conn_dev, cursor)
agency_three = save(Agency(agency = 'DSNY', agency_name = 'Department of Sanitation'), conn_dev, cursor)


complaint_one = save(Complaint(complaint_type = 'noise - residential', descriptor = 'banging/pounding', agency_id = agency_one.id), conn_dev, cursor)
complaint_two = save(Complaint(complaint_type = 'food poisoning', descriptor = '3 or more', agency_id = agency_two.id), conn_dev, cursor)
complaint_three = save(Complaint(complaint_type = 'graffiti', descriptor = 'graffiti', agency_id = agency_three.id), conn_dev, cursor)


location_one = save(Location(setting = 'street/sidewalk', zip_code = 11435, incident_address = '123 main street', city = 'jamaica',
                        borough = 'queens', latitude = 40.70179721060235, longitude = -73.80873372239624), conn_dev, cursor)
location_two = save(Location(setting = 'restaurant/bar/deli/bakery', zip_code = 11231, incident_address = '456 bond street', city = 'brooklyn',
                        borough = 'brooklyn', latitude = 40.6871015496339, longitude = -73.97536548565982), conn_dev, cursor)
location_three = save(Location(setting = 'residentail building/house', zip_code = 10021, incident_address = '789 fifth avenue', city = 'new york',
                        borough = 'manhattan', latitude = 40.82003081301524, longitude = -73.952850909447), conn_dev, cursor)


incident_one = save(Incident(open_data_id = '123456', complaint_id = complaint_one.id, location_id = location_one.id), conn_dev, cursor)
incident_two = save(Incident(open_data_id = '987654', complaint_id = complaint_two.id, location_id = location_two.id), conn_dev, cursor)
incident_three = save(Incident(open_data_id = '213243', complaint_id = complaint_two.id, location_id = location_three.id), conn_dev, cursor)

