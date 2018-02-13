# Echo server program
import socket
import _thread

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 9000               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

def handler(conn, addr):
    print ("Connected by ", addr)
    while 1:
        data = conn.recv(1024)
        if not data: break
        conn.sendall(data)
        print(data)
    conn.close()

while True:
    conn, addr = s.accept()
    _thread.start_new_thread( handler, (conn, addr) )

