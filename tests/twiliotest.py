# basic twilio sms use-case

import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variable s from .env file
load_dotenv()

# credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
your_phone_number = os.getenv('YOUR_PHONE_NUMBER')

# create Twilio client
client = Client(account_sid, auth_token)

# send message
try:
    message = client.messages.create(
        from_=twilio_phone_number,
        body='Hello from Twilio',
        to=your_phone_number
    )
    print(f"Message sent: {message.sid}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
