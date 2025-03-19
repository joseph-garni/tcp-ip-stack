# Create our basic TCP IP Server

# You want the Server to always be running, even if clients are not connected to the server

import socket

# Create a TCP IP Socket (from the module imported in socket)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket address to specific port for the server

server_address = ('localhost', 1812)
print('Starting up on "%s" port "%s"' % server_address)
socket.bind(server_address)

# (Server) listen for inbound connections

socket.listen(1)

while True:
    # (Server) when we get a connection: 
    print("waiting for connection")
    
    # Use method in the socket module: when we get a connection store it in connection, client_address variables
    connection, client_address = socket.accept()

    try:
        print("connection from", client_address)
        # recieve the data in chunks of bytes
        # if client address exists
        while True:
            data = connection.recv(2000) # this defines the size of the buffer, specific to size of the message you are receiving
            print('recieved "%s"' % data)
            # if we have recieved data over this connection
            if data:
                print('Sending data back to client') # establishing an echo-listener client-server relationship - server listens, client responds.
                msg = str(data) # define the message as a string of data so we can manipulate
                msg = msg + ' plus extra from the server' # adding text to message to indicate server did recieve msg from client (AKN message) # this program could be improved through the use of proper AKN messages (form dependent on network, TCPIP stack architecture)
                msg = bytes(msg, 'utf-8') # converting message back to bytes using encoding protocol (method of encoding strings into bytes)
                connection.sendall(msg) # and then we send it back over the same connection 
            else:
                print('no more data from', client_address) # if no more data recieved from client address, send message to client
                break
    finally:
    # clean up the client-server connection
        connection.close()  





