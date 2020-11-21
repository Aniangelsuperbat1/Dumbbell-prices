import smtplib
from email.message import EmailMessage


def Email_alert(to, subject, body):
    message = EmailMessage()
    message.set_content(body)
    message["to"] = to
    message["subject"] = subject
    
    email = "Aniangelsuperbat@gmail.com"
    message["from"] = email
    password = ""

    server = smtplib.SMTP("smtp.gmail.com")
    server.starttls()
    server.login(email, password)
    server.send_message(message)
    
    server.quit()

if __name__ == "__main__":
    Email_alert("Zhen.Patrick@gmail.com", "Notification", "Your dumbbels have reached the desired price!")
