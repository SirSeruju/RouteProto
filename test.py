import socket
import sys

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', int(sys.argv[1]))
tcp_socket.bind(server_address)
tcp_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
    try:
        data = b""
        BLOCK_SIZE = 65536
        while True:
            rd = connection.recv(BLOCK_SIZE)
            data += rd
            if len(rd) != BLOCK_SIZE:
                break
        print(data)
    finally:
        connection.close()
