import openai
import extraction

openai_api_key = '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'

openai.api_key = openai_api_key

def generate_ai_news(user):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a football manager."},
            {"role": "user", "content": f"Create a message for {user['name']} about the matter of physical training (maximum of 100 characters)"}
        ]
    )
    return completion.choices[0].message.content

for user in extraction.users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })

