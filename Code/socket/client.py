import socket



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



host = socket.gethostname()

print(host)

port = 9999

client_socket.connect((host, port))



m = client_socket.recv(1024)

print(m.decode('ascii'))



client_socket.close()