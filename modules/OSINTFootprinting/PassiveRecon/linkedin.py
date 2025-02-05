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

info = "Use LinkedIn as information gathering resource."
searchinfo = "LinkedIn Gathering"
properties = {}

def getposts(web):

    site = str(web)
    def clear_cookie():
        fo = open(".google-cookie", "w")
        fo.close()


    def google_it (dork):
        clear_cookie()
        for title in search(dork, stop=30):
            print(B+' [!] Profile Found :> '+C+title)
            time.sleep(0.5)

    try:
        print(GR+" [*] Finding LinkedIn Employees ...\n")
        google_it("site:linkedin.com employees "+site+"")
        print(O+' [!] Pausing to avoid captcha...')
        time.sleep(10)

        print(GR+' [*] Finding Linkedin company profiles...\n')
        google_it("site:linkedin.com comapany "+site+"")

    except urllib.error.HTTPError as err:
        if err.code == 503:
            print(R+' [-] Captcha appeared...\n')
            pass

def linkedin(web):

    print(GR+' [*] Loading module...')
    time.sleep(0.6)
    print(R+'\n    =====================================')
    print(R+'     L I N K E D I N   G A T H E R I N G')
    print(R+'    =====================================\n')
    getposts(web)

def attack(web):
    linkedin(web)