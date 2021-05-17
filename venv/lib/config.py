from email.message import EmailMessage
import imghdr
email_Address = ""
password = ""
#subject="Security_Alert"
msg= EmailMessage()
msg['Subject'] = "Security_Alert"
msg['From']= email_Address
msg['To'] = ""
msg.set_content("intruder found")
with open('images/image.png','rb') as f:
    file_data= f.read()
    file_type = imghdr.what(f.name)
    file_name = f.name

    msg.add_attachment(file_data, maintype = 'image', subtype = file_type, filename= file_name)
