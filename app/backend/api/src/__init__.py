from flask import Flask, request 
import simplejson as json
import api.src.models as models
import api.src.db as db

# sets default args for running the app
def create_app(database = 'three_one_one_development', testing = False, debug = True):
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

    @app.route('/agencies')
    def agencies():
        conn = db.get_db()
        cursor = conn.cursor()

        agency_names = models.Complaint.get_agency_names() # list of strings ['NYPD', 'FDNY', 'DSNY']
        agency_dicts = [models.Complaint.complaint_total_for_agency(agency_name) for agency_name in agency_names]
        return json.dumps(agency_dicts, default = str)

    @app.route('/incidents/search') 
    def search_incidents():
        conn = db.get_db()
        cursor = conn.cursor()

        params = dict(request.args)
        incidents = models.Incident.search(params, cursor)
        incident_dicts = [incident.to_json(cursor) for incident in incidents]
        return json.dumps(incident_dicts, default = str)

    @app.route('/incidents/<id>') 
    def incident(id):
        conn = db.get_db()

        cursor = conn.cursor()
        incident = db.find(models.Incident, id, cursor)
        return json.dumps(incident.__dict__, default = str)

    return app 