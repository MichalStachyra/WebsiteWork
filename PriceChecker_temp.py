import requests
from bs4 import BeautifulSoup

# URL of the product page
url = "http://example.com/product-page"  # Replace with the URL of the product page

# Send an HTTP GET request to the specified URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the price element (Update this to match the specific HTML structure of the website)
    price_element = soup.find("span", {"class": "product-price"})
    
    if price_element:
        # Extract the price text
        price = price_element.text.strip()
        print(f"Product price: {price}")
    else:
        print("Price element not found on the page.")
else:
    print(f"Failed to access the website. Status code: {response.status_code}")
