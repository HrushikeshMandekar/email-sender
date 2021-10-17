# NOTE: To sent the mail from code, you need to go to the google account setting of that mail id and then type 'Less secure app access' this in that search bar, then you will redirect to it and then turn on the option.

import smtplib
from email.message import EmailMessage

email = EmailMessage() # created email class object
email['from'] = 'sender_name'
email['to'] = 'sender_mailid@gmail.com'
email['subject'] = 'write your subject here'

email.set_content('The content which you like to send, write here!')

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    # host from which service you are going to send mail and port can be found on google of that service.
    
    smtp.ehlo() # .ehlo()  is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email.
    smtp.starttls() # tls is an encryption mechanism, so that you can connect to the server securly
    smtp.login('yourMailId@gmail.com', 'YourMailIdPassword')
    smtp.send_message(email)
    print("Message Sent Successfully! :)")