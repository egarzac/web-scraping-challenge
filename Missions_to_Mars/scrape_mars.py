#!/usr/bin/env python
# coding: utf-8

# In[421]:


# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd


# In[372]:

def scrape_info():
# URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'

# Retrieve page with the requests module
    response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')


# In[373]:


    print(soup.prettify())


# In[374]:


    results = soup.find_all('div', class_='content_title')
    results


# In[226]:


    title = []
    for each in results:
        soup.find_all('a')
        headlines = each.get_text()
        title.append(headlines)
    #print (each.text)
    title


# In[228]:


    links = ['/news/8749/nasa-readies-perseverance-mars-rovers-earthly-twin/',
         '/news/8716/nasa-to-broadcast-mars-2020-perseverance-launch-prelaunch-activities/',
        '/news/8695/the-launch-is-approaching-for-nasas-next-mars-rover-perseverance/',
         '/news/8692/nasa-to-hold-mars-2020-perseverance-rover-launch-briefing/',
         '/news/8659/alabama-high-school-student-names-nasas-mars-helicopter/',
         '/news/8645/mars-helicopter-attached-to-nasas-perseverance-rover/']
#https://mars.nasa.gov/news/8749/nasa-readies-perseverance-mars-rovers-earthly-twin/
    news_p =[]

    for link in links:
        url = f'https://mars.nasa.gov{link}'
#url
# Retrieve page with the requests module
        response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
        soup = BeautifulSoup(response.text, 'lxml')
        content = soup.find('meta', attrs={'name': 'description'})
        content.get_text()
        news_p.append(content)
    news_p


# In[229]:


    for i in range(6):
        print('----------------------------')
        print(title[i])
        print(news_p[i])


# In[230]:


    news = []

    for i in range(len(title)):
        news.append(title[i])
        news.append(news_p[i])


# In[231]:


    news


# In[365]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[366]:


    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


# In[367]:


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    container = soup.find_all('a', class_='button fancybox')
    container


# In[369]:


    href = '/spaceimages/images/mediumsize/PIA17449_ip.jpg'
    featured_image_url = f'https://www.jpl.nasa.gov{href}'
    featured_image_url


# In[408]:


# URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

# Retrieve page with the requests module
    response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'html.parser')


# In[416]:


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


# In[417]:


    url = 'https://twitter.com/marswxreport?lang=en'.format()
    browser.visit(url)


# In[396]:


    print(soup.prettify())


# In[418]:


    tweet = soup.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    tweet


# In[ ]:


    mars_weather = 'InSight sol 636 (2020-09-10) low -94.6C (-138.2F) high -17.1C (1.2F) winds from the W at 7.3 m/s (16.4 mph) gusting to 20.9 m/s (46.8 mph) pressure at 7.80 hPa'


# In[475]:


    url = 'https://space-facts.com/mars/'


# In[476]:


    tables = pd.read_html(url)
    full_table = ['Equatorial Diameter:', 'Polar Diameter:', 'Mass:', 'Moons:', 'Orbit Distance:', 'Orbit Period:', 'Surface Temperature:', 'First Record:', 'Recorded By:']
    tables


# In[477]:


    df = tables[0]
    df.columns = ['facts', 'data']
    df


# In[478]:


    df.set_index('facts', inplace=True)
    df


# In[479]:


    for facts in full_table:
        print(facts, df.loc[facts].data)


# In[480]:


    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg"},
        {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
        {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg"},
        {"title": "Valles Marineris Hemisphere", "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"}
        ]


# In[ ]:
    mars_data = {
    "News":news,
    "Mars Weather": mars_weather,
    "Image":featured_image_url,
    "Hemispheres":hemisphere_image_urls
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_data
