
import smtplib
import config
def send_Email():
    try:
        server= smtplib.SMTP ('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(config.email_Address,config.password)
        server.send_message(config.msg)
        server.quit()
        print("Success email is sent!")
    except:
        print("failed to send email")
