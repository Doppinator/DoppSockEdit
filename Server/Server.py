##### This version further modularises its member functions by importing them from separate files #####

import socket
import threading
import os

#Import GetFile module
import GetFile

# Begin program
def Main():
    # Listen on all interfaces
    host = '0.0.0.0'
    # Set server port
    port = 5000

    #Create object from socket.socket() method called serverSocket 
    serverSocket = socket.socket()
    #Set the socket config options for socket object
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the server socket  to the host address and port above
    serverSocket.bind((host, port))

    # Set the socket to listen for incoming connections
    serverSocket.listen(5)

    #If the socket is listening, inform the user
    print("Server has started, waiting for connection...")

    try:
        while True:
            # Accept new connections using socket.accept() method from serverSocket object, 
            # and assign client socket details and IP address to new variables
            clientSocket, addr = serverSocket.accept()
            print(f"Client connected, IP address: {addr}")
            
            # Create a new thread that uses the getFile method to grab the file
            # Provide the client's socket information
            new_thread = threading.Thread(target=GetFile.getFile, args=(f"Thread-{addr}", clientSocket))
            new_thread.start()
            print("New thread started.")
            print(f"Server working directory: {os.getcwd()}")
        
    #Error handling: print exception to server console 
    except Exception as exception:
        print(f"An error occurred: {exception}")
    
    # Ensure the server socket is closed before exiting    
    finally:
        print("Closing the socket...")
        serverSocket.close()

if __name__ == '__main__':
    Main()
