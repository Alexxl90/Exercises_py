# if temperature is greater than 30 itșs a hot day, 
# otherwise if it's less than 10 it's a cold day, otherwise it's neither hot or cold


temprature = int(input())
if temprature > 30:
    print ("It's a hot day")
elif temprature < 10 :
    print ("It's a cold day")
elif  temprature == 24 :
    print ('Perfect temp')
else:
    print ('Normal temp')    

#if name is less than 3 characters long display the error "Name must be at least 3 characters long"
#otherwise if it's more than 50 characters long  display the error "Nama must be  a max of 25 characters" 
# otherwise display "Name loks good"