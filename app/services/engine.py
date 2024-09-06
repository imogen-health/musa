from openai import OpenAI
from app.environment import Environment

client = OpenAI(api_key=Environment.OPENAI_API_KEY)

def build_chat_message_content(message):
    return "Say this is a test"

def handle_message(message):
    chat_message = {
        "role": "user",
        "content": build_chat_message_content(message),
    }

    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[chat_message],
    )

    return chat_completion.choices[0].message.content