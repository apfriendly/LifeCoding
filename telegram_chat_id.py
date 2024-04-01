import requests


def get_telegram_chat_id():
    TOKEN = "tg_token"
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    response = requests.get(url).json()

    if 'result' in response and response['result']:
        chat_id = response['result'][0]['message']['chat']['id']
        return chat_id
    else:
        print("Невозможно получить chat ID.")
        return None


print(get_telegram_chat_id())
