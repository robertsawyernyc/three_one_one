import streamlit as st
import requests
import numpy as np
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('311_Service_Requests_from_2010_to_Present.csv')
items = ['incidents', 'complaints', 'agency_names']
dataset = df.groupby[items]

index = np.arange(len(items))
label = np.arange()
num_of_incidents = list(dataset.T['incidents'])
num_of_complaints = list(dataset.T['complaints'])
num_of_agency_names = list(dataset.T['agency_names'])

bar_width = 0.35

fig, ax = plt.subplots()
incidents_bar = ax.bar(index, num_of_incidents, bar_width, label='Incidents')
complaints_bar = ax.bar(index, num_of_complaints, bar_width, label='Complaints')
agency_names_bar = ax.bar(index, num_of_agency_names, bar_width, label='Agency Names')

ax.set_xticks(index)
ax.set_xticklabels(incident_details) 

ax.set_yticks(numb)

plt.show()


API_URL = "http://127.0.0.1:5000/incidents/search"


def find_incidents(borough):
    response = requests.get(API_URL, params = {'borough' : borough})
    return response.json()

def find_complaints(complaint_type):
    response = requests.get(API_URL, params = {'complaint_type': complaint_type})
    return response.json()

def find_by_agencies(agency_name):
    reponse = requests.get(API_URL, params = {'agency_name': agency_name})
    return reponse.json()


st.header('Incidents')
st.write('Here are locations of NYC 311 Service Requests')
incidents = incident_locations(incidents)

def incident_locations(incidents):
    return [incident['latitude', 'longitude'] for incident in incidents 
    if incident.get(('latitude', 'longitude'))]

scatter = go.Scatter(x = find_complaints(incidents, True),
        y = number_of_complaints


# def incident_locations(incidents):
#     center = [40.730610, -73.935242]
#     map_nyc = folium.Map(location = center, zoom_start = 8)
#     for index, incident in incidents.iterrows():
#         location = [incident['latitude'], incident['longitude']]
#         folium.Marker(location, popup = f'Name: {incident["complaint type"]}').add_to(map_nyc)
#     return map_nyc.save('index.html')



incidents_df = pd.DataFrame(incidents)

st.map(incidents_df)

def borough_names(boroughs):
    return [borough['borough'] for borough in boroughs]

def agency_names(agencies):
    return [agency['agency_name'] for agency in agencies]

def type_of_complaints(incidents):
    return [type['complaint_type'] for type in incidents]

# def venue_locations(venues):
#     return [venue['location'] for venue in venues if venue.get('location') ]

data = [go.Bar(x = agency_name.index, y = agency_name.values, name = 'Most Utilized Agency')]
layout = go.Layout(title = 'Most Utilized Agency')
fig = go.Figure(data = data, layout = layout)
go.plot(fig)

# scatter = go.Scatter(x = venue_names(venues, True), 
#         y = venue_ratings(venues, True), 
#         hovertext = venue_names(venues, True), mode = 'markers')

# locations = venue_locations(venues)


# fig = go.Figure(scatter)
# st.plotly_chart(fig)
# st.map(pd.DataFrame(locations))