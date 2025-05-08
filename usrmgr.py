from itertools import count
import sys
import os
import json
import colorama
import sqlite3
import uuid

from pathlib import Path
from datetime import datetime
from tabulate import tabulate

import rnw_main
from licensemgr import view_license_list

database_file = Path("datanetwork.db")

def usr_menu():
    while True:
        print(">===============<")
        print("User Menu.")
        print("1. Add User")
        print("2. User List")
        print("3. Edit User")
        print("4. Delete User")
        print("0. Exit ")
        print(">===============<")

        choice = input("Input : ")
        match choice:
            case "1" :
                rnw_main.clr_menu()
                usr_name = input("Input user Real Name* : ")
                usr_nickname = input("Input user Nickname* : ")
                usr_steamid = int(input("Input user steamid64* : "))
                print("Add user discord id?")
                choice = input("YES / NO : ").strip()
                if choice == "yes":
                    usr_discordid = int(input("Input user DiscordID : "))
                
                else : usr_discordid = 0
                choice = None

                print("Add user nationality?")
                choice = input("YES / NO : ").strip()
                if choice == "yes":
                    usr_nationality = input("Input user Nationality : ")
                else :
                    usr_nationality="Globe"
                choice = None
                print("Assign Team?")
                print("this thing is still in developement right now it will assign NONE UwU")

                usr_team = "NONE"

                create_usr(usr_name,usr_nickname,usr_steamid,usr_discordid,usr_nationality,usr_team)

            case "2" :
                rnw_main.clr_menu()
                pass
            case "3" :
                rnw_main.clr_menu()
                pass
            case "4" :
                rnw_main.clr_menu()
                pass
            case "0" | "exit" :
                rnw_main.clr_menu()
                return
            case _:
                rnw_main.clr_menu()
                print("Error : 1 : Wrong Input : Function only takes number or \"exit\"")

def gen_user_id():
    database_file
    if database_file.exists():
        global user_uuid
        user_uuid = str(uuid.uuid4())[:6]
        con = sqlite3.connect("datanetwork.db")
        cur = con.cursor()
        db_l_id = cur.execute("SELECT userid FROM USER").fetchall()
        for i in range(len(db_l_id)):
            if user_uuid == any(db_l_id):
                user_uuid = None
                gen_user_id()
            else : pass
        #print(user_uuid)
    else :
        print("Error : ERR : Database does not exist")
        return

def create_usr( usr_name , usr_nickname , usr_steamid , usr_discordid , usr_nationality , usr_team ):
    database_file # I know its pointless 

    if database_file.exists:
        pass

    else :
        print("Database is Missing or broken ... RETURN 3.2.1...")
        return

    gen_user_id()

    con = sqlite3.connect("datanetwork.db")
    cur = con.cursor()

    # []=============[]
    # []DEFAULT SETUP[] YAV REMIND ME TO DO .txt for it later
    # []=============[] 

    user_lid = user_uuid
    regdate = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    idbrating_base = 1250
    safetyrating_base = 1000
    license_base = "000000"
    track_records_base = 0
    race_amount_base = 0
    wins_base = 0
    podiums_base = 0
    #team_base = "None"

    insertinfo = """INSERT INTO USER(userid , regdate , name , nickname , steamid , discordid , nationality , idbrating , safetyrating ,
     license , track_records , race_amount , wins , podiums , team ) VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?)"""

    cur.execute(insertinfo,(user_lid , regdate , usr_name , usr_nickname , usr_steamid , usr_discordid , usr_nationality , idbrating_base , safetyrating_base ,
    license_base , track_records_base , race_amount_base , wins_base , podiums_base , usr_team ))

    con.commit()
        
    con.close()

    print("Succesfully added user with ID : ",user_lid)