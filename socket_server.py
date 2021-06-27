import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000 # a port number greater than 1024

    server_socket = socket.socket() # get instance
    server_socket.bind((host, port))

    # configure how many client applications can listen
    server_socket.listen(10)
    conn, address = server_socket.accept() # accept connection
    print('Connection from: ' + str(address))
    while(True):
        # receive data stream
        data = conn.recv(1024).decode()
        if not data:
            break
        print('from connected user: ' + str(data))
        data = input(' -> ')
        conn.send(data.encode()) # send data to the client

    conn.close() # close the connection


if __name__ == '__main__':
    server_program()