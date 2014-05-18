import os
import smtplib
import mimetypes
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEAudio import MIMEAudio
from email.MIMEImage import MIMEImage
from email.Encoders import encode_base64
def sendMail(subject, text, *attachmentFilePaths):
  gmailUser = 'yo.mama@gmail.com'
  gmailPassword = 'bogus!'
  recipient = 'test@test.com'
  msg = MIMEMultipart()
  msg['From'] = gmailUser
  msg['To'] = recipient
  msg['Subject'] = subject
  msg.attach(MIMEText(text))
  for attachmentFilePath in attachmentFilePaths:
    msg.attach(getAttachment(attachmentFilePath))
  mailServer = smtplib.SMTP('smtp.gmail.com', 587)
  mailServer.ehlo()
  mailServer.starttls()
  mailServer.ehlo()
  mailServer.login(gmailUser, gmailPassword)
  mailServer.sendmail(gmailUser, recipient, msg.as_string())
  mailServer.close()
  print('Sent email to %s' % recipient)
def getAttachment(attachmentFilePath):
  contentType, encoding = mimetypes.guess_type(attachmentFilePath)
  if contentType is None or encoding is not None:
    contentType = 'application/octet-stream'
  mainType, subType = contentType.split('/', 1)
  file = open(attachmentFilePath, 'rb')
  if mainType == 'text':
    attachment = MIMEText(file.read())
  elif mainType == 'message':
    attachment = email.message_from_file(file)
  elif mainType == 'image':
    attachment = MIMEImage(file.read(),_subType=subType)
  elif mainType == 'audio':
    attachment = MIMEAudio(file.read(),_subType=subType)
  else:
    attachment = MIMEBase(mainType, subType)
  attachment.set_payload(file.read())
  encode_base64(attachment)
  file.close()
  attachment.add_header('Content-Disposition', 'attachment',   filename=os.path.basename(attachmentFilePath))
  return attachment






















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

smtp_server = 'email-smtp.eu-west-1.amazonaws.com'
smtp_username = 'AKIAJSP64C3S2ZASXBIA'
smtp_password = 'ArcrhJNW+OEiGNoAaHSMKF3Iq8Sqrs44uwR83cGJw8zv'
smtp_port = '587'
smtp_do_tls = True
subject = "sending attachment"
fromEmail = "ksrinathchowdary9@gmail.com"
toEmail = "kodalizzzzz434@gmail.com"
filename = "error.txt"
template = amazon_emails.msg1

def send_message(smtp_server,smtp_username,smtp_password,smtp_port,smtp_do_tls,fromEmail,toEmail,subject,filename,template):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = fromEmail
    body = template
    print filename
    attachment = MIMEText(filename.read())
    attachment.set_payload(filename.read())
    filename.close()
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attachment)
    content = MIMEText(body, 'plain')
    msg.attach(content)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.set_debuglevel(10)
    server.starttls()
    server.ehlo()
    server.login(smtp_username,smtp_password)
    server.sendmail(fromEmail, toEmail, msg.as_string()) 

if __name__ == '__main__':
    send_message(smtp_server,smtp_username,smtp_password,smtp_port,smtp_do_tls,fromEmail,toEmail,subject,filename,template)