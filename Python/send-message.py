#############################################################################
# This program asks the user for some text and an optional picture to send  #
# as a text message to a phone number using the twilio library              #
#############################################################################

# you need to install twilio
from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# store your account SID and auth token in the environmental variables for security purposes
account_sid = os.environ.get('ACCOUNTSID')
auth_token = os.environ.get('AUTHTOKEN')
client = Client(account_sid, auth_token)

body = str(input("enter text: "))
add_picture = str(input("Add a picture? Y/N:  "))
if add_picture.lower() == 'y':
    picture = str(input("Enter the url of the picture: "))

    message = client.messages \
                    .create(
                        body="",
                        # optional picture that sends with the text message
                        media_url=picture,
                        # your twilio phone number is created when you sign up for a free account on twilio.com
                        from_='YOUR TWILIO PHONE NUMBER',
                        to='+TARGET PHONE NUMBER'
                    )
else: 
    message = client.messages \
                    .create(
                        body=body,
                        # your twilio phone number is created when you sign up for a free account on twilio.com
                        from_='YOUR TWILIO PHONE NUMBER',
                        to='+TARGET PHONE NUMBER'
                    )
