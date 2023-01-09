temperatures = [5, 9, 11, 12, 2, 4, 14]
print ('initial_list->', temperatures)


temperatures.insert(0 ,  temperatures.pop(6)) #yeyyyyy!!
print ('task_no_2 ->', temperatures)

temperatures.pop(3)
print('task_no_3 ->',temperatures) # too easy :D

temperatures.insert(2, 2 and temperatures.pop(4) )
print ('task_no_4 ->', temperatures)

print ('task_no_5 ->', temperatures[5])

temperatures.reverse()
print('task_no_6 ->',temperatures)

temperatures_copy = temperatures.copy ()
temperatures_copy.append(99999999)
print('task_no_7 ->', temperatures_copy)
print(temperatures)

print ('task_no_8 ->', sorted(temperatures))

print ('task__no_9 ->', max(temperatures))

print ('task__no_10 ->', min(temperatures))

if 30 in temperatures:
    print('TRUE')
else:
    print('FALSE')






