import time
from datetime import datetime as dt

redirect_URL = "127.0.0.1"
website_list = ['www.facebook.com', 'facebook.com', 'www.wikipedia.com', 'wikipedia.com']
hosts_temp = 'hosts'
hosts_path = '/private/etc/hosts'


while True :
	if dt(dt.now().year, dt.now().month, dt.now().day, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 21) :
		with open(hosts_temp, 'r+') as file :
			content = file.read()
			for website in website_list :
				if website in content :   
					pass
				else :
					file.write(redirect_URL+ " " + website + "\n")
	else :
		with open(hosts_temp, 'r+') as file :
			content = file.readlines()
			file.seek(0)
			for line in content :
				if not any(website in line for website in website_list) :
					file.write(line)
			file.truncate()
			print("Fun time")
			
			


	
	time.sleep(5)
