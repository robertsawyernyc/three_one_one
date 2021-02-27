import os
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
ROOT_URL = os.getenv("ROOTURL")
APP_TOKEN = os.getenv("APPTOKEN")


# DB_NAME=three_one_one_development
# DB_HOST=#RDS instance endpoint
# DB_USER=postgres
# DB_PASSWORD=secretsecret
# DEBUG=True
# TESTING=True
# APPTOKEN=MBBwwZPyrrn0xWRNWk4X8qRWK
# ROOTURL=https://data.cityofnewyork.us/resource/erm2-nwe9.json