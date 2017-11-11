#!/usr/bin/python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open('zabi.txt','r')
# Create a text/plain message
msg = MIMEText("zabi is a good boy")
#fp.close()

me = "zabi_ahmed@icloud.com" 
you = "zkhan0889@gmail.com"
msg['Subject'] = 'The contents of my life' 
msg['From'] = me
msg['To'] = you

 #Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('relay.apple.com')
s.sendmail(me, [you], msg.as_string())
s.quit()
