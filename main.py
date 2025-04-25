import requests
import json
import time

# Function to extract token from the cookie
def extract_token_from_cookie(cookie):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Content-Type': 'application/json',
    }

    # Facebook Graph API URL for extracting token
    url = 'https://graph.facebook.com/v15.0/me?access_token=' + cookie

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        user_data = response.json()
        return user_data['id'], user_data['name']
    else:
        print("Error extracting token or invalid cookie.")
        return None, None

# Function to send message to Facebook conversation using the token
def send_message(token, convo_id, message):
    url = f'https://graph.facebook.com/v15.0/{convo_id}/messages'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    # Payload for sending message
    data = {
        'message': {
            'text': message
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.text}")

# Main function to execute the process
def main(cookie, convo_id, message):
    print("Extracting token from cookie...")
    token, user_name = extract_token_from_cookie(cookie)

    if token:
        print(f"Token successfully extracted for user: {user_name}")
        print(f"Sending message to conversation ID: {convo_id}")
        send_message(token, convo_id, message)
    else:
        print("Failed to extract token. Check the cookie and try again.")

# Script execution starts here
if __name__ == "__main__":
    # Input the cookie, conversation ID and the message
    cookie = input("Enter your Facebook cookie: ")
    convo_id = input("Enter the Conversation ID (e.g., 123456789012345): ")
    message = input("Enter the message to send: ")

    main(cookie, convo_id, message)
