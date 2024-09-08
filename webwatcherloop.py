import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import hashlib
import time
from twilio.rest import Client

# credentials from environment variables
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
your_phone_number = os.getenv('YOUR_PHONE_NUMBER')
#url = 'https://www.elitekeyboards.com/'
url = 'https://www.youtube.com/'

# site contents
def get_website_content():
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser').get_text()

# compares current content hash to the former
def calculate_hash(content):
    return hashlib.md5(content.encode()).hexdigest()

# text message alert
def send_text_message(message):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )

# monitoring loop
def monitor_website():
    previous_hash = ''
    
    while True:
        try:
            content = get_website_content()
            current_hash = calculate_hash(content)
            
            if previous_hash and current_hash != previous_hash:
                message = f"The content of {url} has changed!"
                send_text_message(message)
                print(message)
            
            previous_hash = current_hash
            time.sleep(15)  # check every 15 seconds
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            time.sleep(30)  # wait for 30 before retrying

if __name__ == '__main__':
    monitor_website()
