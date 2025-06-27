from socket import *
server_socket = socket()
server_socket.bind(('0.0.0.0',6666))
server_socket.listen()
client_socket,client_addr = server_socket.accept()