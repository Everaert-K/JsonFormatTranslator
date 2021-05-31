from Format import OldFormat
from Format import NewFormat
from translate import TranslatorOldToNew
from db import database

import sys
import getopt

def main(argv):
    # -s --string  => json string that you want to convert
    # -f --file => file with a bunch of json elements
    # -h --help => give info on how to use
    # -a --all => return all json formats stored in the database
    # -r --retrieve => return a json format with specific idea
    try:
        opts, args = getopt.getopt(argv,"has:f:r:",["help","all","string=","file=","retrieve="])
    except getopt.GetoptError:
        print("Apologies, an error occured, try again as follows:")
        print('\tmain.py -s jsonstring')
        print("\tor")
        print('\tmain.py -f filename')
        sys.exit(2)

    db = database()

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print("Usage:")
            print('\tmain.py -s jsonstring')
            print("\tor")
            print('\tmain.py -f filename')
            sys.exit()
        if opt == '-s' or opt == '--string':
            # convert the string to new json format and store in the database
            old = OldFormat(arg)
            new = TranslatorOldToNew.translate(old) 
            db.insert(new)  
        if opt == '-a' or opt == '--all':
            rows = db.retrieve_all()
            for row in rows:
                print(row)
        if opt == '-r' or opt == '--retrieve':
            row = db.retrieve_object_with_id(arg)
            print(row)


if __name__ == "__main__":
   main(sys.argv[1:])














