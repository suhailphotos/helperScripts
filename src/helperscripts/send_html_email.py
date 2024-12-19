import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email details from .env file
sender_email = os.getenv("SENDER_EMAIL")
recipient_email = os.getenv("RECIPIENT_EMAIL")
smtp_password = os.getenv("SMTP_PASSWORD")
subject = "How to share HDR Images on Instagram"

# Path to the HTML file
html_file_path = "html/email.html"

# Read HTML content
with open(html_file_path, "r") as file:
    html_content = file.read()

# Create email
msg = MIMEMultipart("alternative")
msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = recipient_email
msg.attach(MIMEText(html_content, "html"))

# Send email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
