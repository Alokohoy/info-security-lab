import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
smtp_port = 587
sender_email = ""
sender_password = ""
receiver_email = ""
html_page_link = "file:///path/to/lab4/index.html"

subject = "Verify your card - action required"
body = """
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <style>
       body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
       .container { max-width: 600px; margin: 0 auto; background: #fff; padding: 24px; border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); }
       .header { display: flex; align-items: center; padding-bottom: 16px; border-bottom: 1px solid #eee; }
       .header span { font-size: 24px; margin-right: 10px; }
       .header h2 { margin: 0; font-size: 20px; color: #1a1a2e; }
       .button { display: inline-block; background: linear-gradient(135deg, #3498db, #2980b9); color: white; text-decoration: none; padding: 14px 28px; border-radius: 8px; font-size: 16px; font-weight: 600; margin: 16px 0; }
       .footer { text-align: center; margin-top: 24px; font-size: 12px; color: #888; }
   </style>
</head>
<body>
   <div class="container">
       <div class="header"><span>&#128274;</span><h2>Secure Payment</h2></div>
       <p style="font-size: 16px; color: #333;">We need to verify your payment card.</p>
       <p style="font-size: 16px; color: #333;">Please confirm your details by clicking the link below. This helps us protect your account.</p>
       <p style="font-size: 14px; color: #666;">Link: %s</p>
       <a href="%s" class="button">Verify card now</a>
       <div class="footer">
           <p>If you did not request this, please ignore this message.</p>
       </div>
   </div>
</body>
</html>
""" % (html_page_link, html_page_link)

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.attach(MIMEText(body, "html"))

server = None
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")
finally:
    if server:
        server.quit()
