import time
import urllib.request
from urllib.request import urlopen
import xml.dom.minidom as XML


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


def logout_request(username):
    url = 'http://172.16.68.6:8090/logout.xml'
    post_data = bytearray('mode=193' + '&username=' + username, 'UTF-8')
    response = urllib.request.urlopen(url, post_data)


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


def main():
    cmd = sys.argv[1]
    if cmd == 'login':
        un = sys.argv[2]
        passwd = sys.argv[3]
        login_request(un, passwd)
    elif cmd == 'logout':
        un = sys.argv[2]
        logout_request(un)
    elif cmd == 'status':
        un = sys.argv[2]
        print(check_live(un))

if __name__ == '__main__':
    main()