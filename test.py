import requests
import json
import csv
import pandas as pd

# Define your Yelp API key
api_key = 'B9cMCVgVcWrQll09BveLmLuOUknpQC85VM8W2jtwird__ZY96umj-s7O4tk8BcUA4NswMvLT5S04yUfK-B_lBhGOUA3qC8BoOx7r9tB7W7M20NIu3uzyfTaJ1JU4ZXYx'

# Define the Yelp API endpoint URL
url = 'https://api.yelp.com/v3/businesses/search'

# Define the query parameters for the search
params = {
    'term': 'restaurants',  # Change to your desired search term
    'location': 'New York',  # Change to your desired location
    'limit': 50
}
# Define the headers with the Authorization header containing the API key
headers = {
    'Authorization': f'Bearer {api_key}',
    'accept': 'application/json',
}

nyc_raw = []
location = 'Manhattan, NY'
term = "Restaurants"
limit = 50
offset = 50 * 1
categories = "(restaurants, All)"

params = {
    'term': term,
    'location': location,
    'limit': 50,
    'offset': offset,
    'categories': categories
}

response = requests.get(url, headers=headers, params=params)
nyc_raw.append(response)
#get 1000
# for i in range(20):
#     location = 'Manhattan, NY'
#     term = "Restaurants"
#     limit = 50
#     offset = 50 * 1
#
#     params = {
#         'term': term,
#         'location': location,
#         'limit': 50,
#         'offset': offset
#     }
#
#     response = requests.get(url, headers=headers, params=params)
#     nyc_raw.append(response)

#create DataFrame
df = pd.DataFrame()
df = pd.DataFrame.from_dict(nyc_raw[0].json()['businesses'])
# for i in range(20):
#     section = pd.DataFrame.from_dict(nyc_raw[i].json()['businesses'])
#     df = df.append(section)
df.to_csv("nyc_restaurants.csv", index=False)



# # Make the GET request
# response = requests.get(url, params=params, headers=headers)
# data = None
# # Check if the request was successful (status code 200)
# if response.status_code == 200:
#     data = response.json()  # Parse the JSON response
#     businesses = data.get('businesses', [])
#     print(len(businesses))
#     # Process and use the data as needed
#     with open('businesses.json', 'w') as json_file:
#         json.dump(businesses, json_file, indent=4)
# else:
#     print(f'Error: {response.status_code}')
#     print(response.text)