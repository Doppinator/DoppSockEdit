from pathlib import Path
#Not needed anymore
# import os

# New function to receive GET file request from clientSocket and deliver contents of server-side file
def getFile(threadName, socket):
    try:
        # Receive the client's message and store as clientRequest, remove white space with strip()
        clientRequest = socket.recv(1024).decode().strip()

        # If the client request does not have "GET" at the start, give an error
        if not clientRequest.startswith("GET "):
            print(f"Invalid request received: {clientRequest}")
            return
        
        #Split client request into array of strings with split(), select index 1 (the actual file name, not "GET) and store in fileName
        fileName = f"Server/{clientRequest.split(' ')[1]}"
        print(f"{fileName} requested by client")
        
        # If the file exists, pathlib to check
        PathFile = Path(fileName)
        if PathFile.exists():
            fileSize = PathFile.stat().st_size
            #Debugging log to server console
            fileExists = (f"Client selected {fileName} which exists. File size is {fileSize}")
            print(fileExists)
            
            # Open the file in binary read mode as new object 'file'
            with open(fileName, 'rb') as file:
                # Read the 1kb of the file into new var 'content' representing file
                content = file.read(1024)
                print(f"Successfully opened file and read to object {content}")
                # While content still contains data (is not null)
                while content:
                    # Send file bytes over socket to client
                    socket.sendall(content)
                    # Continue to read file contents into content var, loop 1kb chunks until done
                    # while 'content' is true (bytes left to send) continue while loop (socket send)
                    content = file.read(1024)
            print(f"File {fileName} sent successfully.")
            
    # Error handling, print to server console including function name, thread name and exception detail
    except Exception as exception:
        print(f"There was an error transferring the file (getFile) in thread {threadName}: {exception}")
        
    finally:
        # Ensure the client socket is closed
        socket.close()

