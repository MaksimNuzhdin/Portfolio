from email import encoders
import pathlib
from .models import MSettings
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

SMTP_SERVER='smtp.gmail.com'
SENDER_MAIL='nuzhdin05@gmail.com'
ATTACH_FILE_1 = pathlib.Path(__file__).parent.joinpath("resume_en.pdf")
ATTACH_FILE_2 = pathlib.Path(__file__).parent.joinpath('resume_he.pdf')
PASSWORD_FILE=pathlib.Path(__file__).parent.joinpath('password.txt')
PORT='465'
#Zaxscd123
with open (PASSWORD_FILE, 'r')  as pf:
    SMTP_PASSWORD= pf.read()

def send_mail(receiver):
    settings=MSettings.objects.get(pk=1)
    title=str(settings.mail_title)
    h1=str(settings.mail_h1)
    text=str(settings.mail_text)
    RECEIVER_MAIL = receiver
      


    message = MIMEMultipart('alternative')
    message['Subject'] = f"{title}"
    message['From'] = SENDER_MAIL
    message['To'] = RECEIVER_MAIL
    msg_body_html = f"<h1 style = 'color:black;'>{h1}</h1> <p>{text}</p>"
    part1 = MIMEText(msg_body_html, 'html')
    message.attach(part1)
    with open(ATTACH_FILE_1, 'rb') as f: attachment1 = f.read()
    attach_part_1 = MIMEBase('application', 'octet-stream')
    attach_part_1.set_payload(attachment1)
    encoders.encode_base64(attach_part_1)
    # headers for attachment
    attach_part_1.add_header(
        'Content-Disposition',
        f'attachment; filename={ATTACH_FILE_1.name}'
    )
    message.attach(attach_part_1)
    with open(ATTACH_FILE_2, 'rb') as f: attachment2 = f.read()
    attach_part_2 = MIMEBase('application', 'octet-stream')
    attach_part_2.set_payload(attachment2)
    encoders.encode_base64(attach_part_2)
    # headers for attachment
    attach_part_2.add_header(
        'Content-Disposition',
        f'attachment; filename={ATTACH_FILE_2.name}'
    )
    message.attach(attach_part_2)

    context = ssl._create_unverified_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(SENDER_MAIL, SMTP_PASSWORD)
        print(server.sendmail(SENDER_MAIL, [RECEIVER_MAIL, SENDER_MAIL], message.as_string()))
