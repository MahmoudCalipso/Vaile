#!/usr/bin/env python3
# coding: utf-8
#
#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#
#
#Author : @_tID (0xInfection)
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import re
import sys
sys.path.append('files/signature-db/')
import time
import requests
from core.Core.colors import *
from bs4 import BeautifulSoup
from infodisc_signatures import PHONE_NUMBER_SIGNATURE as signature
links = []
urls = []
found = 0x00

info = "This module tries to find phone numbers disclosed in target's source code."
searchinfo = "Phone Number Harvester"
properties = {}

def phone0x00(url):

    print(R+'\n    ========================')
    print(R+'     PHON3 NuMBER HARVESTER')
    print(R+'    ========================\n')
    time.sleep(0.5)
    links = [url]
    po = url.split('//')[1]
    for w in links:
        print(GR+' [*] Scraping Page: '+O+url)
        req = requests.get(w).text
        check0x00(req)

    soup = BeautifulSoup(req,'lxml')
    for line in soup.find_all('a', href=True):
        newline = line['href']
        try:
            if newline[:4] == "http":
                if po in newline:
                    urls.append(str(newline))
            elif newline[:1] == "/":
                combline = url+newline
                urls.append(str(combline))
        except:
            print(R+' [-] Unhandled Exception Occured!')

    try:
        for uurl in urls:
            print(G+"\n [+] Scraping Page: "+O+uurl)
            req = requests.get(uurl).text
            check0x00(req)

    except:
        print(R+' [-] Outbound Query Exception...')

    if found == 0x00:
        print(R+' [-] No Phone Numbers found disclosed in plaintext in Source Code!\n')

    print(G+' [+] Scraping Done!')

def check0x00(req):

    found = 0x00
    print(O+' [!] Setting parse parameters...')
    comments = re.findall(signature,req)
    print(GR+" [+] Searching for Phone Numbers...")
    if comments:
        print(G+'\n [+] Found Phone Numbers:')
    for comment in comments:
        print(C+'   '+comment)
        time.sleep(0.03)
        found = 0x01

def phone(web):

    print(GR+' [*] Loading module...')
    time.sleep(0.6)
    phone0x00(web)

def attack(web):
    phone(web)