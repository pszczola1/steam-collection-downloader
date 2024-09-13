### About
This is a python script that allows you to download an entire steam mod collection using steamcmd

### Requirements
You need [steamcmd](https://developer.valvesoftware.com/wiki/SteamCMD#Downloading_SteamCMD), Python3 and modules listed in requirements.txt

### Usage
1. Copy the collection id, you can find it at the end of the link to the collection
2. Open command prompt in the folder with the script
3. Run the script: `python3 main.py [<collection id>] [<login(or 'anonymous')>] [<password>] [<steam guard code>]`, games on [this list](https://steamdb.info/sub/17906/apps/) will work without login, the rest will probably require signing in with an account **that owns the game**
   
## Important
- You'll probably have to change steamcmd.exe location on line 31 in the script
- Sometimes steamcmd fails to download a mod for some reason, check if the number of files you've downloaded is equal to the number of mods in the collection
- Logging in is required **only** when the anonymous account doesn't allow you to download the mods to your game. It's the developer's choice, blame them
- The script only sends requests to steamcommunity.com and uses your password to login to steamcmd, it won't steal your data 