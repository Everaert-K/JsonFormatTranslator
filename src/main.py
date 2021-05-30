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
    try:
        opts, args = getopt.getopt(argv,"hs:f:",["help","string=","file="])
    except getopt.GetoptError:
        print("Apologies, an error occured, try again as follows:")
        print('\tmain.py -s jsonstring')
        print("\tor")
        print('\tmain.py -f filename')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h' or opt == '--help':
            print("Usage:")
            print('\tmain.py -s jsonstring')
            print("\tor")
            print('\tmain.py -f filename')
            sys.exit()


if __name__ == "__main__":
   main(sys.argv[1:])















