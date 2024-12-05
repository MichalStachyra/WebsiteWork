import requests

# URL of the login page
login_url = "http://example.com/login"  # Replace with the actual login URL
logout_url = "http://example.com/logout"  # Replace with the actual logout URL

# Login credentials
payload = {
    'username': 'your_username',
    'password': 'your_password'
}

# Create a session
session = requests.Session()

# Log in to the website
login_response = session.post(login_url, data=payload)

# Check if login was successful (status code 200)
if login_response.status_code == 200:
    print("Login successful!")

    # Perform actions as an authenticated user here (e.g., access protected pages)

    # Log out from the website
    logout_response = session.get(logout_url)

    if logout_response.status_code == 200:
        print("Logout successful!")
    else:
        print(f"Failed to log out. Status code: {logout_response.status_code}")
else:
    print(f"Failed to log in. Status code: {login_response.status_code}")
