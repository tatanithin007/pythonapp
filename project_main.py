

import requests 
from bs4 import BeautifulSoup 
result = ""
URL = "https://in.bookmyshow.com/buytickets/syeraa-narasimha-reddy-hyderabad/movie-hyd-ET00055035-MT/20191002"
r = requests.get(URL) 
soup = BeautifulSoup(r.text, 'html.parser')
artist_name_list = soup.find_all('a', class_='__venue-name')
for artist_name in artist_name_list:
    names = artist_name.contents
    if ('PVR' in str(names[1])):
        result="available"
    print(names)

    
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''Hello,
tickets released for PVR
'''
#The mail addresses and password
sender_address = 'abhiramtata1995@gmail.com'
sender_pass = 'Nithu2211#'
receiver_address = 'tatanithin007@gmail.com;ruhansharief22@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
if ("available" in result):
 session.sendmail(sender_address, receiver_address, text)
 print('Mail Sent')
session.quit()

