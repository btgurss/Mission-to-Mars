#!/usr/bin/env python
# coding: utf-8
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df
df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
test = "espn.com"
h = []
h.append({"name": "John", "url": test})
h

html = browser.html
img_soup = soup(html, 'html.parser')

Testing = img_soup.find_all('a', class_='itemLink product-item')
Test = Testing[1].get('href')
next_page = browser.find_by_css('a.product-item img')
print(Testing)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.\

#Creating a list of image titles by finding sections with h3 elements
image_title = img_soup.find_all('h3')

#Using for loop to count through the four pictures to collect
for i in range(4):
    
    #Parsing results with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    #Finding image title by pulling from list of titles
    final_title = image_title[i].get_text()
    
    #Clicking on the next page to collect jpeg information
    next_page = browser.find_by_css('a.product-item img')
    next_page.click()
    
    
    image = browser.links.find_by_text('Sample').first
    new_image_url = image['href']
    hemisphere_image_urls.append({'img_url':new_image_url, 'title':final_title})
    print(hemisphere_image_urls)
    
    #Going back to original webpage
    browser.visit(url)

Test_image = browser.find_by_tag('li')
Next = Test_image.first.find_by_tag('a')
Next.click()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()




