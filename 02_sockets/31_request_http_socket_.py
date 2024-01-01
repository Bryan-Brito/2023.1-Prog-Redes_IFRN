import socket

#definir as informações para acessar 
host = 'ifrn.edu.br'
port = 80
resource = '/'

#Descritor do socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #conectar ao servidor
    sock.connect((host,port))

    #enviar a solicitação HTTP
    request = f"GET {resource} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    sock.sendall(request.encode())

    #Receber e imprimir a resposta
    response = b''
    while True:
        data= sock.recv(4096)
        if not data:
            break
        response += data

        print(response.decode())

finally:
    #fecha o socket
    sock.close()