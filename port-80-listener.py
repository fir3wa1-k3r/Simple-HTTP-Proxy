import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("",80))
    print("Listening on port 80 :-)")
    while(1):
        sock.listen(5)
        conn, addr = sock.accept()
        print("Connection from "+addr[0]+" port: "+str(addr[1]))
        conn.close()
except:
    sock.close()
