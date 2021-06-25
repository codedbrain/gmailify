import requests
import sys

def check(email):
    resp = requests.get(f'https://mail.google.com/mail/gxlu', params={'email': email})
    for cookie in resp.cookies:
    	if cookie.name == "COMPASS":
        	return True		

with open(sys.argv[1],'r') as lines:
	for email in lines:
		email = email.rstrip('\n')
		if check(email):
			print(email)
			
