import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower()) #check if location exists in dataset
    except:
        loc_index = -1 

    x = np.zeros(len(__data_columns)) # the input for prediction
    x[0] = bhk
    x[1] = sqft
    x[2] = bath
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2) # returns predicted value rounded to 2 decimal places 


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns  #global variables
    global __locations
    global __model
    with open("C:\\Users\\pc\\Desktop\\Data Science\\housing_price_prediction\\server\\artifacts\\columns.json","r") as f:
        __data_columns = json.load(f)['data_columns']   #retrieving 'data columns' and locations from json file
        __locations = __data_columns[3:]

    if __model is None:    
       with open(r"C:\Users\pc\Desktop\Data Science\housing_price_prediction\server\artifacts\banglore_home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f) #retrieving the Linear Regression model from pickle file

def get_locations_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__=="__main__":
    load_saved_artifacts()
    print(get_locations_names())
    #print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    #print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    #print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    #print(get_estimated_price('Ejipura', 1000, 2, 2))
