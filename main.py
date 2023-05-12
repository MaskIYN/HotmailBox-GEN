import requests
import json
import threading
import ctypes
from colorama import init, Fore, Back, Style
import sys
from time import sleep
from datetime import datetime
from pystyle import *
from pystyle import Add, Center, Colors, Colorate, Write, System
import time
import os
init()

lb = Fore.LIGHTCYAN_EX
lw = Fore.LIGHTWHITE_EX
w = Fore.WHITE
c = Fore.CYAN

def sprint(content: str, status: str = "c") -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(f"{c}[INFO] {current_time} | {content}{Fore.RESET}\n")

def sprint2(content: str, status: str = "c") -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    sys.stdout.write(f"{c}[GENERATED] {current_time} | {content}{Fore.RESET}\n")

os.system("title d0pe#6666")

#inputs
gang = r'''
                                        ██████╗  ██████╗ ██████╗ ███████╗
                                        ██╔══██╗██╔═══██╗██╔══██╗██╔════╝
                                        ██║  ██║██║   ██║██████╔╝█████╗  
                                        ██║  ██║██║   ██║██╔═══╝ ██╔══╝  
                                        ██████╔╝╚██████╔╝██║     ███████╗
                                        ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝
                                                HOTMAILBOX GEN                                                             
                                                Team Dope mask                      
                                       
'''

System.Size(120, 30)
System.Clear()
Anime.Fade(Center.Center(gang), Colors.purple_to_red, Colorate.Vertical, interval=0.030, enter=True)


lock = threading.Lock()
config = json.load(open("config.json"))
thread_count = config["Threads"]
api = config[f"API_Key"]
br = requests.get(f'https://api.hotmailbox.me/user/balance?apikey={api}')
if br.status_code == 200:
  data = br.json()
  balance = data['Balance']
  balance_usd = data['BalanceUsd']
  print(Fore.GREEN + f"INFO:")
  print(f"{c}[INFO] {lw}Balance (VND) --> {balance}")
  print(f"{c}[INFO] {lw}Balance (USD) --> {balance_usd}" + Style.RESET_ALL)
  print("")
else:
  print(Fore.RED + f"API call failed idk why" + Style.RESET_ALL)
amount = input(f"{c}[INPUT] {lw}Amount: ")
type = input(f"{c}[INPUT] {lw}Type: ")


os.system("cls")
class data: mails = 0; retry = 0
def buy_mails():
    while True:
        url = requests.get(f"https://api.hotmailbox.me/mail/buy?apikey={api}&mailcode={type}&quantity={amount}").json()
        try:
            for emailpass in url["Data"]["Emails"]:
                email = emailpass["Email"]; password = emailpass["Password"]
                with open("mails.txt", 'a') as f:
                    sprint2(f"{w}{email}|{password}|{type}")
                    lock.acquire()
                    lock.release()
                    f.write(f"{email}|{password}\n")
        except KeyError as e:()
for x in range(thread_count): threading.Thread(target=buy_mails).start()
sprint(f"{Fore.RED}Generating!")
sleep(5)
raise SystemExit()
