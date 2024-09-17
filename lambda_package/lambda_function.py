import os
import boto3
import requests
from bs4 import BeautifulSoup
import hashlib
from twilio.rest import Client
import json

# AWS S3 setup
s3 = boto3.client('s3')
BUCKET_NAME = os.environ['S3_BUCKET_NAME']
HASH_FILE_NAME = 'url_hashes.json'

# Twilio setup
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone_number = os.environ['TWILIO_PHONE_NUMBER']
your_phone_number = os.environ['YOUR_PHONE_NUMBER']

# List of URLs to monitor (in env variables for ease of change/security)
URLS_TO_MONITOR = os.environ['URLS_TO_MONITOR'].split(',')

def get_website_content(url):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return BeautifulSoup(response.text, 'html.parser').get_text()
    except requests.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None

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

def get_previous_hashes():
    try:
        response = s3.get_object(Bucket=BUCKET_NAME, Key=HASH_FILE_NAME)
        return json.loads(response['Body'].read().decode('utf-8'))
    except s3.exceptions.NoSuchKey:
        return {}

def save_current_hashes(current_hashes):
    s3.put_object(Bucket=BUCKET_NAME, Key=HASH_FILE_NAME, Body=json.dumps(current_hashes))

def lambda_handler(event, context):
    previous_hashes = get_previous_hashes()
    current_hashes = {}
    changed_urls = []

    for url in URLS_TO_MONITOR:
        content = get_website_content(url)
        if content is None:
            continue

        current_hash = calculate_hash(content)
        current_hashes[url] = current_hash

        if url in previous_hashes and current_hash != previous_hashes[url]:
            changed_urls.append(url)

    if changed_urls:
        message = "THIS WEBSITE HAS CHANGED: \n" + "\n".join(changed_urls)
        send_text_message(message)
        print(message)

    save_current_hashes(current_hashes)
    return {'statusCode': 200, 'body': f'Check completed. {len(changed_urls)} sites changed.'}
