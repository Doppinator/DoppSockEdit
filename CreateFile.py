from pathlib import Path

# Define new method to create a file that doesn't exist
def createFile(fileName):
    try:
        # Create PathFile file object from the fileName var, 
        # Just because it's nicer to read than using 'os' library 
        PathFile = Path(fileName)
        
        #Handle file existence check - if it does exist...
        if PathFile.exists():
            #Ask the user if they want to overwrite it
            overWriteResponse = input("The file already exists locally. Overwrite? Y / N")
            #If user enters anything other than Y or y 
            if overWriteResponse.lower() != "y":
                # Return false to method, ending call
                print("Canceled file creation")
                return False
            
        #using open() method create file object in write mode to create the empty file
        with open(fileName, 'w'): #Does this need 'as' statement? Dunno (No it doesn't, works)
            print(f"File {fileName} created successfully.")
            return True
    
    # Error handler critter, prints file name & type of exception to console
    except Exception as exception:
        print(f"Problem creating file {fileName}: {exception}")
        return False
    
