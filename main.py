import subprocess
import requests
import sys
from bs4 import BeautifulSoup

args = sys.argv[1:]
try:
    collection_id = args[0]
    login = args[1]
    if login != "anonymous":
        password = args[2]
        code = args[3]
except IndexError:
    print("Not enough arguments")
    print("[<collection id>] [<login(or 'anonymous')>] [<password>] [<steam guard code>]")
    exit()


page = requests.get(f"https://steamcommunity.com/sharedfiles/filedetails/?id={collection_id}")
soup = BeautifulSoup(page.content, 'html.parser')
anchors = soup.find_all("a", href=True)
links = []
for elem in anchors:
    if elem.parent.attrs.get("class") == ['workshopItem']:
        links.append(elem.attrs["href"])

links = list(filter(lambda link : "https://steamcommunity.com/sharedfiles/filedetails/?id=" in link, links))
ids = list(map(lambda l : l[l.index("=")+1:], links))

commands = []
commands.append("C:\steamcmd\steamcmd.exe")
commands.append(f"+login {login} {password} {code}")
for id in ids:
    commands.append(f"+workshop_download_item 255710 {id}")

cmd = subprocess.run(commands)
a = input()
