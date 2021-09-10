#!/usr/bin/env python
# coding: utf-8

# In[31]:


from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint
import pymongo
import pandas as pd
import requests


# In[32]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[33]:


url = 'https://redplanetscience.com/'
browser.visit(url)


# In[34]:


html_news = browser.html
soup = BeautifulSoup(html_news, "html.parser")


# # NASA Mars News

# In[35]:


news_title = soup.find("div", class_ = "content_title").text
news_paragraph = soup.find("div", class_ = "article_teaser_body").text


# In[36]:


print(news_title)
print("-----------------------------------------")
print(news_paragraph)


# # JPL Mars Space Images - Featured Image

# In[52]:


url_spaceimage = "https://spaceimages-mars.com/"
browser.visit(url_spaceimage)


# In[53]:


img_html = browser.html
img_soup = BeautifulSoup(img_html, "html.parser")


# In[59]:


# Find image url to the full size
featured_image = img_soup.find("img", class_="headerimage fade-in")

# Display url of the full image
featured_image_url = f"https://spaceimages-mars.com/image/featured/mars3.jpg"
print("JPL Featured Space Image")
print("-----------------------------------------")
print(featured_image_url)


# # Mars Facts

# In[43]:


mars_facts_url = "https://galaxyfacts-mars.com/"
table = pd.read_html(mars_facts_url)
table[0]


# In[45]:


df = table[0]
df.columns = ["Facts", "Planet1", "Planet2"]
df.set_index(["Facts"])
df


# In[46]:


facts_html = df.to_html()
facts_html = facts_html.replace("\n","")
facts_html


# # Mars Hemispheres

# In[47]:


url_hemisphere = "https://marshemispheres.com/"
browser.visit(url_hemisphere)


# In[48]:


html_hemisphere = browser.html
soup = BeautifulSoup(html_hemisphere, "html.parser")


# In[51]:


# Scrape all items that contain mars hemispheres information
hemispheres = soup.find_all("div", class_="item")

# Create empty list
hemispheres_info = []

# Sign main url for loop
hemispheres_url = "https://marshemispheres.com/"

# Loop through the list of all hemispheres information
for i in hemispheres:
    title = i.find("h3").text
    hemispheres_img = i.find("a", class_="itemLink product-item")["href"]
    
    # Visit the link that contains the full image website 
    browser.visit(hemispheres_url + hemispheres_img)
    
    # HTML Object
    image_html = browser.html
    web_info = BeautifulSoup(image_html, "html.parser")
    
    # Create full image url
    img_url = hemispheres_url + web_info.find("img", class_="wide-image")["src"]
    
    hemispheres_info.append({"title" : title, "img_url" : img_url})

# Display titles and images ulr
#hemispheres_info

# Or Display titles and images ulr this way
    print("")
    print(title)
    print(img_url)
    print("-----------------------------------------")


# In[ ]:




