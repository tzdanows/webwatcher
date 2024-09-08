import os
import boto3
import requests
from bs4 import BeautifulSoup
import hashlib
from twilio.rest import Client

# AWS S3 setup
s3 = boto3.client('s3')
BUCKET_NAME = 'your-bucket-name'
FILE_NAME = 'last_hash.txt'

# credentials from environment variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
your_phone_number = os.environ['YOUR_PHONE_NUMBER']
url = 'https://www.elitekeyboards.com/'

def get_website_content():
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser').get_text()

def calculate_hash(content):
    return hashlib.sha256(content.encode()).hexdigest()

def send_text_message(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )
    print(f"Text message sent: {message.sid}")

def get_previous_hash():
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=FILE_NAME)
        return response['Body'].read().decode('utf-8').strip()
    except s3.exceptions.NoSuchKey:
        return ''

def save_current_hash(current_hash):
    s3.put_object(Bucket=BUCKET_NAME, Key=FILE_NAME, Body=current_hash)

def lambda_handler(event, context):
    content = get_website_content()
    current_hash = calculate_hash(content)
    previous_hash = get_previous_hash()

    if previous_hash and current_hash != previous_hash:
        message = f"The content of {url} has changed!"
        send_text_message(message)
        print(message)

    save_current_hash(current_hash)
    return {'statusCode': 200, 'body': 'Check completed successfully'}
