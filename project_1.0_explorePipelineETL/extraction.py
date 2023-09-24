import pandas as pd
import requests
import json

api_url = 'https://sdw-2023-prd.up.railway.app'

data_frame = pd.read_csv('data/santanderDevWeek.csv')

# The method toList() from pandas lib is used to convert a pandas object into a Python List
users_id = data_frame['UserID'].tolist()

def get_user(id, api_end_point):
    response = requests.get(f'{api_end_point}/users/{id}')
    return response.json() if response.status_code == 200 else None


users = [user for id in users_id if (user := get_user(id, api_url)) is not None]

print(json.dumps(users, indent=2))
