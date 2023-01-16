user_input = input('Press - help -  to start the program \n> ')
while user_input != 'help' and user_input != 'HELP':
    print ('Incorect input, please try again')
    user_input = input('Press - help -  to start the program \n> ')

while True:

    print ('start - to start the car \nstop - to stop the car \nquit - to exit')
    game_options = input('> ')    

    if game_options == 'start':
        print ('Car started... Ready to go!')

    elif game_options == 'stop':
        print ('Car stopped.')
        
    elif game_options == 'quit':
        exit()

    else:
        print('invalid')






