import os, requests, base64, time, json
from pystyle import Write, Colorate, Colors, Center

# CONFIG PATH
config_path = os.path.join(os.path.dirname(__file__), "config.json")

try:
    with open(config_path, 'r') as config_file:
        configuration = json.load(config_file)
except FileNotFoundError:
    print(f"Configuration file not found. Ensure it exists at: {config_path}")
    exit(1)

ROBLO_SECURITY = configuration.get(".ROBLO_SECURITY")
UID = configuration.get("userID")

userInput = Write.Input("Choice$ ", Colors.white_to_blue, interval=0.025)

if userInput == 'robux' or userInput == 'rbx':
    path = f"/v1/users/{UID}/currency"
else:
    path = userInput 
headers = {
    "authority": "economy.roblox.com",
    "method": "GET",
    "path": path,
    "scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cookie": f".ROBLOSECURITY={ROBLO_SECURITY}",
    "origin": "https://www.roblox.com",
    "referer": "https://www.roblox.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"
}
url = f"https://economy.roblox.com{path}"
response = requests.get(url, headers=headers)
os.system("cls")
robux = response.json()
prbx = robux['robux']
print(prbx)
input("Relaunch..")
##