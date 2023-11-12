# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

# Connect to website

URL='https://www.amazon.in/Urbano-Fashion-Printed-T-Shirt-aopleaffull-drgreen-l/dp/B08JQKJ5FH/ref=sr_1_7?crid=258V266WIWB5L&keywords=t+shirt&qid=1699802032&sprefix=t+shir%2Caps%2C216&sr=8-7'

headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",  "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page=requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

title = soup2.find(id="productTitle").get_text()

price=soup2.find('span',{"class":"a-price-whole"}).text

title=title.strip()
price=price.strip()
today = datetime.date.today()

import csv

header=['Title','Price','Date']
data=[title,price,today]

#w=write
#newline is everything starts in newline?

# with open("AmazonWebScraperDataset.csv","w", newline="",encoding='UTF8') as f:
#     writer=csv.writer(f)
#     writer.writerow(header) #heding for csv columns
#     writer.writerow(data)   #inserting data in row


import pandas as pd

pd.read_csv(r'C:\Users\SomaVamsi\JupyterNoteBooks\AmazonWebScraperDataset.csv')


#after initial insertion of header and 1st row we shall start appending with a+

with open("AmazonWebScraperDataset.csv","a+", newline="",encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(data)   #inserting data in row



def check_price():
    URL='https://www.amazon.in/Urbano-Fashion-Printed-T-Shirt-aopleaffull-drgreen-l/dp/B08JQKJ5FH/ref=sr_1_7?crid=258V266WIWB5L&keywords=t+shirt&qid=1699802032&sprefix=t+shir%2Caps%2C216&sr=8-7'

    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",  "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page=requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

    title = soup2.find(id="productTitle").get_text()

    price=soup2.find('span',{"class":"a-price-whole"}).text

    title=title.strip()
    price=price.strip()
    today = datetime.date.today()

    import csv

    header=['Title','Price','Date']
    data=[title,price,today]

    with open("AmazonWebScraperDataset.csv","a+", newline="",encoding='UTF8') as f:
        writer=csv.writer(f)
        writer.writerow(data)   #inserting data in row
        
    if (price<20):
        send_mail()
        

# while(True):
#     check_price()
#     time.sleep(86400) #for every 5 sec the entire process runs again


import pandas as pd

df = pd.read_csv(r'C:\Users\SomaVamsi\JupyterNoteBooks\AmazonWebScraperDataset.csv')

print(df)

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('somac196@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'somac196@gmail.com',msg)