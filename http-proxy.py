#Author: fir3wa1k3r
#Name: Simple terminal based HTTP-Proxy
#version: 0.1

import socket
import re
import requests

host = "0.0.0.0"
port = 8080

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind((host,port))

def handle(conn):
    while(1):
        data = conn.recv(1024)

        d_data = data.decode()
        print(d_data)
        regex_target = re.findall("[0-9]+\.[0-9]+\.[0-9+]+\.[0-9]+|[a-z]+\.[a-zA-Z0-9]+\.[a-z]+|http[s]*:\/\/[a-zA-Z0-9.]*",d_data)
        if(regex_target):
            ip = regex_target[0]
            if(re.findall("http[s]*",ip)):
            #print(ip[0])
                pass
            else:
                ip = "http://"+ip
            try:
                r = requests.get(ip)
                print(r)
            except:
                print("Successfully connected to host, Enjoy proxying")
            
        else:
            print("bad IP")
            #Still in testing phase
    conn.close()

print("Proxy Server listening on port 8080")
while(1):
    sock.listen(5)
    conn, addr = sock.accept()
    print("Connection from host: "+addr[0]+" and port: "+str(addr[1]))
    handle(conn)

sock.close()

print("Thanks for connecting!!!")
