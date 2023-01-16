user_input = input('Press - help -  to start the program \n> ')
while user_input != 'help' and user_input != 'HELP':
    print ('Incorect input, please try again')
    user_input = input('Press - help -  to start the program \n> ')
else:
    print ('start - to start the car \nstop - to stop the car \nquit - to exit')
game_options = input('> ')    
while game_options == 'start':
    print ('Car started... Ready to go!')

while game_options == 'stop':
    print ('Car stopped.')
    
while game_options == 'quit':
    break






