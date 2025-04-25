import requests
import re

def extract_eaab_token(cookie):
    headers = {
        'Host': 'business.facebook.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'Cookie': cookie
    }

    try:
        print("\n[*] Connecting to Facebook Business endpoint...")
        response = requests.get("https://business.facebook.com/business_locations", headers=headers)

        # Search for EAAB token using regex
        match = re.search(r'EAAB\w+', response.text)
        if match:
            token = match.group(0)
            return token
        else:
            return None
    except Exception as e:
        print(f"[!] Error: {str(e)}")
        return None

def main():
    print("\n==============================")
    print("     EAAB Token Extractor")
    print("        by Broken Nadeem")
    print("==============================\n")

    cookie = input("[?] Paste your Facebook Cookie: ").strip()

    print("\n[*] Extracting EAAB token...")
    token = extract_eaab_token(cookie)

    if token:
        print("\n[+] Token Found!")
        print("EAAB Token:\n" + token)
    else:
        print("\n[-] Failed to extract token. Check your cookie or try again.")

if __name__ == "__main__":
    main()
