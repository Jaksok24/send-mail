import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, receiver_email, subject, body, password):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print("E-mail został wysłany pomyślnie!")

    except Exception as e:
        print(f"Coś poszło nie tak... {str(e)}")

sender_email = "moj_mail"
receiver_email = "mail_odbiorcy"
subject = "Powiadomienie"
body = "Test Python"
password = "ktup rkcb ryhh pxow"

send_email(sender_email, receiver_email, subject, body, password)
