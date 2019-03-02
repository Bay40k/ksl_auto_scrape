import getdata
import smtplib
from config import config_options

server = smtplib.SMTP_SSL(config_options["mail_server"], config_options["mail_port"])

#Next, log in to the server
server.login(config_options["email"], config_options["email_password"])

#Send the mail
msg = "Subject: KSL Cars {}\n\n{}".format(getdata.retrieveData()[1], getdata.retrieveData()[0]) # The /n separates the message from the headers
server.sendmail(config_options["email"], config_options["email"], msg)