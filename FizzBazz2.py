print("Introduceti un numar: ")
numar = input()
numar = int(numar)

if numar % 3 != 0 and numar % 5 != 0:
    print(numar)

elif numar % 3 == 0 and numar % 5 == 0:
    print("FizzBuzz")    

elif numar % 3 == 0:
    print("Fizz")
elif numar % 5 == 0:
    print("Buzz")     
