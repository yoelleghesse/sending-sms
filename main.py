import os
from twilio.rest import Client
import time
from datetime import datetime as dt


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

while True:
  now = dt.now()
  if now.hour == 13 and now.minute == 18:
    message = client.messages \
                    .create(
                        body="Message sent.",
                        from_='+1000000000',
                        to='+2000000000'
                    )

    print(message.sid)
  time.sleep(60)
