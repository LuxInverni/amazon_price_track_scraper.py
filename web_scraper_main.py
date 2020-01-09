import requests
from bs4 import BeautifulSoup
import smtplib

def check_price(URL, headers):
    """ (URL of product, Browser headers) -> (Float Value)

    Checks price of Amazon product, returns a float value.
    The URL is the URL of the product, the headers is user browser request headers

    """
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[:-3]# -3 removes the .99 pence value from product
    float_price = ''
    for c in converted_price:
        if c.isdigit():
            float_price = float_price + c
            #loop that removes the £$,. from product so the string can convert to float correctly
    return float(float_price)

def check_title(URL, headers):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="productTitle").get_text()
    return title.strip()

def send_mail(URL):

    '''   (URL of product) -> (Email to user)
    
    Send an Email to user once price condition is met.
    
    '''
    
    # Login and server details
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('useremail@here.com', 'password')#'User email to send email from', 'app password')

    #Email content details
    subject = 'Price fell down!'
    body = f'Check the Amazon link {URL}'
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('useremail@here.com', 'customeremail@here.com', msg)#(Email sent from, sends to, msg)

    print('Mail Sent!')#confirmation on terminal that mail was sent
    server.quit

def main(URL, headers, desired_price):
    ''' (Product URL, Browser headers, Desired Price) ->> (Float, Email)

    Main function, takes product URL, Browser headers and desired price of product.
    If the price drops below the desired price, an email is send to user.
    Checks once a day.
    
    '''
    if check_price(URL, headers) < desired_price:
        send_mail(URL)
    return (check_price(URL, headers)), "for",(check_title(URL, headers))
