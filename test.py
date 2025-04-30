# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-c5f8476a6aef4a73b61cbb0c7bc1f099",
                base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a good coder on python"},
        {"role": "user", "content": "Hello, write a simple program for the output of 'Hello World'"},
    ],
    stream=False
)

print(response.choices[0].message.content)
