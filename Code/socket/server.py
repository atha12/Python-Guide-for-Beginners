import socket



server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



host = socket.gethostname()

print(host)

port = 9999

server_socket.bind((host, port))

server_socket.listen(1)



msg = 'Hello Client'

c, addr = server_socket.accept()



c.send(msg.encode('ascii'))



c.close()
