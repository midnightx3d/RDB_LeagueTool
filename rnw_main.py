from shutil import unregister_archive_format
import sys
import os
import json
import sqlite3
#from turtle import color
import colorama

from pathlib import Path

import usrmgr
import licensemgr
'''
TO DO LIST :
- Main Menu ASCII
- User Menu ASCII
- Json Structures
'''

RNW_VERSION = ("a.0.0.1")

def main():
    create_database()
    fix_cmd_size()
    launch_ascii()
    about_me_info()

    menu_ascii()

def fix_cmd_size():
    cmd = 'mode 140,40'
    os.system(cmd)


def clr_menu():
    if sys.platform == "linux" or sys.platform =="linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system('cls')

def launch_ascii():
    f = open("asciiart.txt","r")
    colorama.just_fix_windows_console()
    print(colorama.Fore.GREEN , f.read())
    print(colorama.Back.RESET)
    print(colorama.Fore.RESET)

def about_me_info():
    print(colorama.Fore.BLUE + colorama.Back.YELLOW + "Developed by",colorama.Back.LIGHTYELLOW_EX + "[MiDNightX3D]\n")
    print(colorama.Fore.WHITE + colorama.Back.LIGHTBLUE_EX + "Current Version :" , colorama.Fore.RED + colorama.Back.BLUE + "[" , RNW_VERSION , "]\n")
    print(colorama.Fore.RESET + colorama.Back.RESET)
    #print(colorama.Back.LIGHTBLACK_EX)
    print("Welcome to RacingNetwork League Tool , this application is on version : " , RNW_VERSION , "\n")
    print("""    This is early developement buld so majority of functions may not work , or work incorrectly ,
    Currenly working functions is [About Me] [User Manager] [License Manager]... More Functions will be added with the updates .
    Current Version doesnt have User Intrface so to navigate trough this app you need to use numbers,
    like [0...99] or normal input for registration etc.
    """)

def create_database():
    database_file = Path("datanetwork.db")
    if database_file.exists():
        con = sqlite3.connect("datanetwork.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS LICENSE(licenseid, regdate, name, color, licensing_country)")
        cur.execute("""CREATE TABLE IF NOT EXISTS USER(userid, regdate, name , nickname, steamid , discordid , nationality , idbrating , 
        safetyrating , license , track_records , race_amount , wins , podiums , team )""")

        baseLcheck = cur.execute("SELECT EXISTS (SELECT 1 FROM LICENSE WHERE licenseid = '000000')").fetchone()[0] # this shit works somehow !
        #print(baseLcheck)
        if baseLcheck :
            pass
        else :
            print("Base License is not found ... Trying to genereate one ! ")
            licensemgr.createbasiclicense()

        pass
        #print("Database already exist")

        con = sqlite3.connect("datanetwork.db")
        cur.execute("CREATE TABLE IF NOT EXISTS LICENSE(licenseid, regdate, name, color, licensing_country)")
        con.commit()
        con.close()

    else : 
        print("Database not found , Creating...")
        

def menu_ascii():
    while True:
        print("Main Menu.")
        print(">===============<")
        print("1. About Me")
        print("2. User Menu")
        print("3. Team Menu")
        print("4. Car Menu")
        print("5. Track Menu")
        print("6. League Tool")
        print("7. Render Tool")
        print("8. License Manager")
        print("9. Database Manager")
        print("0. Exit")
        print(">===============<")

        choice = input("Input : ")

        match choice:
            case "1" :
                clr_menu()
                launch_ascii()
                about_me_info()
            case "2" :
                clr_menu()
                usrmgr.usr_menu()
            case "3" :
                clr_menu()
                pass
            case "4" :
                clr_menu()
                pass
            case "5" :
                clr_menu()
                pass
            case "6" :
                clr_menu()
                pass
            case "7" :
                clr_menu()
                pass
            case "8" :
                clr_menu()
                licensemgr.license_menu()
                pass
            case "9" :
                clr_menu()
            #exit
            case "0" | "exit" :
                exit()
            case _:
                clr_menu()
                print("Error : 1 : Wrong Input : Function only takes number or \"exit\"")



# Driver program
if __name__ == "__main__":
    sys.exit(int(main() or 0))