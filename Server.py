import socket
import sys

def main():# Configurações do servidor
    try:
        HOST = sys.argv[1]  # Endereço IP do servidor
    except:
        print('Endereco IP do servidor nao encontrado')
        return

    try:
        PORT = int(sys.argv[2]) # Porta do servidor
    except:
        print('Porta do servidor nao encontrada')
        return

    BUFFER_SIZE = 1024

    # Cria um socket TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liga o socket ao endereço e à porta
    server_socket.bind((HOST, PORT))

    # Coloca o socket em modo de escuta
    server_socket.listen()

    print('Servidor esperando por conexões...')

    # Aceita uma conexão
    client_socket, client_address = server_socket.accept()
    print(f'Conexão estabelecida com {client_address}')

    while True:
        # Recebe dados do cliente
        data = client_socket.recv(BUFFER_SIZE)
        if not data:
            break
        client_response = data.decode()
        print(f'Mensagem recebida do cliente: {client_response}')
        if client_response.lower() == 'tchau':
            break
        # Envia uma resposta ao cliente
        #ack = 'Mensagem recebida com sucesso!\n'
        response = input('Digite uma mensagem para o cliente: ')
        client_socket.sendall(response.encode())
        if response.lower() == 'tchau':
            break
        #client_socket.sendall(ack.encode())

    print('Conexão encerrada.')
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
