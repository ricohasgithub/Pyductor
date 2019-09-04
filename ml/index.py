
import pandas as pd
import numpy as np

import keras

''' 
    Take in a csv of data points on supposed note values, and then actual performance values.
    Then use algorithm to calculate deviation, and then train algorithm via deviated values.
    Take data feedstream from pipeline on web frontend and then run network
'''

# Function for loading verified data
def load_ver (filename):
    return pd.read_csv('../data/' + filename)

# Function for translating user data music stream into Pandas dataframe
def parse_user (filename):
    return pd.read_csv('../gen/' + filename)

# Load training data

# Train Model

# Save Model