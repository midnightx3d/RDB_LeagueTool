"""
This function is unfinished but this will be very important thing for league structure

TO DO :
all main functions
"""
from itertools import count
import sys
import os
import json
import colorama
import sqlite3
import uuid
import pycountry

from pathlib import Path
from datetime import datetime
from tabulate import tabulate

import rnw_main
from licensemgr import view_license_list

#datavase :)
database_folder = Path("databases")
database_file = Path("datanetwork.db")

database_path = database_folder / database_file

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
                rnw_main.clr_menu() #Finished MAYBE?
                usr_name = input("Input user Real Name* : ")
                usr_nickname = input("Input user Nickname* : ")
                usr_steamid = int(input("Input user steamid64* : "))
                print("Add user discord id?")
                choice = input("YES / NO : ").strip().lower()
                if choice == "yes":
                    usr_discordid = int(input("Input user DiscordID : "))
                
                else : usr_discordid = 0
                choice = None

                print("Add user nationality?")
                choice = input("YES / NO : ").strip().lower()
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
                view_userlist() #FINISHED
            case "3" :
                rnw_main.clr_menu()
                edit_user_menu()
            case "4" :
                rnw_main.clr_menu()
                delete_user()
            case "0" | "exit" :
                rnw_main.clr_menu()
                return
            case _:
                rnw_main.clr_menu()
                print("Error : 1 : Wrong Input : Function only takes number or \"exit\"")

def gen_user_id():
    if database_path.exists():
        global user_uuid
        user_uuid = str(uuid.uuid4())[:6]
        con = sqlite3.connect(database_path)
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
    if database_path.exists:
        pass

    else :
        print("Database is Missing or broken ... RETURN 3.2.1...")
        return

    gen_user_id()

    con = sqlite3.connect(database_path)
    cur = con.cursor()

    # []=============[]
    # []DEFAULT SETUP[] YAV REMIND ME TO DO .txt for it later
    # []=============[] 

    user_lid = user_uuid
    regdate = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    idbrating_base = int(1250)
    safetyrating_base = int(1000)
    license_base = "000000"
    track_records_base = int(0)
    race_amount_base = int(0)
    wins_base = int(0)
    podiums_base = int(0)

    insertinfo = """INSERT INTO USER(userid , regdate , name , nickname , steamid , discordid , nationality , idbrating , safetyrating ,
     license , track_records , race_amount , wins , podiums , team ) VALUES (? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,? ,?)"""

    cur.execute(insertinfo,(user_lid , regdate , usr_name , usr_nickname , usr_steamid , usr_discordid , usr_nationality , idbrating_base , safetyrating_base ,
    license_base , track_records_base , race_amount_base , wins_base , podiums_base , usr_team ))

    con.commit()
        
    con.close()

    print("Succesfully added user with ID : ",user_lid)

def view_userlist():
    if database_path.exists():
        pass
    else :
        print("Error database doesnt exist ....")
        return

    con = sqlite3.connect(database_path)
    cur = con.cursor()

    cur.execute(f"SELECT userid , name , nickname , steamid , nationality , idbrating , safetyrating , license FROM USER")
    columns = [desc[0] for desc in cur.description]
    cur.execute(f"SELECT userid , name , nickname , steamid , nationality , idbrating , safetyrating , license FROM USER")
    data = cur.fetchall()

    print(tabulate(data, headers=columns, tablefmt="grid"))
    con.close()

def edit_user_menu():
    rnw_main.clr_menu()
    while True :
        print("====================")
        print("1. Edit Name")
        print("2. Edit NickName")
        print("3. Edit SteamID")
        print("4. Edit DiscordID")
        print("5. Edit Nationality")
        print("6. Adjust Rating")
        print("7. Adjust Safety Rating")
        print("8. Manage License.")
        print("9. Manage Team")
        print("0. Exit")
        print("====================")

        choice = str(input("Input : "))
        match choice:
            case "1" :
                rnw_main.clr_menu()
                edit_usrname()
            case "2" :
                rnw_main.clr_menu()
                edit_usrnickname()

            case "3" :
                rnw_main.clr_menu()
                edit_steamid()

            case "4" :
                rnw_main.clr_menu()
                edit_discordid()

            case "5" :
                rnw_main.clr_menu()
                edit_usrnationality()

            case "6" :
                rnw_main.clr_menu()
                edit_rating()

            case "7" :
                rnw_main.clr_menu()
                edit_SRating()

            case "8" :
                rnw_main.clr_menu()
                manage_usr_license()

            case "9" :
                rnw_main.clr_menu()
                usr_team()

            case "0" | "exit" :
                rnw_main.clr_menu()
                return
            case _:
                rnw_main.clr_menu()
                print("Wrong input ... Return....")
                return

def check_exist(user_lid): #this shit isnt working
    if database_path.exists():
        pass
    else :
        print("Error : ERR : Database does not exist")
        return
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    cur.execute("SELECT EXISTS (SELECT 1 FROM USER WHERE userid = ?)",(user_lid,))

    arexists = cur.fetchone()[0]

    if arexists:
        pass
    else :
        print("Error User Not Found : 404 TRALALA ....")
        con.close()
        edit_user_menu()

    con.close() #no this would work but I am and idiot

def validate_country(user_input):
    user_input = user_input.strip().lower()
    
    # Attempt to match alpha-2 code
    country = pycountry.countries.get(alpha_2=user_input.upper())
    if country:
        return country.name

    # Attempt to match full country name or official name
    for country in pycountry.countries:
        if user_input == country.name.lower():
            return country.name
        if hasattr(country, 'official_name') and user_input == country.official_name.lower():
            return country.name
    
    return None

def edit_usrname():
    view_userlist()
    if database_path.exists():
        pass
    else :
        print("Database doesnt exists...Return...")
        return
    
    con = sqlite3.connect(database_path)
    cur = con.cursor()

    user_lid = input("input user ID : ") # ADD CHECK FOR USRID 
    newUName = input("Input new User name : ")

    print("You sure you want to continue?")
    choice = input("YES/NO : ").strip().lower()
    match choice:
        case "yes" :
            pass
        case _:
            edit_user_menu()
    cur.execute("UPDATE USER SET name = ? WHERE userid = ?",(newUName,user_lid))
    con.commit()
    showdata = cur.execute("SELECT * FROM USER WHERE userid =?",(user_lid,)).fetchall()
    rnw_main.clr_menu()
    print("Name Has been updated : ")
    print(tabulate(showdata, tablefmt="grid"))
    con.close()

def edit_usrnickname():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        pass
    else :
        print("Database doesnt exists...Return...")
        return

    view_userlist()
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    #check if usr exist
    cur.execute("SELECT EXISTS (SELECT 1 FROM USER WHERE userid = ?)",(user_lid,))
    arexist = cur.fetchone()[0]
    if arexist:
        pass
    else :
        con.close()
        print("Error 404 Not Found CYA!")
        return

    newUNickname = input("Input new user Nickname : ")

    print("You sure you want to continue?")
    choice = input("YES/NO : ").strip().lower()
    match choice:
        case "yes" :
            pass
        case _:
            con.close()
            edit_user_menu()

    #cur.execute(f"SELECT * FROM USER LIMIT 0")
    #columns = [desc[0] for desc in cur.description]

    cur.execute("UPDATE USER SET nickname = ? WHERE userid = ?",(newUNickname,user_lid))    
    con.commit()
    showdata = cur.execute("SELECT * FROM USER WHERE userid =?",(user_lid,)).fetchall()
    rnw_main.clr_menu()
    print("Nickname Has been updated : ")
    print(tabulate(showdata, tablefmt="grid"))

    con.close()

def edit_steamid():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        pass
    else :
        print("Database doesnt exists...Return...")
        return
    
    view_userlist()
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    
    check_exist(user_lid)

    newUSteamID = int(input("Input new SteamID (INT ONLY!) : "))

    print("You sure you want to continue?")

    choice = input("YES/NO : ").strip().lower()
    match choice:
        case "yes" :
            pass
        case _:
            con.close()
            return
            edit_user_menu()
    
    cur.execute("UPDATE USER SET steamid = ? WHERE userid = ?",(newUSteamID,user_lid))

    con.commit()
    showdata = cur.execute("SELECT * FROM USER WHERE userid =?",(user_lid,)).fetchall()
    rnw_main.clr_menu()
    print("SteamID Has been updated : ")
    print(tabulate(showdata, tablefmt="grid"))

    con.close()

def edit_discordid():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        pass
    else :
        print("Database doesnt exists...Return...")
        return
    
    view_userlist()
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    
    check_exist(user_lid)

    newUDiscordID = int(input("Input new DiscordID (INT ONLY!) : "))

    print("You sure you want to continue?")

    choice = input("YES/NO : ").strip().lower()
    match choice:
        case "yes" :
            pass
        case _:
            con.close()
            edit_user_menu()
    
    cur.execute("UPDATE USER SET discordid = ? WHERE userid = ?",(newUDiscordID,user_lid))

    con.commit()
    showdata = cur.execute("SELECT * FROM USER WHERE userid =?",(user_lid,)).fetchall()
    rnw_main.clr_menu()
    print("DiscordID Has been updated : ")
    print(tabulate(showdata, tablefmt="grid"))

    con.close()

def edit_usrnationality():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        pass
    else :
        print("Database doesnt exists...Return...")
        return

    view_userlist()
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    check_exist(user_lid)

    #newUCountry = str(input("Input new user nationality : "))
    user_input = input("Type Country Name or Alpha-2 Code: ")
    country_name = validate_country(user_input)

    #print(country_name)

    print("Do you want to continue ? ")
    case_choice = input("YES/NO : ").strip().lower()
    match case_choice:
        case "yes":
            pass
        case _:
            con.close()
            edit_user_menu()

    cur.execute("UPDATE USER SET nationality = ? WHERE userid = ?", (country_name,user_lid))
    con.commit()
    print("New Driver nationality set to : ",country_name)
    con.close()



    # ADD REAL COUNTRIES CHECKER, DONE
def edit_rating():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        pass
    else :
        print("Database doesnt exists...Return...")
        return
    
    view_userlist()
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    current_rating = cur.execute("SELECT idbrating FROM USER").fetchone()
    check_exist(user_lid)

    print("<========>")
    print("1. Add Rating")
    print("2. Remove Rating")
    print("3. Input new Rating")
    print("0. Exit")
    print("<========>")

    choice = input("Input : ").lower()
    match choice :
        case "1":
            rnw_main.clr_menu()
            print("Current rating : ")
            print(current_rating[0])
            print("How much rating to add : ")
            add_r = int(input("Input (int only): "))
            print("Do you want to continue ? ")
            case_choice1 = input("YES/NO : ").strip().lower()
            match case_choice1:
                case "yes":
                    pass
                case _:
                    con.close()
                    edit_user_menu()
            new_rating = int(current_rating[0] + add_r)
            cur.execute("UPDATE USER SET idbrating = ? WHERE userid = ?",(new_rating,user_lid))
            con.commit()
            print("New Rating is : " , new_rating )
            pass
        case "2":
            rnw_main.clr_menu()
            print("Current rating : ")
            print(current_rating[0])
            print("How much rating to remove : ")
            rm_r = int(input("Input (int only): "))
            print("Do you want to continue ? ")
            case_choice2 = input("YES/NO : ").strip().lower()
            match case_choice2:
                case "yes":
                    pass
                case _:
                    con.close()
                    edit_user_menu()
            new_rating = int(current_rating[0] - rm_r)
            cur.execute("UPDATE USER SET idbrating = ? WHERE userid = ?",(new_rating,user_lid))
            con.commit()
            print("New Rating is : " , new_rating )

        case "3" :
            rnw_main.clr_menu()
            print("Current rating : ")
            print(current_rating[0])

            set_rating = int(input("Input rating to set : "))

            case_choice3 = input("YES/NO : ").strip().lower()
            match case_choice3:
                case "yes":
                    pass
                case _:
                    con.close()
                    edit_user_menu()

            cur.execute("UPDATE USER SET idbrating = ? WHERE userid = ?",(set_rating,user_lid))
            con.commit()
            print("New Rating is : " , set_rating )
            #idk if this works I hope it does
        case "0" | "exit" :
            con.close()
            edit_user_menu()
        case _:
            con.close()
            print("Error : Wrong Input !")
            edit_user_menu()



def edit_SRating():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
        pass
    else :
        print("Database doesnt exists...Return...")
        return
    
    view_userlist()
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    current_SRating = cur.execute("SELECT safetyrating FROM USER").fetchone()
    check_exist(user_lid)
    ########################################
    print("<========>")
    print("1. Add Rating")
    print("2. Remove Rating")
    print("3. Input new Rating")
    print("0. Exit")
    print("<========>")

    choice = input("Input : ").lower()
    match choice :
        case "1":
            rnw_main.clr_menu()
            print("Current Safety Rating : ")
            print(current_SRating[0])
            print("How much rating to add : ")
            add_sr = int(input("Input (int only): "))
            print("Do you want to continue ? ")
            case_choice1 = input("YES/NO : ").strip().lower()
            match case_choice1:
                case "yes":
                    pass
                case _:
                    con.close()
                    edit_user_menu()
            new_srating = int(current_SRating[0] + add_sr)
            cur.execute("UPDATE USER SET safetyrating = ? WHERE userid = ?",(new_srating,user_lid))
            con.commit()
            con.close()
            print("New Rating is : " , new_srating )
            pass


        case "2":
            #rnw_main.clr_menu()
            print("Current Safety Rating : ")
            print(current_SRating[0])

            print("How much rating to remove : ")
            rm_sr = int(input("Input (int only): "))

            print("Do you want to continue ? ")
            case_choice2 = input("YES/NO : ").strip().lower()
            match case_choice2:
                case "yes":
                    pass
                case _:
                    con.close()
                    edit_user_menu()

            new_SRating = int(current_SRating[0] - rm_sr)
            cur.execute("UPDATE USER SET safetyrating = ? WHERE userid = ?",(new_SRating,user_lid))
            con.commit()
            con.close()
            print("New Rating is : " , new_SRating )

        case "3" :
            rnw_main.clr_menu()
            print("Current rating : ")
            print(current_rating[0])

            set_SRating = int(input("Input rating to set : "))

            case_choice3 = input("YES/NO : ").strip().lower()
            match case_choice3:
                case "yes":
                    pass
                case _:
                    con.close()
                    edit_user_menu()

            cur.execute("UPDATE USER SET safetyrating = ? WHERE userid = ?",(set_SRating,user_lid))
            con.commit()
            con.close()
            print("New Rating is : " , set_SRating )
            #idk if this works I hope it does
        case "0" | "exit" :
            con.close()
            edit_user_menu()
        case _:
            con.close()
            print("Error : Wrong Input !")
            edit_user_menu()

def manage_usr_license():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
    else :
        print("Error : ERR : Database does not exist")
        return
    
    cur.execute(f"SELECT userid , name , nickname , nationality , license FROM USER")
    columns = [desc[0] for desc in cur.description]
    cur.execute(f"SELECT userid , name , nickname , nationality , license FROM USER")
    data_l = cur.fetchall()

    
    print(tabulate(data_l, headers=columns, tablefmt="grid"))
    user_lid = input("input user ID : ") # ADD CHECK FOR USRID
    
    check_exist(user_lid)
    print(view_license_list())

    usr_llicense = input("Input license to assign : ")
    # add check if license in the list later
    print("You sure you want to continue?")

    choice = input("YES/NO : ").strip().lower()
    match choice:
        case "yes" :
            pass
        case _:
            con.close()
            return
            edit_user_menu()
    
    cur.execute("UPDATE USER SET license = ? WHERE userid = ?",(usr_llicense,user_lid))
    con.commit()
    con.close()
    return

def usr_team():
    print("W.I.P")

def delete_user():
    if database_path.exists():
        con = sqlite3.connect(database_path)
        cur = con.cursor()
    else :
        print("Error : ERR : Database does not exist")
        return
    
    view_userlist()
    user_lid = input("input user ID : ")
    check_exist(user_lid)

    print("You sure you want to continue?")

    choice = input("YES/NO : ").strip().lower()
    match choice:
        case "yes" :
            pass
        case _:
            con.close()
            return
            edit_user_menu()
    
    cur.execute("DELETE FROM USER WHERE userid = ?",(user_lid,))
    con.commit()
    con.close()

    print("User with ID : " , user_lid , " was deleted !")
    return