## Variables are places you can store value
## you can transform these values or change them
## you can identify what your program can do because of this

var = 1
# this creates a variable named "var" that stores in a integer (number with no decimals)
var = 3
# this changes the value of "var" and sets it to 3 instead of 1
print(var)
# displays var
var2 = 6
# creates another variable and sets it to 6
var2 += 1
# this increaments the value of 6 by 1
print(var + var2)
# this will show the sum of both numbers

## Now let's see all the possible equations we can create

# basic arithmatics
print("addition")
print(f'{var} + {var2} = {var + var2}')
print("subtraction")
print(f'{var} - {var2} = {var - var2}')
print("multiplication")
print(f'{var} * {var2} = {var * var2}')
print("division")
print(f'{var} / {var2} = {var / var2}')

# function "abs()" grabs a number and makes it the absolute value

print("absolute value of var2")
print(abs(var2))
print("negative absolute value of var2")
print(-abs(var2))

# POWERRR
print("2 to the 4 power")
print(pow(2,4))

# Modulo is what gets us what's left to reach a division
# for example the modulo of 10 and 3 is 1 because 10/3(<-- divisor) is 3.3333 now only use the first number which is 3 and times the with divisor, thats 3 X 3 and that equal to 9
# now, how many number remaining to reach 10. That's just 1 so 10 modulo 3 is 1
print("10 Modulo 3 (10 % 3)")
print(10 % 3)

# String are varaibles that hold words and can't do math

str1 = "Hello"
str2 = "World"
str3 = "2"
str4 = "5"
print(str1 + str2 + str3 + str4)


