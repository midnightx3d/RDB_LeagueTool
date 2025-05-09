"""
With this you can add,edit,delete License for the database
There is menu function license_menu() that is cli 

many other functions... ugh they work but I think this code is not optimal and it can be optimized for good
for now this thing doesnt cause performance issues but when there is majority of the functions is done

REMINDERS : Add license sorting by class or prestige 

After project path changes all paths should be fixed? I hope <3
"""
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

#datavase :)
database_folder = Path("databases")
database_file = Path("datanetwork.db")

database_path = database_folder / database_file

#print("Database path:", database_path)

def license_menu():
	while True:
		print(">===============<")
		print("License Menu.")
		print("1. Add License")
		print("2. Edit License")
		print("3. View Licenses")
		print("4. Delete License")
		print("0. Exit")
		print(">===============<")

		choice = input("Input : ")
		match choice:
			case "1" :
				rnw_main.clr_menu()
				name = input("Input the name of your License : ")
				country = input("Input country that will issue your License : ")
				color = input("Input color of your license , supported colors [RED,GREEN,BLUE,GOLD,SILVER,BRONZE] : ")
				if name and country == "" :
					print("\n\nError : 1 : Input cannot be equal NULL \n\n")
					return

				add_license(name , country , color)

			case "2" :
				rnw_main.clr_menu()
				edit_license()
				return
			case "3" :
				rnw_main.clr_menu()
				view_license_list()
			case "4" :
				rnw_main.clr_menu()
				#view_license_list()
				delete_license()
				pass
			case "0" | "exit" :
				rnw_main.clr_menu()
				return
			case _:
				rnw_main.clr_menu()
				print("Error : 1 : Wrong Input : Function only takes number or \"exit\"")

def add_license(name , country , color):

	regdate = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

	# ADD CHECK IF DB EXISTS
	con = sqlite3.connect(database_path)
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS LICENSE(licenseid, regdate, name, color, licensing_country)")

	gen_license_id()

	insertr = """INSERT INTO LICENSE(licenseid, regdate, name, color, licensing_country) VALUES (?,?,?,?,?);"""

	cur.execute(insertr,(licenseid,regdate,name,color,country))
	con.commit()
	con.close()

	print("\nSuccesfully added License with id : " , licenseid)

def gen_license_id():
	if database_path.exists():
		global licenseid
		licenseid = str(uuid.uuid4())[:6]
		con = sqlite3.connect(database_path)
		cur = con.cursor()
		db_l_id = cur.execute("SELECT licenseid FROM LICENSE").fetchall()

		for i in range(len(db_l_id)):
			if licenseid == any(db_l_id):
				licenseid = None
				gen_license_id()
			

			else : pass

		#print(db_l_id,licenseid)
		#licenseid = None
		con.close()

	else:
		print("Error : ERR : Database does not exist")
		return

def view_license_list():
	if database_path.exists():
		con = sqlite3.connect(database_path)
		cur = con.cursor()
		
		cur.execute(f"SELECT * FROM LICENSE LIMIT 0")
		columns = [desc[0] for desc in cur.description]
		cur.execute(f"SELECT * FROM LICENSE")
		
		data = cur.fetchall()

		print(tabulate(data, headers=columns, tablefmt="grid"))
		
		con.close()

	else : 
		print("Error : ERR : Database does not exist")
		return

def createbasiclicense():
	database_path #idk why its there lol  I just place it here for fun fuck you 
	if database_path.exists:
		con = sqlite3.connect(database_path)
		cur = con.cursor()
		
		#gen_license_id()
		cname = "Common"
		regdate = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
		clid = "000000"
		ccolor = "Blue"
		ccountry = "Germany"

		commonlicense = """INSERT INTO LICENSE(licenseid, regdate, name, color, licensing_country) VALUES (?,?,?,?,?);"""

		cur.execute(commonlicense,(clid,regdate,cname,ccolor,ccountry))
		con.commit()
		con.close()

		print("Common License was created , Please DO NOT DELETE THIS LICENSE YOU WILL BREAK THE DATABASE!!!")

def delete_license():
	database_path
	if database_path.exists:
		con = sqlite3.connect(database_path)
		cur = con.cursor()


		view_license_list()
		print("DANGER ZONE!!!")
		del_choiceid = input("Input ID of the license you want to delete : ")
		cur.execute("SELECT EXISTS (SELECT 1 FROM LICENSE WHERE licenseid = ?)",(del_choiceid,))
		arexists = cur.fetchone()[0]
		if arexists:
			#print("Success!")
			pass
		else :
			print("Error : wrong license ID...")
			return

		print("input 0 or exit to cancel operation")
		issure = input("Print DELETE to delete the license : ")
		
		match issure:
			case "DELETE":
				cur.execute("DELETE FROM LICENSE WHERE licenseid = ?",(del_choiceid,))
				print("License with ID" , del_choiceid , " was succesfully deleted!")
				con.commit()
				pass
			case "0" | "exit" | "EXIT" :
				license_menu()
			case _:
				print("Wrong Input : RETURN")
				return
	else :
		print("Error : ERR : Database does not exist")
		return
	pass

def edit_license():
	if database_path.exists():
		con = sqlite3.connect(database_path)
		cur = con.cursor()

		print("Succesfully connected to the database! Ready to edit license parameters!")
		view_license_list()

        #input ID
		licenselid=str(input("Please Enter valid License ID : "))


		#check if license id exists
		cur.execute("SELECT EXISTS (SELECT 1 FROM LICENSE WHERE licenseid = ?)",(licenselid,))
		arexists = cur.fetchone()[0]
		if arexists:
			print("Success!")
			pass
		else :
			print("Error : wrong license ID...")
			return

		print("Choose what to edit : ")
		print("1. Name")
		print("2. Color")
		print("3. Country")
		print("0. Exit")
		choice = input("Input : ").strip()
		match choice :
			case "1" :
				newLName = input("Input New License Name : ")
				#
				# I M P O R T A N T 
				# ADD CHECKS FOR NAME INPUTS
				cur.execute("UPDATE LICENSE SET name = ? WHERE licenseid = ?" ,(newLName,licenselid)) #update DB
				con.commit()

				data = cur.execute("SELECT * FROM LICENSE WHERE licenseid = ?",(licenselid,)).fetchall()
				print("New license name : ")
				print(tabulate(data, tablefmt="grid"))
				
				pass

			case "2" :
				newLColor = input("Input New License Color (choose form the official list) : ")

				cur.execute("UPDATE LICENSE SET color = ? WHERE licenseid = ?" , (newLColor,licenselid))
				con.commit()

				data = cur.execute("SELECT * FROM LICENSE WHERE licenseid = ?",(licenselid,)).fetchall()
				print("New license color : ")
				print(tabulate(data, tablefmt="grid"))
				pass
			
			case "3" : 
				newLCountry = input("Input New Licensing Country (Make sure to use real country names) : ")

				cur.execute("UPDATE LICENSE SET licensing_country = ? WHERE licenseid = ?", (newLCountry,licenselid))
				con.commit()

				data = cur.execute("SELECT * FROM LICENSE WHERE licenseid = ?",(licenselid,)).fetchall()
				print("Updated licensing country : ")
				print(tabulate(data, tablefmt="grid"))
				pass

			case "0" | "exit" :
				pass

			case _:
				print("Error : 1 : Wrong Input : Function only takes number or \"exit\"")
				pass

		con.close()
		license_menu()

	else :
		print("Error : ERR : Database does not exist")
		return