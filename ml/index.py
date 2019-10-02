
import pandas as pd
import numpy as np

from flask import Flask

# Initialize flask server pipeline
app = Flask(__name__)

import json

import keras

''' 
    Take in a csv of data points on supposed note values, and then actual performance values.
    Then use algorithm to calculate deviation, and then train algorithm via deviated values.
    Take data feedstream from pipeline on web frontend and then run network.

    NN/Model used is a comparison network that checks for how similar your playing is to
    the actual song.
'''

# Class that represents a user json and file request
class Request(object):

    def __init__(self, ver_file, user_file, json_req):
        self.ver_file = self.load_ver(ver_file)
        self.user_file = self.load_user(user_file)
        self.parse_request = self.parse_requests(json_req)

    def load_ver (self, filename):
        # Function for loading verified data
        return pd.read_csv('../data/' + filename)

    def load_user (self, filename):
        # Function for loading user data music stream into Pandas dataframe
        return pd.read_csv('../gen/' + filename)

    def parse_requests (self, json_req):
        # Function that parses the json request that the user sends via the web/Arduino interface
        return json.loads(json_req)

# Load training data

print("Hello World!")

# Train Model

# Save Model