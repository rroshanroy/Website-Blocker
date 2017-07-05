import time
from datetime import datetime as dt

redirect_URL = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com', 'www.wikipedia.com', 'wikipedia.com'] # Will work on interface soon. 
hosts_temp = 'hosts' # Working on a dummy hosts folder.
hosts_path = '/private/etc/hosts'


# Creates a continuous process.
while True :
	# Checking to see if we're in the working hours (8am to 4pm). Block websites if condition is met. 
	if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16) :
		with open(hosts_temp, 'r+') as file :
			content = file.read()
			for website in website_list :
				if website in content :   
					pass
				else :
					file.write(redirect_URL+ " " + website + "\n")
	# This is for leisure time. Unblock websites.
	else :
		with open(hosts_temp, 'r+') as file :
			content = file.readlines()
			file.seek(0)
			for line in content :
				if not any(website in line for website in website_list) :
					file.write(line)
			file.truncate()
			print("Fun time")
			
			

	# To avoid working every millisecond (depending on processor speed).
	time.sleep(30)
