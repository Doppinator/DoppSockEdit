import os

def Main():
    try:
        while True:
        # Ask the user for text input, assign input to var
            targetFile = input("Enter the filename of the file you yearn to edit: ")

        # Check if the file exists before proceeding
            if not os.path.exists(targetFile):
                print(f"The file '{targetFile}' does not exist.")
                return  
        
        # Ask the user to specify which position of the file they want to edit
            thisLine = int(input("Enter the line number you desire to modify: "))
            if thisLine > 5 or thisLine < 1:
                print("Only lines 1-4 can be edited.")
                # Restart the loop if the input greater than 5
                continue  
                
            # If the line number is valid, break the loop and continue with the rest of the program
            # Ask the user to enter desired substitution
            newLine = input(f"Enter the text that will write over line number {thisLine}: ")
                
            # Use the open() method to open the file in read-only mode
            # Use new var thisFile to do stuff with the data
            thisFile = open(targetFile, 'r')
            
            # Read the lines in the thisFile var into tempp var fileContent
            fileContent = thisFile.readlines()
            
            # Close the file, calling close() on the thisFile. No longer needed as we have contents in fileContent
            thisFile.close()
            
            # Open the specified file in write mode (w) and use var thisFile to do things with it
            thisFile = open(targetFile, 'w')
            
            # Reduce value of line selection by 1, as the array/list index starts at 0,
            # So the first line is line 0
            fileContent[thisLine - 1] = newLine + "\n"
            
            # Call writelines method to overwrite the bits in the file with the contents we read above
            thisFile.writelines(fileContent)
            
            # Print all lines to console
            for allLines in fileContent:
                print(allLines)
            
            #Close the file again
            thisFile.close()
            
    # Overall error handler bit 
    except Exception as exception:
        print(f"Some error happened. This one: {exception}")    

if __name__ == '__main__':
        Main()