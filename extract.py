import pandas as pd     #store as df/table
import requests         #connect to api

#main website address so we dont have to type it out every time
BASE_URL = 'https://fakestoreapi.com/'

def extract_product():

    #'https://fakestoreapi.com/products' for product extract function
    url = f'{BASE_URL}/products'

    #get() - tell website to send you data, from requests library
    #website will say which url to use as an argument based on data you want
    #requests.get('https://fakestoreapi.com/products')
    response = requests.get(url)

    #check if API request success
    #stop if failed - prevent bad/missing data use
    response.raise_for_status()

    #.json() - coverts API data from JSON to python data
        #dict - if single
        #list - if multiple (array)
    data = response.json()

    # convert data into a pandas table (DataFrame) for easier use
    product_df = pd.DataFrame(data)

    #return table to main variable
    return product_df

def extract_users():

    url = f'{BASE_URL}/users' #url specific to user data

    #get user data
    response = requests.get(url)

    #check status
    response.raise_for_status()

    #parse json to python objects
    data = response.json()

    #data frame
    df = pd.DataFrame(data)

    return df
