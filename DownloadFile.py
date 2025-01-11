from pathlib import Path

#Define new method to download files from server, with options for the client socket, file name and path to save location
def downloadFile(clientSocket, fileName, savePath):
    try:
        # Send GET request and file name to download to server
        clientSocket.sendall(f"GET {fileName}".encode('utf-8'))
        
        # If local file exists
        if Path(savePath).exists():
            #Ask user whether to overwrite it
            overWriteResponse = input(f"The file '{savePath}' already exists locally. Overwrite? (Y/N): ").strip().lower()
            #If response is not Y or y, cancel 
            if overWriteResponse != "y":
                print("Download canceled.")
                return False
                
        # Create local file to write to using open() method with binary write mode. Use object 'file' to write temporary data.
        with open(savePath, 'wb') as file:
            print(f"Local {savePath} created...")
            #Confirm to user that file is downloading
            print(f"Downloading {fileName} from server...")
            while True:
                #While the sockcet is open, write data ti file
                fileContent = clientSocket.recv(1024)
                # Break when reaching end of file
                if not fileContent:
                    print("No more data received from the server.")
                    break
                # Keep writing unless above if condition is met
                file.write(fileContent)
            
        print(f"File {fileName} downloaded successfully to {savePath}.")
        return True
                    
    #Catch an error downloading file, give file name & exception break and end
    except Exception as exception:
        print(f"Error downloading file {fileName}: {exception}")
        return False
