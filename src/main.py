from AbsentError import AbsentError
from Format import OldFormat
from Format import NewFormat
from translate import TranslatorOldToNew
from db import database

import psycopg2
import json
import sys
import getopt

def print_help():
    print("To submit a json-string use:")
    print('\tmain.py -s jsonstring')
    print("To retrieve all json formats stored in the database:")
    print("\tmain.py -a")
    print("To retrieve a json-object with a specific ID:")
    print("\tmain.py -r id")

def main(argv):
    # -s --string  => json string that you want to convert
    # -h --help => give info on how to use
    # -a --all => return all json formats stored in the database
    # -r --retrieve => return a json format with specific idea
    if(len(argv)<1):
        print_help()
        sys.exit()

    try:
        opts, args = getopt.getopt(argv,"has:r:",["help","all","string=","retrieve="])
    except getopt.GetoptError:
        print("Apologies, an error occured, try again as follows:")
        print_help()
        sys.exit(2)

    try:
        db = database()
    except psycopg2.OperationalError:
        print("The connection to the database could not be established")
        print("Please navigate to the config folder and execute the following command in order to start the database:")
        print("docker-compose up")
        sys.exit()

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print("Usage:")
            print_help()
            sys.exit()
        if opt == '-s' or opt == '--string':
            # convert the string to new json format and store in the database
            try:
                old = OldFormat(arg)
                new = TranslatorOldToNew.translate(old) 
                db.insert(new)
            except json.decoder.JSONDecodeError:
                print("The JSON-format appears to be incorrect, try again...")
                sys.exit()
            except AbsentError:
                print("The provided JSON-object appears to be missing some required fields, check your input...")
                sys.exit()  
        if opt == '-a' or opt == '--all':
            rows = db.retrieve_all()
            for row in rows:
                print(row)
        if opt == '-r' or opt == '--retrieve':
            row = db.retrieve_object_with_id(arg)
            print(row)


if __name__ == "__main__":
   main(sys.argv[1:])














