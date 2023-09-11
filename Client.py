import socket
import sys

def main():
    # Configurações do cliente
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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conecta ao servidor
    client_socket.connect((HOST, PORT))
    print('Conexão estabelecida com o servidor.')

    while True:
        # Lê uma mensagem do usuário
        message = input('Digite uma mensagem para o servidor: ')
        if not message:
            break
        # Envia a mensagem para o servidor
        client_socket.sendall(message.encode())
        if message.lower() == 'tchau':
            break

        # Recebe a resposta do servidor
        data = client_socket.recv(BUFFER_SIZE)
        server_response = data.decode()
        print(f'Resposta do servidor: {server_response}')
        if server_response.lower() == 'tchau':
            break

    print('Conexão encerrada.')
    client_socket.close()

if __name__ == '__main__':
    main()
