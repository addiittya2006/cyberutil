#!/usr/bin/python
import os
import signal
import sys
import time
import urllib.request
from urllib.request import urlopen
import xml.dom.minidom as XML

cybfile = 'cyberoam.pid'


def daemon():
    s = os.fork()
    if s != 0:
        sys.exit()
    pid = os.getpid()
    pidfile = open(cybfile, 'w')
    pidfile.write(str(pid))
    pidfile.close()


def login_request(username, password):
    url = 'http://172.16.68.6:8090/login.xml'
    post_data = bytearray('mode=191' + '&username=' + username + '&password=' + password, 'UTF-8')
    # try:
    response = urllib.request.urlopen(url, post_data)
    xml_dom = XML.parseString(response.read())
    document = xml_dom.documentElement
    response = document.getElementsByTagName('message')[0].childNodes[0].nodeValue
    if 'successfully' in response:
        return True
    else:
        return False
        # except:
        #     return False


def logout_request(username):
    url = 'http://172.16.68.6:8090/logout.xml'
    post_data = bytearray('mode=193' + '&username=' + username, 'UTF-8')
    response = urllib.request.urlopen(url, post_data)
    print('Logged out.')
    try:
        if os.path.exists(cybfile):
            pidfile = open(cybfile, 'r')
            for line in pidfile:
                os.kill(int(line), signal.SIGKILL)
            pidfile.close()
            if os.path.exists(cybfile):
                os.remove(cybfile)
    except:
        print('Logout Failed')
                # except:
                # if os.path.exists('cyberoam.pid'):
                # os.remove('cyberoam.pid')
                # try:
                #     pf = open('cyberoam.pid', 'r')
                #     pid = int(pf.read().strip())
                #     pf.close()
                # except:
                #     pid = None
                #
                # if not pid:
                #     message = "pidfile %s does not exist. Daemon not running?\n"
                #     sys.stderr.write(message % username.pidfile)
                #     return
                # try:
                #     while 1:
                #         os.kill(pid,)
                #         time.sleep(1.0)
                # except OSError, err:
                #         err = str(err)
                #         if err.find("No such process") > 0:
                #             if os.path.exists(username.pidfile):
                #                 os.remove(username.pidfile)
                #             else:
                #
                #         else:
                #             print(str(err))
                #             sys.exit(1)



def check_live(username):
    url = 'http://172.16.68.6:8090/live?mode=192'
    url = url + '&username=' + username
    response = urlopen(url).read()
    xml_dom = XML.parseString(response)
    document = xml_dom.documentElement
    status = document.getElementsByTagName('ack')[0].childNodes[0].nodeValue
    if status == 'ack':
        return True
    else:
        return False


def init(username, password):
    daemon()
    while True:
        if not check_live(username):
            login_request(username, password)
        time.sleep(5)
    # return p

def main():
    cmd = sys.argv[1]
    if cmd == 'login':
        un = sys.argv[2]
        passwd = sys.argv[3]
        init(un, passwd)
    elif cmd == 'logout':
        un = sys.argv[2]
        logout_request(un)
    elif cmd == 'status':
        un = sys.argv[2]
        print(check_live(un))

if __name__ == '__main__':
    main()