import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEText import MIMEText
import os
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
import amazon_emails
#if we are import then we are also sending the mail through amazon_emails also
#means twoo emails are send

smtp_server = 'fet_server_name'
smtp_username = 'get name'
smtp_password = 'get password'
smtp_port = '587'
smtp_do_tls = True
subject = "sending attachment"
fromEmail = "email@example.com"
toEmail = "to@email.com'
file_name = "error.txt"
template = amazon_emails.msg

def send_message(smtp_server,smtp_username,smtp_password,smtp_port,smtp_do_tls,fromEmail,toEmail,subject,file_name,template):
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    body = template
    file_read = open(file_name,"rb")
    attachment = MIMEText(file_read.read())
    attachment.set_payload(file_read.read())
    
    attachment.add_header('Content-Disposition', 'attachment', filename="error.txt")
    msg.attach(attachment)
    content = MIMEText(body, 'html')
    msg.attach(content)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(10)
    server.starttls()
    server.ehlo()
    server.login(smtp_username,smtp_password)
    server.sendmail(fromEmail, toEmail, msg.as_string()) 

if __name__ == '__main__':
    send_message(smtp_server,smtp_username,smtp_password,smtp_port,smtp_do_tls,fromEmail,toEmail,subject,file_name,template)
