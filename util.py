import json
import joblib
import numpy as np

__furnishing = None
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, size, bhk, furnishing):
    try:
        loc_index = __data_columns.index(location)
        loc_furnishing = __data_columns.index(furnishing)
    except:
        loc_index = -1
        loc_furnishing = -1
    x = np.zeros(len(__data_columns))
    x[0] = bhk
    x[1] = size
    
    if loc_index>=0:
        x[loc_index] = 1
    if loc_furnishing >= 0:
        x[loc_furnishing] = 1    
    return round(__model.predict([x])[0])

def load_saved_artifacts():
    global  __data_columns
    global __locations
    global __furnishing

    with open("columns.json", "r") as f:
        __data_columns = json.load(f)['columns']
        __locations = __data_columns[2:-3]  
        __furnishing= __data_columns[-3:]  
    global __model
    if __model is None:
        with open('Rent_joblib', 'rb') as f:
            __model = joblib.load(f)

def get_location_names():
    return __locations

def get_furnishing_type():
    return __furnishing

if __name__ == '__main__':
    load_saved_artifacts()