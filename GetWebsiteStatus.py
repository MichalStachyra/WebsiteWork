import requests

url = "http://example.com"  # Replace with the URL of the website you want to download

try:
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the content of the response
        html_content = response.text
        
        # Save the content to a file
        with open("website_content.html", "w", encoding="utf-8") as file:
            file.write(html_content)
        
        print("Website content downloaded successfully!")
    else:
        print(f"Failed to download website content. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")
