import os
import smtplib
from email.message import EmailMessage

SMTP_HOST = os.getenv("SMTP_HOST", "")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER", "")
SMTP_PASS = os.getenv("SMTP_PASS", "")
MAIL_FROM = os.getenv("MAIL_FROM", SMTP_USER)
MAIL_TO = os.getenv("MAIL_TO", "")
SUBJECT = os.getenv("MAIL_SUBJECT", "Lab 7 Cron Email")
BODY = os.getenv("MAIL_BODY", "Scheduled email sent by cron.")

if not (SMTP_HOST and SMTP_USER and SMTP_PASS and MAIL_TO):
    raise SystemExit("Missing SMTP_* or MAIL_TO environment variables.")

msg = EmailMessage()
msg["From"] = MAIL_FROM
msg["To"] = MAIL_TO
msg["Subject"] = SUBJECT
msg.set_content(BODY)

with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
    server.starttls()
    server.login(SMTP_USER, SMTP_PASS)
    server.send_message(msg)
