# NOTE: To sent the mail from code, you need to go to the google account setting of that mail id and then type 'Less secure app access' this in that search bar, then you will redirect to it and then turn on the option.

import smtplib
from email.message import EmailMessage
from string import Template 
from pathlib import Path    # Path is same as os.path

html = Template(Path('text.html').read_text())
# Using Template we can manipulate the variable
# Path is used to access the text.html file from this folder
# .read_txt() is use to read the text.html file
email = EmailMessage()
email['from'] = 'sender_name'
email['to'] = 'sender_mailid@gmail.com'
email['subject'] = 'write your subject here'

email.set_content(html.substitute({'name':'name_of_receiver'}), 'html')
# we used .substitute() to manipulate the variable $name which is inside text.html
# instead of (name = 'Danvir') we can also give it in dictionary format like ({'name':'Danvir'}) for the multiple attributes.
# specified 'html' format to specifiy the format so that it will give the required txt from that .html file

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo() 
    smtp.starttls() 
    smtp.login('yourMailId@gmail.com', 'YourMailIdPassword')
    smtp.send_message(email)
    print("Message Sent Successfully! :)")