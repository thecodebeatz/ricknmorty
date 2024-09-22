import requests
import random

def send_telegram_message(message=""):
    bot_token = 'XXX'
    chat_id = 'YYY'  # Replace with your chat ID

    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}'
    
    response = requests.get(send_text)
    if response.status_code == 200:
        print("Telegram message sent!")
    else:
        print("Failed to send message:", response.status_code)

def get_random_character():
    # First, get the total number of characters in the Rick and Morty universe
    response = requests.get("https://rickandmortyapi.com/api/character")
    data = response.json()
    total_characters = data['info']['count']
    
    # Get a random character by their ID
    random_id = random.randint(1, total_characters)
    character_response = requests.get(f"https://rickandmortyapi.com/api/character/{random_id}")
    character_data = character_response.json()

    # Extract relevant details
    name = character_data['name']
    status = character_data['status']  # Status can be 'Alive', 'Dead', or 'unknown'

    # Check if the character is dead
    if status == 'Dead':
        send_telegram_message(f"The character '{name}' is dead.")
    else:
        send_telegram_message(f"The character '{name}' is {status.lower()}.")

def lambda_handler(event, context):
    get_random_character()