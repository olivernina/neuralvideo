from email.mime.text import MIMEText
from datetime import date
import smtplib

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
user=open('user','r')
SMTP_USERNAME = user.readline()
p= open('pass','r')
SMTP_PASSWORD = p.readline()

EMAIL_TO = [SMTP_USERNAME]
EMAIL_FROM = SMTP_USERNAME
EMAIL_SUBJECT = "Cluster Script "
DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

DATA='This is the content of the email for testing.'

def send(subject,data):
    msg = MIMEText(data)
    msg['Subject'] = subject #+ " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

if __name__=='__main__':
    send(EMAIL_SUBJECT,DATA)
