#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import socket
import time
import sys
import getopt
import http.client
from core.Core.colors import *

info = "This module tries to determine if the target is vulnerable to Host Header Injection Attacks."
searchinfo = "Host Header Injection"
properties = {}

def hostheader0x00(web):

    print(R+'\n    ==========================================')
    print(R+'     H O S T  H E A D E R   I N J E C T I O N')
    print(R+'    ==========================================\n')

    port = input(O+' [#] Enter the port to use (eg. 80) :> ')

    if port == 443:
        print(O+" [!] Using HTTPS <port 443>...")
        print(GR+' [*] Setting headers...')
        headers = {
                'User-Agent': 'The Infected Drake [@_tID] on Systems (Vaile)',
                'Content-Type': 'application/x-www-form-urlencoded',
                }

        print(GR+' [*] Requesting response...')
        conn = http.client.HTTPSConnection(host)
        conn.request("GET", "/", "", headers)
        response = conn.getresponse()
        print(' [*] Reading the response...')
        data = response.read()

        print(O+' [!] Response : '+GR, response.status, response.reason)
        print(O+' [!] Data (raw) : \n'+GR)
        print(data + '\n')

    else:
        print(GR+' [*] Setting buffers...')
        buffer1 = "TRACE / HTTP/1.1"
        buffer2 = "Test: <script>alert(tID)</script>"
        buffer3 = "Host: " + web
        buffer4 = "GET / HTTP/1.1"

        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(GR+' [*] Making the connection...')
        result=s.connect_ex((web,int(port)))
        s.settimeout(1.0)

        if result == 0:

            print(C+' [*] Setting injection frame buffers...')
            frame_inject = "codesploit"
            buffer1 = "GET / HTTP/1.1"
            print(B+' [+] Buffer Set : '+C+buffer1)
            buffer2 = "Host: teamcodesploit.gq"
            print(B+' [+] Buffer Set : '+C+buffer2)
            time.sleep(0.5)
            print(GR+' [+] Sending buffers...')
            s.send(buffer1 + "\n")
            s.send(buffer2 + "\n\n")
            print(O+' [!] Receiving response...')
            data1 = s.recv(1024)
            s.close()
            time.sleep(0.7)
            print(GR+' [+] Analysing results...')
            if frame_inject.lower() in data1.lower():
                print(G+' [+] Site is vulnerable to Host Header Injection...')
            else:
                print(R+' [-] Site is immune against Host Header Injection...')

            print("")
            print(GR+' [*] Obtaining header dump data...')
            print("")
            print(O+data1)
            time.sleep(1)

def hhi(web):

    print(GR+' [*] Loading the module...')
    time.sleep(0.5)
    if 'http' in web:
        web = web.replace('http://','')
        web = web.replace('https://','')

    hostheader0x00(web)

def attack(web):
    hhi(web)