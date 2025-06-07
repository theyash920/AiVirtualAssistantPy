import openai
import os
from openai import OpenAI

key = "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"

messages = []

client = OpenAI(
    api_key=key,
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )

    # print(chat_completion)
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }

    messages.append(message)
    print(f"Jarvis: {message['content']}")

if __name__ == "__main__":
    print("Jarvis: Hi I am Jarvis, How may I help you\n")
    while True:
        user_question = input()
        print(f"User: {user_question}")
        completion(user_question)

