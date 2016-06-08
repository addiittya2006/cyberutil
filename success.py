from cyber import *
from time import sleep
import os

id_file = os.path.dirname(__file__)+'ids.txt'

def load_id():
    id_txt = open(id_file).read()
    lines = id_txt.split('\n')
    ids = map(lambda x: x.split(' '), lines)
    return ids


def cycle(ids):
    fo = open("success.txt", "w")
    global cred
    try:
        for cred in ids:
            if login_request(cred[0], cred[1]):
                fo.write(cred[0]+" "+cred[1]+"\n")
                logout_request(cred[0])
    except:
        logout_request(cred[0])


if __name__ == '__main__':
    cycle(load_id())
