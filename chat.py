import os
import requests
import json

def chat_loop():
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise SystemExit('Please set the OPENAI_API_KEY environment variable.')

    messages = []
    print('Starting conversation with ChatGPT. Type "exit" to quit.')
    while True:
        user_input = input('You: ')
        if user_input.lower() in {'exit', 'quit'}:
            break
        messages.append({"role": "user", "content": user_input})
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {api_key}',
                'Content-Type': 'application/json'
            },
            json={
                'model': 'gpt-3.5-turbo',
                'messages': messages
            }
        )
        if response.status_code != 200:
            print('Error communicating with API:', response.text)
            break
        data = response.json()
        reply = data['choices'][0]['message']['content']
        messages.append({"role": "assistant", "content": reply})
        print('ChatGPT:', reply)

if __name__ == '__main__':
    chat_loop()
