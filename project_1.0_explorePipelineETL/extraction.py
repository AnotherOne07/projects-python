import pandas as pd
import requests
import json


# API endpoint
api_url = 'https://sdw-2023-prd.up.railway.app'
data_frame = pd.read_csv('data/santanderDevWeek.csv')
# The method toList() from pandas lib is used to convert a pandas object into a Python List
users_id = data_frame['UserID'].tolist()

def get_user(id, api_end_point):
    response = requests.get(f'{api_end_point}/users/{id}')
    return response.json() if response.status_code == 200 else None

# List comprehension to filter the data received by API request and obtain only the necessary information
users = [user for id in users_id if (user := get_user(id, api_url)) is not None]

# def generate_ai_news(user):
#     completion = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a football manager."},
#             {"role": "user", "content": f"Create a message for {user['name']} about the matter of physical training (maximum of 100 characters)"}
#         ]
#     )
#     return completion.choices[0].message.content


def attribute_user_news(user):
    response = {
        "speak_1":"Welcome, we are part of the biggest football organization",
        "speak_2":"Welcome, we are part of the lowest football organization",
    }
    return response['speak_1'] if int(user['id']) % 2 == 0 else response['speak_2']


def update_credit_card(user):
    card_limit = user["account"]["limit"]
    # print(card_limit)
    coefficient = str(user['id'])
    return card_limit + (len(coefficient) * 10)

def update_user(user):
    response = requests.put(f"{api_url}/users/{user['id']}", json=user)
    return True if response.status_code == 200 else False


# Function to append news to a register
for user in users:
    news = attribute_user_news(user)
    # print(news)
    user['news'].append({
        "icon": "https://digitalinovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })
    # print(user)


for user in users:
    new_credit = update_credit_card(user)
    user["account"]["limit"] = new_credit
    print(new_credit)

for user in users:
    success = update_user(user)
    print(f"User {user['name']} updated ? {success}")
