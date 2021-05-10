#!/usr/bin/env python
# coding: utf-8

# In[63]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
import os

driver = browser = webdriver.Chrome(executable_path="/home/sohaib/Documents/algo_trading/chromedriver_linux64/chromedriver")
driver.get("https://bitcoinaverage.com/en/bitcoin-price/btc-to-usd")
time.sleep(20)



# In[ ]:


import pandas as pd
output_dir = "/home/sohaib/Documents/algo_trading/dataframes/"


def store_data(price, date):
    '''
    Description:
        This fucntion help you out to store your scraped data to dataframe so that you can use it later.
        
    Input:
        price   (list) : Scrap prices list
        date    (list) : Date time on which data is scraped
        
    Output:
        No Output But will save data into the give output Dir path
    
    
    '''
    # making new file for every day
    dataframe_path = f"{output_dir}bitcoin_{datetime.today().strftime('%Y_%m_%d')}.csv"
    
    if os.path.isfile(dataframe_path):
        df = pd.read_csv(dataframe_path)
        if len(df) > 1000:
            previous_data   = df['date'].to_list()
            previous_prices = df['price'].to_list()
            date.extend(previous_data)
            price.extend(previous_prices)
        
    # Saving Dataframe
    df = pd.DataFrame({"date":date,"price":price})
    df.to_csv(dataframe_path)


prices, dates  = [], []
count =0
while 1:
    
    # Getting elements continously
    price = driver.find_element_by_xpath("//*[@id=\"mainDivForPage\"]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div[1]/span[1]")
    
    # Getting Current data and time
    now = datetime.now()
    
    # Getting Price of the bitcoin
    bitcoinPrice = price.text
    
    # Getting Date
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    # Appending information to string 
    prices.append(bitcoinPrice)
    dates.append(dt_string)
    
    print(f"price {bitcoinPrice}")
    print(f"price {dt_string}")
    
    count += 1
    # Saving Dataframe
    if count > 10:
        print("saving Dataframe")
        count =0
        store_data(prices, dates)
        prices, dates  = [], []
        
    time.sleep(1)
    
    
    


# In[ ]:




