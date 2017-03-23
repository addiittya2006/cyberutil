from cybercheck import *
from time import sleep
import os

def load_id():
    id_txt = open(id_file).read()
    lines = id_txt.split('\n')
    ids = map(lambda x: x.split(' '), lines)
    return ids


def cycle(ids):
    global cred
    # try:
    login = False
    new_id_file = open("new_ids_file.txt", 'a')
    for cred in ids:
        if login_request(cred[0], cred[1]):
            print('Logged in with', cred[0], cred[1])
            new_id_file.write(cred[0]+" "+cred[1])
            logout_request(cred[0])
            # login = True
            # while True:
                # sleep(0.5)
                # if not check_live(cred[0]):
                    # login = False
                    # break
    new_id_file.close()
    # except:
        # print("error")
        # try:
            # logout_request(cred[0])
            # print ("Logged out.")
        # except:
            # print ("Wi-fi not Connected or Server Down!")


if __name__ == '__main__':
    id_file = os.path.dirname(__file__)+'/ids.txt'
    # new_id_file = os.path.dirname(__file__)+'/new_ids.txt'
    cycle(load_id())
