import requests # http requests

from bs4 import BeautifulSoup # Web Scraping
# Send the mail
import smtplib
# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# System data and time manipulation
import datetime
now = datetime.datetime.now()

# Email content placeholder
content = ''

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = ''
    cnt +=('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>\n')
    response = requests.get(url)
    content  = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in  enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-----------<br>')
content += ('<br><br>End of Message')
print(content)

# Lets send the email
print('Composing Email...')

# Update your email details
# Added a little code here to not share the email and password on Github
filename = 'info.txt' # Will be ignored by Github
txtfile  = open(filename,"r")
info = [] # Will store the necessary info
for line in txtfile:
   nL = line.replace("\n","")
   info.append(nL)

SERVER = 'smtp.gmail.com' # "your smtp server"
PORT = 587
FROM = info[0]
TO   = info[1]
PASS = info[2]

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories in HN ' + str(now.day) + '-' + str(now.month)
msg['From']    = FROM
msg['To']      = TO

msg.attach(MIMEText(content, 'html'))

print('Initiating server...')

server = smtplib.SMTP(SERVER, PORT)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email sent...')

server.quit()
