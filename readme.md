# Web-Watcher
This project is a 24/7 monitor for website changes. It periodically checks specified websites for any content changes and sends notifications to your cell phone when changes are detected.

#### Features
* Monitors multiple websites for content changes
* Uses AWS Lambda for serverless execution
* Stores website hashes in AWS_S3/buckets/hashes.json for comparison
* Sends SMS notifications via Twilio when changes are detected
* Configurable time intervals using AWS CloudWatch Events

## Requirements 
* python 3.8+
* aws account
* twilio account

### twilio phone requirements
* twilio account sid
* twilio phone number
* twilio api key
* your phone number authenticated with twilio

(all of these factors stored in environment variables via .env or in aws env vars)

# Project Setup

I've chosen to take the AWS lambda approach due to it's convenience factors:

to setup AWS S3 + Lambda to run webwatcher on your urls, you should:

1. Login to AWS and set up an S3 bucket (default settings)
2. Create a new lambda function
    * Configuration:
        * Runtime: Python 3.8+ (sole aspect configured during creation)
        * Policies:
            * AmazonS3FullAccess (for S3 operations)
            * CloudWatchLogsFullAccess (for logs)
3. Set up a cloudwatch event to run the lambda function every {x} minutes/seconds (under lambda/configuration/triggers)
4. Configure your code to match the aws bucket & lambda function settings:
    * prepare environment variables (under lambda/configuration/environment variables)
    ```js
    S3_BUCKET_NAME=your_s3_bucket_name
    TWILIO_ACCOUNT_SID=your_twilio_account_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_PHONE_NUMBER=your_twilio_phone_number
    YOUR_PHONE_NUMBER=your_phone_number
    URLS_TO_MONITOR=url1,url2,url3
    ```
5. Prepare a folder with dependencies for the lambda function, then zip it
    (on your local pc)
    * install dependencies via:
    ```bash
    # make a new folder(if necessary) & cd into it
    mkdir lambda_function
    cd lambda_function
    # move your code & requirements.txt into the folder
    # pre-install dependencies
    pip install -r requirements.txt -t .
    # zip the folder
    zip -r ../lambda_function.zip .
    ```
    * and import this folder to your lambda function
5. Test and deploy the function!
    * you should now be able to test your function and run it assuming everything is correctly configured
    * refer to cloudwatch log groups for debugging alongside checking the contents of the S3 bucket

## options I considered:
* lambda_function.py
    * set up an aws lambda function
    * create an aws S3 bucket
    * set up aws cloudwatch
    * more details above
* gcf.py
    * set up a google cloud function
    * not yet explored..
* cron job approach (as shown by webwatcher.py)
    * explored but deemed too much work

## resources:
* https://docs.aws.amazon.com/lambda/
* https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/
* https://www.crummy.com/software/BeautifulSoup/bs4/doc/
* https://www.twilio.com/docs/libraries/python
* https://www.twilio.com/docs/messaging/quickstart
