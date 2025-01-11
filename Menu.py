#import File transfer client & File edit modules from their files
import Client
import Edit

#User welcome message
def initMessage():
    print (""""
           Greetings traveller. Four options there are, choose you must:
           
           1. Connect to file server to upload or download files
           2. Edit an existing file, or create a new file in the current folder
           3. Cross the bridge
           4. Exit the application
           \n""")
    
while True:
    #Call the welcome message method
    initMessage()
    
    #Ask for user menu option selection
    menuSelection = int(input("Choose your fate by entering the number corresponding to the desired action.\n"))
    
    try:
        #Invalid selection handling
        if menuSelection > 4 or menuSelection < 1:
            print("Please choose an option between 1 and 4.\n")
            # Restart the loop if the input greater than 4 or smaller than 1
            continue  

        # If menu selection (number) then go to Main() function in selected module, 
        # quote some Monty PYTHON (I didn't notice the pun until just now to be honest)
        # Or exit
        
        if menuSelection == 1:
            Client.Main()
        
        elif menuSelection == 2:
            Edit.Main()
            
        elif menuSelection == 3:
            input("What is the airspeed velocity of an unladen Swallow?\n")
            print("Oh no...\n")
            continue
        
        elif menuSelection == 4:
            input ("Press return to exit")
            break
        
    # Overall error handler bit 
    except Exception as exception:
        print(f"Something went wrong with the selection: {exception}")    