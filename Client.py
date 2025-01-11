import socket
from pathlib import Path
#Not needed anymore, using pathlib
#import os

#import Modules
import ListFiles
import DownloadFile
import CreateFile

def Main():
    #Set the IP address of the server 
    host = '127.0.0.1'
    #Set the server port
    port = 5000
    #Set the path to the server directory
    serverPath = Path('Server/')
    
    try:
        #Try connecting to the server, start by creating a socket on the client using socket.socket() method
        with socket.socket() as clientSocket:
            # Connect client socket to server IP and Port
            clientSocket.connect((host, port))
            
            while True:
                # Create list filesOnServer with available files using listFiles method,
                # give listFiles the Server Path as location to search
                filesOnServer = ListFiles.listFiles(serverPath)
                
                # User input for file selection or creation or exit, strip() whitespace
                choice = input(
                    "\nEnter the number of a file to download, a new filename to create, or 'Q' to quit: ").strip()
                #If the user enters Q or q, exit
                if choice.lower() == 'q':
                    print("Exiting the program. My work here is done.")
                    break

                #If the user enters a number to choose a file
                elif choice.isdigit():
                    #Minus 1 from number entered since first position in list is 0, not 1
                    fileListIndex = int(choice) - 1
                    
                    #If fileListIndex is NOT negative 
                    # *and* less than the number of files in the list (rudimentary additional validation)
                    if 0 <= fileListIndex < len(filesOnServer):
                        
                        #Give new var selectedFile the numbered index of the chosen file in the list/array filesOnServer
                        selectedFile = filesOnServer[fileListIndex]
                        
                        #Call downloadFile method from its module and set clientSocket as socket arg, selected file name as fileName arg 
                        # (sends as GET + File Name to server) and save location arg (saves to current dir)
                        DownloadFile.downloadFile(clientSocket, selectedFile.name, selectedFile.name)
                        
                    else:
                        print("Invalid selection. Please choose a valid file number.")
                        
                #If no digit entered, call createFile give the entered choice to the fileName arg
                #Write the entered string (choice) to working directory
                else:
                    CreateFile.createFile(choice)
     
    except Exception as exception:
        print(f"Oh snap. Something went wrong: {exception}")

if __name__ == '__main__':
    Main()
