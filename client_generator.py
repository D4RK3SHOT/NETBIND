#usr/bin/python
'''
 _       ____  _    _     _  _          _
| |____ |  __|| |_ | |    _ | |____    | |
|  __  ||  __||  _|| |__ | ||  __  | __| |
| |  | || |__ | |  | __ || || |  | || __ |
|_|  |_||____||_|  |____||_||_|  |_||____|
---------------------------------------------
#THE NETBIND network tool
#Author  : D4RK3SH0T
#Github  : https://github.com/D4RK3SHOT
#Twitter : https://twitter.com/D4Rk3Sh0T
#Licence : Open-Source
'''
import os,sys,argparse
def Arg_Parser():
    parser = argparse.ArgumentParser(description="NETBIND CLIENT GENERATOR")
    parser.add_argument('--LHOST',required=True,help="The server address")
    parser.add_argument('--LPORT',required=True,help="The server port")
    parser.add_argument('--FILE',required=True,help="Output file(.py)")
    args = parser.parse_args()
    LHOST = args.LHOST
    LPORT = args.LPORT
    FILE  = args.FILE
    generator(LHOST,LPORT,FILE)
def generator(LHOST,LPORT,FILE):
    _FILE = "Clients/%s" % FILE
    _FILE = open(_FILE,"w")
    _SOURCE = open("src/client.py","r").read()
    _FILE.write(_SOURCE % (LHOST,LPORT))
    _FILE.close()
    print("[~] %s Generated !" % FILE)
Arg_Parser()
