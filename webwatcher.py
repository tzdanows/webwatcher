import os
import requests
from bs4 import BeautifulSoup
import hashlib
import logging
from dotenv import load_dotenv
from twilio.rest import Client

# load environment variables
load_dotenv()

# set up logging
logging.basicConfig(filename='ekmonitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
your_phone_number = os.getenv('YOUR_PHONE_NUMBER')
url = 'https://www.elitekeyboards.com/'

def get_website_content():
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser').get_text()
    except requests.RequestException as e:
        logging.error(f"Error fetching website content: {e}")
        return None

def calculate_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

def send_text_message(message):
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=your_phone_number
        )
        logging.info(f"Text message sent: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending text message: {e}")

def check_website():
    content = get_website_content()
    if content is None:
        logging.error("Failed to fetch website content")
        return

    current_hash = calculate_hash(content)
    
    try:
        with open('last_hash.txt', 'r') as f:
            previous_hash = f.read().strip()
    except FileNotFoundError:
        previous_hash = ''

    if previous_hash and current_hash != previous_hash:
        message = f"The content of {url} has changed!"
        send_text_message(message)
        logging.info(message)

    with open('last_hash.txt', 'w') as f:
        f.write(current_hash)

    logging.info("Website check completed")

if __name__ == '__main__':
    logging.info("Starting website check")
    check_website()

