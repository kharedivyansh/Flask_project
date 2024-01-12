from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Function to scrape YouTube data
def scrape_youtube():
    url = "https://www.youtube.com/watch?v=aQjg-ZZic0o"  # Replace with the actual YouTube video URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Attempt to find the title element
    title_element = soup.find('span', {'class': 'watch-title'})

    # Check if the title element is found
    if title_element:
        title = title_element.text.strip()
    else:
        title = "Title not found"

    # Attempt to find the description element
    description_element = soup.find('p', {'id': 'eow-description'})

    # Check if the description element is found
    if description_element:
        description = description_element.text.strip()
    else:
        description = "Description not found"

    return {'title': title, 'description': description}

# Function to scrape Amazon data
def scrape_amazon():
    url = "https://www.amazon.in/s?k=water+bottles&i=kitchen&rh=n%3A5925789031%2Cp_n_format_browse-bin%3A19560801031&_encoding=UTF8&content-id=amzn1.sym.4b814a1e-8ea3-427c-a234-6e45c73685df&pd_rd_r=d4d2ce02-ac65-44fb-bb20-997778548992&pd_rd_w=6dL9s&pd_rd_wg=1z0mu&pf_rd_p=4b814a1e-8ea3-427c-a234-6e45c73685df&pf_rd_r=2NR4FRZPEE80F48YEF68&ref=pd_gw_unk"  # Replace with the actual Amazon product URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Attempt to find the title element
    title_element = soup.find('span', {'id': 'productTitle'})

    # Check if the title element is found
    if title_element:
        title = title_element.text.strip()
    else:
        title = "Title not found"

    # Attempt to find the price element
    price_element = soup.find('span', {'id': 'priceblock_ourprice'})

    # Check if the price element is found
    if price_element:
        price = price_element.text.strip()
    else:
        price = "Price not found"

    return {'title': title, 'price': price}

# Route to display scraped data
@app.route('/')
def index():
    youtube_data = scrape_youtube()
    amazon_data = scrape_amazon()
    return render_template('index.html', youtube_data=youtube_data, amazon_data=amazon_data)

if __name__ == '__main__':
    app.run(host = "0.0.0.0")
