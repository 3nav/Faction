import os
import time
import string
import random

random_title = ''.join(random.choice(string.ascii_letters) for _ in range(15))
os.system(f"title {random_title}")

from colorama import init
from gradient import gradient
from snipe import snipeLoop
init()

LOGO = """\n
    ███████╗ █████╗  ██████╗████████╗██╗ ██████╗ ███╗   ██╗    ██████╗  ██████╗ 
    ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██║██╔═══██╗████╗  ██║   ██╔════╝ ██╔════╝ 
    █████╗  ███████║██║        ██║   ██║██║   ██║██╔██╗ ██║   ██║  ███╗██║  ███╗
    ██╔══╝  ██╔══██║██║        ██║   ██║██║   ██║██║╚██╗██║   ██║   ██║██║   ██║
    ██║     ██║  ██║╚██████╗   ██║   ██║╚██████╔╝██║ ╚████║██╗╚██████╔╝╚██████╔╝
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝ ╚═════╝  ╚═════╝ 
"""

OPTIONS = """
    ╔══════════════════════════════════════════════════════╗
    ║                 OPTIONS                              ║
    ╠══════════════════════════════════════════════════════╣
    ║   ▸ 1) 4 Letters (lowercase)                         ║
    ║   ▸ 2) 5 Letters (lowercase)                         ║
    ║   ▸ 3) Words combination                             ║
    ║   ▸ 4) Random letters                                ║
    ║   ▸ 5) Letters & Numbers combination                 ║
    ║   ▸ 6) 4 Numbers					   ║
    ╚══════════════════════════════════════════════════════╝
"""

logoGradient = gradient((166, 98, 245), (66, 39, 97), LOGO)
optionsGradient = gradient((66, 39, 97), (166, 98, 245), OPTIONS)

def start():
    global currentToken

    print(logoGradient)
    print(optionsGradient)
    print("\033[38;2;217;0;83m    You can get rate-limited, so beware and try not to send a lot of requests.")
    
    #if currentToken == None:
    #    xcsrftoken = input("\033[38;2;166;98;245m    X-Csrf-Token ▸ ")
    #    currentToken = xcsrftoken
    #else:
    #    print("\033[38;2;166;98;245m    Already got X-Csrf-Token, continuing process.")

    wordLength = None

    selectOption = int(input("\033[38;2;166;98;245m    Select Option ▸ "))
    if selectOption == 5:
        wordLength = int(input("\033[38;2;166;98;245m    Select Length ▸ "))
    rangeBetween = int(input("\033[38;2;166;98;245m    Select Range ▸ "))

    nameTable = snipeLoop(rangeBetween, selectOption, wordLength)
    if len(nameTable) >= 1:
        print(f"\033[38;2;166;98;245m    Got Usernames")
        for name in nameTable:
            print(f"    ▸ {name}")
        input("\033[38;2;166;98;245m    Press enter to go back.")
        os.system("cls")
        start()
    else:
        print("\033[38;2;217;0;83m    No usernames got, retry in 2 seconds.")
        time.sleep(2)
        os.system("cls")
        start()

if __name__ == "__main__":
    start()