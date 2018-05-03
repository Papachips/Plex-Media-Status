import os
import time
from twilio.rest import Client

account_sid = '/ TWILIO ACCOUNT ID HERE /'
auth_token = '/ TWILIO AUTH TOKEN HERE /'
client = Client(account_sid, auth_token)

isUnmounted = False
while(True):
	while(isUnmounted == False):
		if(os.path.ismount('/ MEDIA FILE PATH HERE /')):
			time.sleep(60)
			isUnmounted = False
		else:
			message = client.messages \
				.create(
					body = "KregFlix is currently down for maintenance.",
					from_="/ TWILIO PHONE NUMBER HERE /",
					to="/ RECIPIENT PHONE NUMBER HERE "
					)
			isUnmounted = True

	while(isUnmounted == True):
		if(os.path.ismount('/ MEDIA FILE PATH HERE /')):
			message = client.messages \
				.create(
					body = "KregFlix is back up and running.",
					from_="/ TWILIO PHONE NUMBER HERE /",
					to="/ RECIPIENT PHONE NUMBER HERE "
					)
			isUnmounted = False
		else:
			time.sleep(60)
			isUnmounted = True