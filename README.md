# NETBIND
NETBIND is a simple networking tool based on server/client data exchange.
server.py : a script that serve a given host on a given port and accept client connection.
client.py : a script that connect to the first host, it allow the server to take control of the command line and get the machine info using the <server command line>.

usage:
   <root> python server.py --LHOST <LHOST> --LPORT <LPORT>
          python client_generator.py --LHOST <LHOST> --LPORT <LPORT> --FILE <Output file>
