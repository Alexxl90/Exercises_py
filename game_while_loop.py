print ('Type -help-')
started = False

user_input = ''
while True:
    user_input = input ('> ').lower()     
    
    if user_input == 'start':
        if started:
            print ('The car is already started')
        else:
            started = True

            print ('Car started... Ready to go!')
    elif user_input == 'stop':
        if not started:
            print ('The car is already stoped') 
        else:
            started = False ### am nevioe de ceva lamuriri pe aici
            print ('Car stoped ..')
    elif user_input == 'help':
        print ('''Your options are:
start - To start the car
stop - To stop the car
quit - To quit game
help - Main menu
        ''')
    elif user_input == 'quit':
        break
    else:
        print ('''I don't understand, please retype
You options are:
start - To start the car
stop - To stop the car
quit - To quit game''')    



