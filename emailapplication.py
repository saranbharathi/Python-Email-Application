import smtplib
import email
import getpass
import imghdr
from email.message import EmailMessage

email_address = input('Mail Address : ')
email_password = getpass.getpass(prompt='Password : ')

subject = input('Subject : ')
body = input('Body : ')
receiver = 'sarankintern@gmail.com'
print('\nMessage sending to %s...'%receiver)

message = EmailMessage()
message['Subject'] = subject
message['From'] = email_address
message['To'] = receiver
message.set_content(body)

with open('taskdescription.PNG', 'rb') as att:
	file_data = att.read()
	file_type = imghdr.what(att.name)
	file_name = att.name

message.add_attachment(file_data, maintype = 'Image', subtype = file_type, filename = file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_address, email_password)
    smtp.send_message(message)

print('\nEmail sent successfully!!')
