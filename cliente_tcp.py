import socket

target_host = input("informe o site que deseja fazer uma requisição: ")
target_port = 80

#Cria um objeto socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#SOCK_STREAM, É UM TIPO DE SOCKET QUE USA TCP.

client.connect((target_host, target_port))

request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
request_encode = request.encode('utf-8')

client.send(request_encode)


response = client.recv(4096)
print(response.decode('utf-8'))
client.close()