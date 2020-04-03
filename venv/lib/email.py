import smtplib
import config
import email.mime.multipart
import email.mime.text

server= smtplib.SMTP(host=smtp.gmail.com,587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(config.senders_email,config.password)
msg= mime.multipart()
msg['from']=senders_email
msg['to']=recievers_email
msg['subject']="security issues"
body=''' malicious person suspected


'''

server.sendmail(config.senders_email,config.recivers_email,config.msg)
server.quit()
