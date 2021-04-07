from flask import Flask, request 
import simplejson as json
import api.src.models as models
import api.src.db as db
# controller file
# sets default args for running the app
def create_app(
    database = 'three_one_one_development', 
    testing = False, 
    debug = True):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE = database,
        DEBUG = debug,
        TESTING = testing
    )

    @app.route('/')
    def root_url():
        return 'Welcome to NYC 311 Service Requests API'

    @app.route('/incidents') 
    def incidents():
        conn = db.get_db()
        cursor = conn.cursor()

        incidents = db.find_all(models.Incident, cursor)
        incident_dicts = [incident.__dict__ for incident in incidents]
        return json.dumps(incident_dicts, default = str)

    @app.route('/boroughs')
    def boroughs():
        conn = db.get_db()
        cursor = conn.cursor()

        boroughs = models.Location.total_incidents_by_borough(cursor)
        borough_dicts = [borough.__dict__ for borough in boroughs]
        return json.dumps(borough_dicts, default = str)

    @app.route('/settings')
    def settings():
        conn = db.get_db()
        cursor = conn.cursor()

        settings = models.Location.total_incidents_by_setting(cursor)
        settings_dicts = [setting.__dict__ for setting in settings]
        return json.dumps(setting_dicts, default = str)

    @app.route('/zipcodes')
    def zip_codes():
        conn = db.get_db()
        cursor = conn.cursor()

        zip_codes = models.Location.total_incidents_by_zip_code(cursor)
        zip_code_dicts = [zip_code.__dict__ for zip_code in zip_codes]
        return json.dumps(zip_code_dicts, default = str)

    @app.route('/agencies')
    def agencies():
        conn = db.get_db()
        cursor = conn.cursor()

        agencies = models.Agency.total_complaints_by_agency(cursor)
        agency_dicts = [agency.__dict__ for agency in agencies]
        return json.dumps(agency_dicts, default = str)

    @app.route('/incidents/<id>') 
    def incident(id):
        conn = db.get_db()

        cursor = conn.cursor()
        incident = db.find(models.Incident, id, cursor)
        return json.dumps(incident.__dict__, default = str)

    return app 