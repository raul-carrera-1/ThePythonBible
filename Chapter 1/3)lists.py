## List hold a lot of varibles in one place
## They are called ARRAYS by the pros

# create array
# index  0 1 2
array = [1,4,3]
# display the sum of all there values
print(array[0] + array[1] + array[2])

# ddding to one
array.append(2)
print(array)
# or set an already existing position
array[0] = 9
print(array)

#now delete one
del array[0]
print(array)