First_name = input('Enter your first name: \n' )
Last_name = input('Enter your last name: \n')
message = f'Hi {First_name.title()} {Last_name.title()} I have another question for you:' 
print (message)
weight_in_pounds = input ('Tell me your exact weight in pounds \n')

weight_in_kg = 0.4536 * float(weight_in_pounds)
print ("I've calculate your weight in kg -> " , weight_in_kg , 'kg')
nickname = f'{First_name[0]}{Last_name[0:1]}'
nickname_1 = f'{Last_name[2]}'
print ('Here is you alias on this site: ', nickname.upper() + nickname_1.lower()) 
print ('Have a nice day!')



