# Set dependencies
import datetime as dt
from flask.globals import session
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy import engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variable for ea class
Measurement = Base.classes.measurement
Station = Base.classes.station

# Session link from Python to our database
session = Session(engine)

# Define our Flas app
app = Flask(__name__)
# Define welcome route
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/percipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')