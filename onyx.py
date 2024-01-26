import requests
import discord
import os

banner = """

  /$$$$$$                               
 /$$__  $$                              
| $$  \ $$ /$$$$$$$  /$$   /$$ /$$   /$$
| $$  | $$| $$__  $$| $$  | $$|  $$ /$$/
| $$  | $$| $$  \ $$| $$  | $$ \  $$$$/ 
| $$  | $$| $$  | $$| $$  | $$  >$$  $$ 
|  $$$$$$/| $$  | $$|  $$$$$$$ /$$/\  $$
 \______/ |__/  |__/ \____  $$|__/  \__/
                     /$$  | $$          
                    |  $$$$$$/          
                     \______/           




Welcome to Onyx.
Coded by me - Midwuu
Any questions you got? add me and ill most likely respond
_____________________________________________________________________
"""

os.system("cls")
print(banner)
print("[1] Clear")
print("[2] Help")   
print("[3] Discord Webhook Deleter")
print("[4] Discord Webhook Spammer")
print("[5] Discord Token Server Joiner")
print("[6] Discord Bot Activator")
print("[7] Discord Token Checker")
print("[8] Quit")
surum = int(input("\nSelect Your Action: "))

if surum == 1:
  os.system("cls")
  print(banner)

elif surum == 2:
  os.system("cls")
  print("[1] Clear")
  print("[2] Help")   
  print("[3] Discord Webhook Deleter")
  print("[4] Discord Webhook Spammer")
  print("[5] Discord Token Server Joiner")
  print("[6] Discord Bot Activator")
  print("[7] Discord Token Checker")
  print("[8] Quit")

elif surum == 3:
    os.system("cls")
    print(banner)
    vblink = input("Enter Webhook Url:")
    requests.delete(vblink)
    print("Webhook Deleted Successfully.")

elif surum == 4:
  os.system("cls")
  print(banner)
  kacdefagonderildi = 0
  url = input("Enter Webhook URL: ")
  isim = input("Enter Webhook Name: ")
  avatarurl = input("Enter Webhook Avatar Url: ")
  mesaj = input("Enter Message: ")
  while True:
    bilgiler = {
        "username": isim,
        "avatar_url": avatarurl,
        "content": mesaj
    }
    requests.post(url, data=bilgiler)
    kacdefagonderildi = kacdefagonderildi + 1
    print(str(kacdefagonderildi) + " Messages Send!")

elif surum == 5:
  os.system("cls")
  print(banner)
  link = input('Discord Invite Link: ')
  apilink	= "https://discord.gg/" + str(link)
  print(link)
  with open('tokens.txt','r') as handle:
    tokens = handle.readlines()
    for x in tokens:
      token = x.rstrip()
      headers={
          'Authorization': token
        }
      requests.post(apilink, headers=headers)
      print("Token has officially joined server.")

elif surum == 6:
    os.system("cls")
    print(banner)
    bottoken = input('Enter Your Bot Token: ')
    client = discord.Client()
    client.run(bottoken)
    print("Discord Bot Activated Successfully.")

elif surum == 7:
    os.system("cls")
    print(banner)
    with open("tokens.txt") as f:
        for line in f:
            tokenn = line.strip("\n")
            headerss = {'Content-Type': 'application/json', 'authorization': tokenn}
            url = "https://discordapp.com/api/v6/users/@me/library"
            r = requests.get(url, headers=headerss)
            if r.status_code == 200:
                print("{} this token works.".format(line.strip("\n")))
            else:
                print("{} this token dosent work.")

elif surum == 8:
    quit()

else:
  pass	
