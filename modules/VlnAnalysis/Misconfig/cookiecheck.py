#!/usr/bin/env python3
# coding: utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import urllib.request as urllib
import time
import ssl
from core.Core.colors import *

info = "This module analyzes the security of cookies (HTTPOnly/Secure Flags)"
searchinfo = "Cookie Analysis"
properties = {}

def cookiecheck0x00(searchheaders):

    c = 0
    for header in searchheaders:
        if (("Set-Cookie:".lower() in str(header.lower())) or ('Cookie:'.lower() in str(header.lower()))):
            c = c + 1
    print(G+' [+] %s cookie(s) obtained!' % c)

    for header in searchheaders:
        if (("Set-Cookie:".lower() in str(header.lower())) or ('Cookie:'.lower() in str(header.lower()))):
            try:
                print(G+' [+] Cookie obtained!')
                time.sleep(0.5)
                print(O+' [*] Examining cookie...')
                time.sleep(0.4)
                CookieSplit = header.split(';')
                del CookieSplit[0]
                CookieSplit[-1] = CookieSplit[-1].rstrip()
                CookieString = ''.join(CookieSplit)
                if "HttpOnly".lower() not in CookieString.lower():
                    print(R+" [-] Cookie not marked HttpOnly - "+C+"'" + header.rstrip() + "' ")
                else:
                    print(G+' [+] Cookie marked HTTPOnly - '+C+'"'+header.rstrip()+'"')
                if "Secure".lower() not in CookieString.lower():
                    print(R+" [-] Cookie not marked Secure - "+C+"'" + header.rstrip() + "' ")
                else:
                    print(G+' [+] Cookie marked Secure - '+C+'"'+header.rstrip()+'"')

            except Exception as e:
                print(R+' [-] Some thing happened!')
                print(R+' [!] Error : '+str(e))


def RetrieveHeader(Target):

    ReplyHeaders = ""
    print(O+' [*] Making request to retrieve HHTP headers...')
    if "https" in Target[:5]:
        sslcontext = ssl.create_default_context()
        n = input(O+' [#] Ignore SSL certificate errors? (Y/n) :> ')
        if n == 'y' or n == 'Y':
            print(GR+" [*] Ignoring certificate errors...")
            sslcontext = ssl._create_unverified_context()
        try:
            ReplyHeaders = urllib.urlopen(Target,context=sslcontext).headers.headers
        except ssl.CertificateError:
            print(R+" [-] SSL Certificate authentication error...")
        return ReplyHeaders
    else:
        ReplyHeaders = urllib.urlopen(Target).headers.headers
        return ReplyHeaders

def cookiecheck(web):

    print(R+'\n    ==================================================')
    print(R+'     C O O K I E   C H E C K  (HTTPOnly/Secure Flags)')
    print(R+'    ==================================================\n')

    print(GR+" [!] Initializing Header Analysis...")
    Headers = RetrieveHeader(web)
    cookiecheck0x00(Headers)

def attack(web):
    cookiecheck(web)