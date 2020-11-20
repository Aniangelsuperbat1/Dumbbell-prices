import smtplib
from email.message import EmailMessage


def Email_alert(to, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message["subject"] = subject

    email = ""
    password = ""

    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(email, password)

    server.quit

if __name__ == "__main__":
    Email_alert("Zhen.Patrick@gmail.com", "Notification", "Your dumbbels have reached the desired price!")
