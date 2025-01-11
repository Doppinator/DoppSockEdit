#Lists files in the given directory with the specified extension.
#Define new method for listing files in a directory with .bat extension
def listFiles(serverPath, extension="*.bat"):

    #Assigns list of file names in the given directory to list/array 'files'
    files = list(serverPath.glob(extension))
    
    #If files has a value (if there are files), iterate over each entry and print to console
    if files:
        print("The following files are available for download:")
        # For each file in the enumerated list 'files' first file numbered 1.
        for listIteration, file in enumerate(files, 1):
            #Print numbered list of files
            print(f"{listIteration}. {file.name}")
        return files
            
    #If no files with .bat extension exist, print and return empty value to files list
    else:
        print(f"Oh snap. No files with extension '{extension}' found in {serverPath}.")
        return False