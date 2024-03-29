# Download the Python helper library from twilio.com/docs/python/install
import os

from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+16096197576',
                        from_='+17162717577'
                    )

print(call.sid)
