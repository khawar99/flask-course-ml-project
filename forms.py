from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

# Load the data
train = pd.read_csv('./data/train.csv')
val = pd.read_csv('./data/val.csv')
X_data = pd.concat([train, val], axis=0).drop(columns="price")

class InputForm(FlaskForm):
    airline = SelectField(
        label="Airline",
        choices=[(airline, airline) for airline in X_data.airline.unique()],
        validators=[DataRequired()]
    )
    date_of_joining = DateField(
        label="Date of Journey",
        format='%Y-%m-%d',  # Specify the date format
        validators=[DataRequired()]
    )
    source = SelectField(
        label="Source",
        choices=[(source, source) for source in X_data.source.unique()],
        validators=[DataRequired()]
    )
    Destination = SelectField(
        label="Destination",
        choices=[(destination, destination) for destination in X_data.destination.unique()],
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="Departure Time",
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival Time",
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=[(info, info) for info in X_data.additional_info.unique()],
        validators=[DataRequired()]
    )
    submit = SubmitField("Predict")