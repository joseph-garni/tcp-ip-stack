# Create a basic TCP/IP socket for a client

# This is essentially a simple TCP/IP echo client, where the server listens for the client on a port,
# and returns the message recieved by the client back. 
# This is a VERY basic TCP/IP server, not full functionality implemented. In my own time I think I will try and expand the different 
# levels of the network stack, implementing Classes/Functions for each part of the TCP/IP stack. 

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket address to the server address (specific port the server is on so they're connected)

server_address = ('localhost', 1812) 
print('Starting up on "%s" port "%s"' % server_address)
client_socket.connect(server_address)

try:
    # send data to the server
    message = 'This is the message. Please repeat. '
    print('sending "%s"' % message)
    client_socket.sendall(bytes(message, 'utf-8')) # send data to server (where the message is encoded in bytes type, under UTF-8)

    # look for response back from Server
    amount_received = 0
    amount_expected = len(message) # defining the amout of data expected to be received by the server should be the 
                                   # length of the bytes message sent
                                   # to improve this, we should define the data / message the client can send as a funtion of the TCP packets (these are IP packets actually) (connected to HTTP)

    while amount_received < amount_expected: # we want the server to keep listening for our message, so it captures all our message (no data loss across the client and server)
        data = client_socket.recv(2000) # set the size of the maximim amount of data to be recieved 
        amount_received += len(data) 
        print('received "%s"' % data)

finally:
    print('closing client')
    client_socket.close()

