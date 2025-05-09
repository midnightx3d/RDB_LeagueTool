"""
file for checking shit
"""

import usrmgr
import sqlite3
from pathlib import Path

def main():
    create_countries_db()

def create_countries_db():
    countries_file = Path("countries.db")
    if countries_file.exists():
        con = sqlite3.connect("countries.db")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS COUNTRY(name , id)")

        # print("Database already exist")

        con.commit()
        con.close()

    else:
        print("Database not found , Creating...")
        con = sqlite3.connect("countries.db")
        con.close()




#def check_country(country: str) -> None:
#    country = country.strip().lower()
#    if len(country)<4:
#        return None
#    with open("countries.txt", "r") as countries:
#        countries_list = countries.readlines()
#        countries_list = [x.strip("\n").lower() for x in countries_list]
#        print(countries_list)
#    for j in countries_list:
#        if country in j:
#            if country.lower() == j.lower():
#                print("1")
#            else:
#                print(j)
#
#check_country("ukr")