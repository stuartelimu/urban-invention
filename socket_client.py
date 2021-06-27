import socket

def client_program():
    host = socket.gethostname()
    port = 5000 # the same with socket server port

    client_socket = socket.socket()
    client_socket.connect((host,port))

    message = input(' -> ') # get client input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) # send message
        data = client_socket.recv(1024).decode() # get data from the server

        print('received from server: ' + data)

        message = input(' -> ') # take another input

    client_socket.close() # close the connection

if __name__ == '__main__':
    client_program()