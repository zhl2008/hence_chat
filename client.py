#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re
import time
import Queue
import threading
import itertools
import subprocess
import urllib
import logging
import base64
import sys
import readline
reload(sys)
sys.setdefaultencoding('utf-8')

list_data = []
url = 'http://47.75.2.217/server.php'


def help():
    print "python client.py  [yourname]"


def get_data():
    global sequence
    r = requests.get(url+"?op=read&seq=" + str(sequence + 1))
    res = r.content
    if res == 'null':
	return False
    res = base64.b64decode(res)
    f.write(res + '\n')
    user,msg = res.split('<::>')
    sequence += 1
    print("\033[1;32m" + user + ' said >' +  msg + "\033[0m")

def send_data(data):
    data_enc = base64.b64encode(username + '<::>' + data)
    r = requests.post(url+"?op=send", data={"data": data_enc})
    if r.status_code == 200:
        logging.info("data have been send!")
    else:
        logging.warning("data haven't been send!")

def period_get():
    while True:
        get_data()
        time.sleep(0.5)


if __name__ == '__main__':
    if len(sys.argv) == 2:
	sequence = len(open("client_data.txt","r").readlines()) 
        f = open("client_data.txt", "ab")
        username = sys.argv[1]
        t1 = threading.Thread(target=period_get, args=())
        t1.setDaemon(True)
        t1.start()
        while True:
            data = raw_input('say something: ')
            if data != "":
                send_data(data)
    else:
        help()
