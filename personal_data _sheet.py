First_name = input('Enter your first name: \n' )
Last_name = input('Enter your last name: \n')
message = f'Hi {First_name.title()} {Last_name.title()} I have another question for you:' 
print (message)

weight = input ('Tell me your exact weight  \n')
print ('You enter ' , weight)
print ("(L)bs or (K)g")
metric = input()
if metric == "K" or metric == "k":
    mess =  2.205 * float(weight)
    print ('You are', mess ,'lbs')
elif metric == "L" or metric == "l":
    mess_2 =   0.4536 * float(weight) 
    print ('You are' , mess_2 , 'kg')
else :
    print ("Error, please retype")


nickname = f'{First_name[0]}{Last_name[0:1]}'
nickname_1 = f'{Last_name[2]}'
print ('Here is you alias for this site: ', nickname.upper() + nickname_1.lower()) 
print ('Have a nice day!')



