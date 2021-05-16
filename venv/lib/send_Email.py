
import smtplib
import config
def send_Email():
    try:
        server= smtplib.SMTP ('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(config.email_Address,config.password)
        message = f'Subject: {config.subject} \n\n {config.msg}'
        server.sendmail(config.email_Address,config.recievers_email,message)
        server.quit()
        print("Success email is sent!")
    except:
        print("failed to send email")
