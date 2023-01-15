
#if name is less than 3 characters long display the error "Name must be at least 3 characters long"
#otherwise if it's more than 25 characters long  display the error "Name must be  a max of 25 characters" 
# otherwise display "Name loks good"
print ("Enter your name: ")
name = input()
name_characters_count =  len(name)
if name_characters_count <= 3:
    print ("Name must be at least 3 characters long")
elif name_characters_count >= 25:
    print ("Name must be  a max of 25 characters")
else:
    print("Name loks good")
