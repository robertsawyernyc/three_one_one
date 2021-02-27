import streamlit as st
import requests
import numpy as np
import plotly.offline as py
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt 
API_URL = "http://127.0.0.1:5000/incidents"
API_URL_AGENCIES = "http://127.0.0.1:5000/agencies"
API_URL_COMPLAINTS = "http://127.0.0.1:5000/complaints"

def get_incidents():
    response = requests.get(API_URL)
    return response.json()

def get_agencies():
    response = requests.get(API_URL_AGENCIES)
    return response.json()

def get_complaints():
    response = requests.get(API_URL_COMPLAINTS)
    return response.json()


st.header('Incidents')
st.write('Here are locations of NYC 311 Service Requests')


incidents = get_incidents()
coordinates = get_lat_longs(incidents)

#this is my map of incidents
df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
st.map(df)
