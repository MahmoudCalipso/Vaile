#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


try:
    from google import search
except:
    from googlesearch import search
import time
import urllib.request
from random import randint
from time import sleep
from core.Core.colors import *

info = "Find Pastebin posts."
searchinfo = "Find Pastebin posts."
properties = {}

def getposts(web):

    site = str(web)
    def clear_cookie():
        fo = open(".google-cookie", "w")
        fo.close()


    def google_it (dork):
        clear_cookie()
        for title in search(dork, stop=30):
            print(B+' [!] Post Found :> '+C+title)
            time.sleep(0.5)

    try:
        print(O+" [*] Finding Pastebin posts ...\n")
        google_it("site:pastebin.com intext:"+site+"")

    except urllib.error.HTTPError as err:
        if err.code == 503:
            print(R+' [-] Captcha appeared...\n')
            pass

def pastebin(web):

    print(GR+' [*] Loading module...')
    time.sleep(0.6)
    print(R+'\n    =============================')
    print(R+'     P A S T E B I N   P O S T S')
    print(R+'    =============================\n')
    getposts(web)

def attack(web):
    pastebin(web)