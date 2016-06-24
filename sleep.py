from cyber import *
from time import sleep
import os

id_file = os.path.dirname(__file__)+'/ids.txt'

def load_id():
    id_txt = open(id_file).read()
    lines = id_txt.split('\n')
    ids = map(lambda x: x.split(' '), lines)
    return ids


def cycle(ids):
    global cred
    try:
        login = False
        for cred in ids:
            if login_request(cred[0], cred[1]):
                print('Logged in with', cred[0], cred[1])
                login = True
                while True:
                    sleep(0.5)
                    if not check_live(cred[0]):
                        login = False
                        break
    except:
        try:
            logout_request(cred[0])
            print ("Logged out.")
        except:
            print ("Wi-fi not Connected or Server Down!")


if __name__ == '__main__':
    cycle(load_id())
