from email.message import EmailMessage
from multiprocessing import context
import ssl
import smtplib
import os
import datetime


email_sender = "emailsendemail83@gmail.com"
email_password = "xihanzlcljlbhunk"
email_reciever = "ShirisaSaya@gmail.com"

subject = "yo!"

today = datetime.date.today()
now = datetime.datetime.now()

body = f"""
User = {os.getlogin()}
Date = {today.strftime('%d/%m/%Y')} 
Time = {now.strftime('%H:%M:%S')}
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_sender
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())
    
