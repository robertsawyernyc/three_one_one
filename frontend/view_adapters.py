def get_borough_names(incident_details):
    return [borough['borough'] for borough in incident_details]

def get_agency_complaint_counts(incident_details):
    return []

def get_agency_names(incident_detailss):
    return [agency['agency_name'] for agency in incident_details]

def get_type_of_complaints(incident_details):
    return [complaint['complaint_type'] for complaint in incident_details]

agency_data = go.Bar({'x': get_agency_names(incidents),
                 'y': get_agency_complaint_counts(agency)}, name= 'Incidents by Agency')
agency_layout = go.Layout(title = 'Most Utilized Agencies')
fig = go.Figure(data = agency_data, layout = agency_layout) 
go.plot(fig)

# the next 3 methods used for mapping location of incidents
def incident_locations(incidents):
    return [location['location'] for location in incidents]

def get_lat_long(location):
    get_coordinates = [location.get(k) for k in ['latitude', 'longitude', 'human_address']]
    return get_coordinates[:2]

def get_lat_longs(locations):
    return [get_lat_long(location) for location in locations]

# data = [go.Bar(x = get_agency_names.index, y = agency_name.values, name = 'Most Utilized Agency')]
# layout = go.Layout(title = 'Most Utilized Agency')
# fig = go.Figure(data = data, layout = layout)
# go.plot(fig)

# scatter = go.Scatter(x = venue_names(venues, True), 
#         y = venue_ratings(venues, True), 
#         hovertext = venue_names(venues, True), mode = 'markers')

# locations = venue_locations(venues)