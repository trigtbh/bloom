import socket
import config

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((config.SERVER_HOST, config.SERVER_PORT))

s.listen(0)

def process(sock):
    print("not implemented")
    sock.close()

while True:
    sock, addr = s.accept()
    process(sock)