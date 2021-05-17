import send_Email
import face_detect

if(False == face_detect.face_check()):
    send_Email.send_Email()