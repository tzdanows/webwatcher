# a 24/7 watcher for website changes

## cron job approach
* webwatcher.py

add:
```
*/5 * * * * /path/to/your/venv/bin/python /path/to/webwatcher.py
```
to:
```
crontab -e
```
keep the server running.

## basic / aws lambda or gcf approach
* webwatcherloop.py (standard approach)
* webwatcherawslambda.py (aws lambda approach)
    * set up an aws lambda function
    * set up aws cloudwatch
* webwatchergcf.py (google cloud function approach)
    * set up a google cloud function
    * etc..
* 
--- 

this implementation will check for changes every 5 minutes, the cronjob is the more resource effective approach but you will need a server running 24/7, while the aws lambda approach is more flexible and can be scaled to any number of websites and can be run on any schedule without the need for a server.