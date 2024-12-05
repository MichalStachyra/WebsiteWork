import requests
from bs4 import BeautifulSoup

# User credentials
username = 'your_username'
password = 'your_password'
item_url = 'http://example.com/item'  # Replace with the URL of the item

# Prices threshold
price_threshold = 100.0

# Login details
login_url = 'http://example.com/login'  # Replace with the actual login URL
buy_url = 'http://example.com/buy'  # Replace with the URL for the purchase endpoint

# Create a session
session = requests.Session()

# Login payload
login_payload = {
    'username': username,
    'password': password
}

# Log in to the website
login_response = session.post(login_url, data=login_payload)
if login_response.status_code == 200:
    print("Login successful!")

    # Check the item price
    item_response = session.get(item_url)
    if item_response.status_code == 200:
        soup = BeautifulSoup(item_response.text, 'html.parser')
        
        # Find the price element (adjust selector as needed)
        price_element = soup.find("span", {"class": "price"})
        
        if price_element:
            price = float(price_element.text.strip().replace('$', ''))
            print(f"Current price: ${price}")
            
            if price < price_threshold:
                # Prepare buy payload
                buy_payload = {
                    'item_id': 'item_id_from_page',  # Adjust according to the page structure
                    'quantity': 1
                }
                
                # Make the purchase
                buy_response = session.post(buy_url, data=buy_payload)
                if buy_response.status_code == 200:
                    print("Purchase successful!")
                else:
                    print(f"Failed to purchase the item. Status code: {buy_response.status_code}")
            else:
                print("Price is above the threshold.")
        else:
            print("Price element not found on the item page.")
    else:
        print(f"Failed to access the item page. Status code: {item_response.status_code}")
else:
    print(f"Failed to log in. Status code: {login_response.status_code}")
