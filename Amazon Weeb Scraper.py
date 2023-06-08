#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')
get_ipython().system('pip install bs4')
get_ipython().system('pip install msedge-selenium-tools')


# In[2]:


get_ipython().system('pip install chromedriver_binary')


# In[1]:


from selenium import webdriver
import chromedriver_binary

# for msedge
from msedge.selenium_tools import Edge, EdgeOptions
import csv


# In[2]:


driver=webdriver.Chrome()


# In[3]:


url='https://www.amazon.com/'
driver.get(url)


# In[12]:


def my_url(keyword):
    temp='https://www.amazon.com/s?k={}&ref=nb_sb_noss'
    keyword=keyword.replace(' ','+')
    return temp.format(keyword)


# In[19]:


url1=my_url('mobile phone')


# In[20]:


url1


# In[21]:


driver.get(url1)


# In[22]:


from bs4 import BeautifulSoup


# In[23]:


soup=BeautifulSoup(driver.page_source,'html.parser')


# In[24]:


soup


# In[25]:


soup_result=soup.find_all('div',{'data-component-type':'s-search-result'})


# In[26]:


len(soup_result)


# In[27]:


obj=soup_result[0]


# In[29]:


atag=obj.h2.a


# In[30]:


atag


# In[31]:


des=obj.h2.a.text.strip()


# In[32]:


des


# In[33]:


url='https://www.amazon.com/'+atag.get('href')


# In[34]:


parent=obj.find('span','a-price')


# In[35]:


price=parent.find('span','a-offscreen').text


# In[36]:


parent


# In[37]:


price


# In[43]:


rate=obj.find('span','a-icon-alt').text


# In[40]:


rate


# In[48]:


obj.find('span',{'class':'a-size-base'}).text


# In[47]:


obj.find_all('span',{'class':'a-size-base'})


# In[49]:


obj.find('img',{'class':'s-image'}).get('src')


# # Amazon Generic functions

# In[82]:


def my_url(keyword):
    temp='https://www.amazon.com/s?k={}&ref=nb_sb_noss'
    keyword=keyword.replace(' ','+')
    url=temp.format(keyword)
    url +='&page{}'
    return url

def extract_record(obj):
    atag=obj.h2.a
    description=obj.h2.a.text.strip()
    url='https://www.amazon.com/'+atag.get('href')
    try:
        parent=obj.find('span','a-price')
        price=parent.find('span','a-offscreen').text
    except AttributeError:
        return
    try:
        rate=obj.find('span','a-icon-alt').text
        count_review=obj.find('span',{'class':'a-size-base'}).text
    except AttributeError:
        rate=' '
        count_review=' '
    image=obj.find('img',{'class':'s-image'}).get('src')
    result=(description,price,rate,count_review,url,image)
    return result

def main1(keyword):
    driver=webdriver.Chrome()
    records=[]
    url=my_url(keyword)
    for page in range(1,21):
        driver.get(url.format(page))
        from bs4 import BeautifulSoup
        soup=BeautifulSoup(driver.page_source,'html.parser')
        soup_result=soup.find_all('div',{'data-component-type':'s-search-result'})
        
        for item in soup_result:
            record=extract_record(item)
            if record:
                records.append(record)
        with open("WebscrapResult3.csv",'w',newline='',encoding='utf-8') as f:
            writer1=csv.writer(f)
            writer1.writerow(['Description','Price','Rate','Count_Review','Url','Image'])
            writer1.writerows(records)
            
                
        
        
        
    
    
    


# In[83]:


main1('mobile phone')


# In[68]:





# In[70]:


import pandas as pd


# In[84]:


data=pd.read_csv("WebscrapResult3.csv")


# In[85]:


data.head()


# In[77]:


data


# In[87]:


data.Description[0]


# In[88]:


data.Url[0]


# In[89]:


data.Image[0]


# In[90]:


data.tail()


# In[92]:


data.sort_values(by='Count_Review',ascending=True)


# In[93]:


data.dtypes


# In[95]:


data['Count_Review']=data['Count_Review'].str.replace(',','')


# In[96]:


data


# In[97]:


data['Count_Review']=data['Count_Review'].astype(float)


# In[98]:


data.dtypes


# In[99]:


data.sort_values(by='Count_Review',ascending=True)


# In[100]:


data["Price"]=data["Price"].str.replace('$','')


# In[101]:


data


# In[103]:


data["Price"]=data["Price"].str.replace(',','')


# In[104]:


data


# In[106]:


data["Price"]=data["Price"].astype(float)


# In[107]:


data.Price.max()


# In[108]:


data.dtypes


# In[ ]:




