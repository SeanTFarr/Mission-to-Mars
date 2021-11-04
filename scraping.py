
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    # set news title and paragraph variables
    news_title, news_paragraph = mars_news(browser)

    img_url, title = hemi(browser)
    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "hemispheres": [{"img_url": img_url, "title": title}],
      "last_modified": dt.datetime.now()
    }
    
    # Stop webdriver and return data
    browser.quit()
    return data

# ### News Title and Paragraph

# Declare and define function
def mars_news(browser):
    
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # set up the HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        
    except AttributeError:
        return None, None
    
    return news_title, news_p


# ### Featured Images

# Declare and define function
def featured_image(browser):
    
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    #add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url


# ##Mars Facts

# Declare and define function
def mars_facts():
    
    #add try/except for error handling
    try:
        #  creating a dataframe from the HTML table
        # '.read_html()' searches for and returns a list of tables found in the HTML
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    # assign columns in the new database
    df.columns=['description', 'Mars', 'Earth']
    # turn the Description column into the DataFrame's index.updated index will remain in place
    df.set_index('description', inplace=True)

    # convert our DataFrame back into HTML-ready code, add bootstrap 
    return df.to_html(classes="table table-striped")

# ##Hemispheres

# Declare and define function
def hemi(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html
    hemisphere_image_urls = []
    for image in range (0, 4):
        browser.visit(url)
        hemisphere = browser.find_by_tag('h3')[image]
        hemisphere.click()
        html = browser.html
        hemi_soup = soup(html, 'html.parser')
        sample = hemi_soup.find('div', class_='downloads')
        hemisphere_image = sample.find('a').get('href')
        img_url = 'https://marshemispheres.com/' + hemisphere_image
        title = hemi_soup.find('h2', class_='title').get_text()
        hemispheres = {'image_url': img_url, 'title': title}
    if hemispheres not in hemisphere_image_urls:
        hemisphere_image_urls.append(hemispheres)

    return img_url, title


if __name__ == "__main__":

    # If running as script, print scraped data
    print(scrape_all())

