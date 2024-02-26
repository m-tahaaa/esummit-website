import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
from email.message import EmailMessage
from email.utils import make_msgid

def mail(email, otp):
    myEmail = 'sharmarishav676@gmail.com'
    password = 'tobvfkbjlcudrxnh'
    msg = EmailMessage()
    msg.set_content(f'''Your otp is {otp}''')
    msg['From'] = myEmail
    msg['To'] = email
    msg['Subject'] = 'OTP'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(myEmail, password)
        server.send_message(msg)
        server.quit()
