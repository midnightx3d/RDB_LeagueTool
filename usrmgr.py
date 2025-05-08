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
                usrname = input("Input user Real Name : ")
                usrnickname = input("Input user Nickname : ")
                usrdiscordid = input("Input user DiscordID : ")
                usrnationality = input("Input user Nationality : ")

                create_usr()
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
        print(user_uuid)
    else :
        print("Error : ERR : Database does not exist")
        return

def create_usr( usr_name , usrnickname , usrdiscordid , usrnationality ):

    gen_user_id()

    con = sqlite3.connect("datanetwork.db")
    cur = con.cursor()

    #cur.execute("""CREATE TABLE IF NOT EXISTS USER(userid, regdate, name , nickname, discordid , nationality , idbrating ,
    # safetyrating , license , track_records , races , wins , podiums , team )""")

    con.close()