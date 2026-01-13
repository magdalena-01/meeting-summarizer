import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()  # Loads from .env file

def send_email(summary, recipient):
    msg = EmailMessage()
    msg.set_content(summary)
    msg['Subject'] = 'Meeting Summary & Action Items'
    msg['From'] = os.getenv("EMAIL_SENDER")
    msg['To'] = recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(os.getenv("EMAIL_SENDER"), os.getenv("EMAIL_APP_PASSWORD"))
        smtp.send_message(msg)
