#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import re
import requests
import socket
import http.cookiejar
import subprocess
import time
from modules.ScanningEnumeration.getports import *
from core.Core.colors import *

info = "This module tries to determine the target's OS using censys."
searchinfo = "OS Identifier"
properties = {}

def getos0x00(web):

    global flag
    flag = 0x00
    ip_addr = socket.gethostbyname(web)
    print(C+' [*] Querying Reverse DNS...')
    time.sleep(0.7)
    print(G+' [+] Website IP : ' +O+ str(ip_addr))
    time.sleep(0.5)
    print(GR+' [*] Trying to identify operating system...')
    time.sleep(0.5)
    print(O+' [!] Configuring requests...')
    result = requests.get('https://www.censys.io/ipv4/%s/raw' % ip_addr).text
    print(GR+' [*] Getting raw data...')
    time.sleep(0.8)
    print(R+' [*] Analysing responses...')
    try:
        match = re.search(r'&#34;os_description&#34;: &#34;[^<]*&#34;', result)
        if match:
            flag = 0x01
            print(B+' [+] Operating System Identified : ' + C+ match.group().split('n&#34;: &#34;')[1][:-5])
        else:
            print(R+' [-] No exact Operating System matches for '+O+web+'...')
            flag = 0x00
        return flag
    except Exception as e:
        print(R+' [-] Unhandled Exception : '+str(e))

def attack(web):
    getos0x00(web)