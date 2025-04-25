import os import time import datetime

Tool Information

developer = "CHANDU KHAN" brothers = ["SHAHIL SURYA"] github = "ASADO787" version = "9.6.3" tool_name = "CONVO OFFLINE" facebook = "https://www.facebook.com/being.chandu.khan" whatsapp = "+917761888399"

System Info

country = "IN" region = "Bihar" city = "Patna"

Token File Path

def get_token_file(): return "/storage/emulated/0/5id_ahmad_to_sanni.txt"

def show_header(): os.system("clear") print(""" ██████  ███████ ███████ ████████ ██      ██ ███    ██ ███████ ██       ██      ██         ██    ██      ██ ████   ██ ██
██   ███ █████   ███████    ██    ██      ██ ██ ██  ██ █████
██    ██ ██           ██    ██    ██      ██ ██  ██ ██ ██
██████  ███████ ███████    ██    ███████ ██ ██   ████ ███████

< INFORMATION >
[DEVELOPER]    =>  {developer}
[BROTHERS]     =>  {brothers[0]}
[GITHUB]       =>  {github}
[VERSION]      =>  {version}
[TOOL'S NAME]  =>  {tool_name}
[FACEBOOK]     =>  {facebook}
[WHATSAPP]     =>  {whatsapp}

< YOUR INFO >
[TODAY TIME]   =>  {datetime.datetime.now().strftime('%I:%M %p')}
[TODAY DATE]   =>  {datetime.datetime.now().strftime('%d/%B/%Y')}

< COUNTRY ~ >
[COUNTRY]      =>  {country}
[REGION]       =>  {region}
[CITY]         =>  {city}

< NOTE >
Tool Paid Monthly ₹250
Tool Paid 1 Year ₹2000
""")

def show_menu(): print(""" < CONVO > [1] Start Loader [2] Stop Loader [3] Show All Loader [4] Token Generate [5] Exit """)

def load_tokens(): path = get_token_file() if not os.path.exists(path): print("[!] Token file not found:", path) return [] with open(path, "r") as f: tokens = [line.strip() for line in f if line.strip()] return tokens

def show_tokens(tokens): for idx, token in enumerate(tokens, 1): name = token.split("|")[-1] if "|" in token else f"User {idx}" print(f"Token {idx}: [✓] Account Name - {name}")

def main(): show_header() show_menu() choice = input("[?] Choose an option: ")

if choice == '1':
    print("\n    ↳ 🌐 Tool Running📶")
    key = "OFFLINE_CONVO-cfg1740ccd1e63b99db2b8492d6aea04d91300252bb92ebee72dc108685c1feace19pm"
    print(f"\n    your key=> {key}")
    print("\n    [✓] your approval successfull.")
    print("\n    < Host >")
    print("    Connecting to termux terminal secure network... Please wait...")
    print(f"    [ {datetime.datetime.now().strftime('%H:%M %d-%b-%y')} 0:bash* localhost tcp://223.228.226.225:8080")
    time.sleep(2)
    print("\n[+] Enter Token File =>", get_token_file())
    tokens = load_tokens()
    show_tokens(tokens)

elif choice == '2':
    print("\n[+] Loader stopped.")
elif choice == '3':
    print("\n[+] Showing all loaders...")
    print("Loader 1: Patna_Network")
    print("Loader 2: Secure_Termux")
    print("Loader 3: Offline_Gang")
elif choice == '4':
    print("\n[+] Token generation started...")
    print("[✓] Token created successfully: EAAB...Fake_Token")
elif choice == '5':
    print("\n[!] Exiting tool. Goodbye!")
    exit()
else:
    print("\n[!] Invalid option. Try again.")

input("\n[+] Press Enter to return to menu...")
main()

if name == 'main': main()

