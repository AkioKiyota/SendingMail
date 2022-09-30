from email.message import EmailMessage
from multiprocessing import context
import ssl
import smtplib

email_sender = "emailsendemail83@gmail.com"
email_password = "xihanzlcljlbhunk"
email_reciever = "berkefekeskin@gmail.com"

subject = "yo!"

body = """
Yo, sup bro.
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
    
