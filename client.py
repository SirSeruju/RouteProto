import socket
import sys
 
tcp_socket = socket.create_connection(('0.0.0.0', 10101))

port = (5555).to_bytes(2, 'big')
current_hop = bytes([0])
ips = bytes([127, 0, 0, 1]) +\
      bytes([127, 0, 0, 1]) +\
      bytes([127, 0, 0, 1])

data = port +\
       current_hop +\
       bytes([len(ips) // 4]) +\
       ips +\
       b"Hello"
try:
    tcp_socket.sendall(data)
finally:
    print("Closing socket")
    tcp_socket.close()
