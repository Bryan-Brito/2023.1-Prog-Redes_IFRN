import socket
import threading
import random

#configurações
candidates = {
    1: "Paulo",
    2: "Pedro",
    3: "Ana"
}
votes = {candidate: 0 for candidate in candidates}
password = "senha123"

def process_message(client_socket, client_address):
    try:
        message = client_socket.recv(1024).decode
        parts = message.strip().split() #separando as partes da mensagem

        if parts(0) == "candidatos?":
            
            response = "#".join([f"{number}{name}" for number, name in candidates.items()])
            client_socket.send(response.encode())
        elif parts[0] == "votar":
            candidate_number = int(parts[1])
            if candidate_number in candidates:
                with lock:
                    votes[candidate_number]+= 1
                    client_socket.send("ok".encode())
            else:
                client_socket.send("zero".encode())
        elif parts[0] == "resultado":
            if len(parts) == 2 and parts[1] == password:
                response = "#".join([f"{number} {votes}" for number, votes in votes.items{}])
                client_socket.send(response.encode())
            else:
                client_socket.send("zero".encode())
        else:
            client_socket.send("zero".encode())

    except Exception as e:
        print(f"Erro ao processar mensagem do cliente {client_address}: {str(e)}")
        client_socket.send("zero".encode())

    

def handle_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=process_message, args=(client_socket, client_address)).start


#configuração do servidor
server_host = "localhost"
server_port = 8888

#descritos do socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_host, server_port))
server_socket.listen(10)
#inicia a thread para a lidar com as conexões do cliente.
print(f"Servidor de votação iniciado em {server_host}:{server_port}")
threading.Thread(target=handle_connections,args=(server_socket)).start()