import socket
import sys
from protoMeta import ProtoMeta
 
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_port = 10101
server_address = ('0.0.0.0', server_port)
tcp_socket.bind(server_address)
tcp_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
    try:
        protoMeta = ProtoMeta()
        protoMeta.get(connection)
        print(protoMeta)
        
        if protoMeta.isLast():
            next_addr = "0.0.0.0"
            next_conn = socket.create_connection((next_addr, protoMeta.port))
            next_conn.sendall(protoMeta.getData())
            next_conn.close()
        else:
            next_addr = ".".join(list(map(str, list(protoMeta.ips[protoMeta.current_hop + 1]))))
            next_conn = socket.create_connection((next_addr, server_port))
            next_conn.sendall(protoMeta.getNextProtoMeta())
            next_conn.close()
    finally:
        connection.close()
