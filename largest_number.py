
#write a program to fiind the largest number in a list

numbers = [121 , 432425 , 22, 232]
print (sorted(numbers)[-1])             #solutia pe care eu am gasit-o

number_list = [23, 4, 64, 7]               #solutia pe care o indica Mosh. Nu inteleg de ce as folosi varianta lui. Outputul este acelasi
max = number_list[0]
for max_count in number_list:
    if max_count > max:
        max = max_count
print (max)

