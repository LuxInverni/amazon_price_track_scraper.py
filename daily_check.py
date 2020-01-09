import Amazon_Price_Track_API
import time

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'}
#User browser details, put in your own browser user-agent

def daily_checkURL, headers, desired_price):
    """ (product_URL, browser_headers, int) -> Email alert, string with current price and name of product.
    
    This function calls the main function once every 24 hours to scrap the 
    target product URL's for their price and if they hit a target price, send
    an email to the user to alert them of the sale price.
    
    """
    text = Amazon_Price_Track_API.main(URL, headers, desired_price)
    str1 = str(text[0]) + " " + str(text[1]) + " " + str(text[2])
    return str1


tuple_of_URLs_and_desired_prices = (('product URL', integer price in £),
                                    ('product URL', integer price in £),
                                    ('product URL', integer price in £),
                                    )

while True:
    for tup in tuple_of_URLs_and_desired_prices:
        print(daily_check(tup[0], headers, tup[1]))
    time.sleep(84400)  # Checks every 24 hours
