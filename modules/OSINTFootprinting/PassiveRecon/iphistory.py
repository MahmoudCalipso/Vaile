#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import requests
from bs4 import *
import time
import lxml
import urllib3
import json
from core.Core.colors import *

info = "Display the history of the target's IP."
searchinfo = "IP History lookup"
properties = {}

def iphistory(web):

    try:
        print(R+'\n    =====================')
        print(R+'     I P   H I S T O R Y')
        print(R+'    =====================\n')
        print(GR+' [*] Parsing Url...')
        web0 = web.split('//')[-1]

        print(web0)

        print(O+' [!] Making the request...')
        html = requests.get('http://viewdns.info/iphistory/?domain=' + web0).text
        print(GR+' [*] Parsing raw-data...')
        time.sleep(0.7)
        soup = BeautifulSoup(html,'lxml')
        print(O+' [!] Setting parameters...')
        table = soup.findAll('table', attrs={'border':'1'})[0]
        print(C+' [!] Finding IP history instances...')
        trs = table.findAll('tr')
        trs.pop(0)

        print(G+'\n [+] Following instances were found...')

        for tr in trs:
            td = tr.findAll('td')
            info = {'ip' : td[0].text, 'owner' : td[2].text.rstrip(), 'last' : td[3].text}
            print(G+' [+] Instance : ' +C+ info['ip'] +GR+ ' => ' + info['owner'] +B+ ' - (' + info['last'] + ')')
            time.sleep(0.02)

    except:
        print(R+' [-] No instances of IP History found...')

def attack(web):
    iphistory(web)