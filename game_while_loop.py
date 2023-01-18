print ('Type -help-')

user_input = ''
while True:
    user_input = input ('> ').lower()     
    
    if user_input == 'start':
          print ('Car started... Ready to go!')
    elif user_input == 'stop':
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



