## For loops just loop through and do a certain task x amount of times

# initiate for loop
# cycles from 0 to 2
for i in range(3):
    print(i)

fruits = ['banana', 'apple', 'grapes', 'kiwi']
# now all though for loops should ignore the last number, they don't in lists/arrays
for items in fruits:
    print(items)

# OR
print("-----")

for item in range(len(fruits)):
    print(fruits[item])

# now let's find and delete from list

for delete in range(len(fruits)):
    if (fruits[delete] == 'apple'):
        del fruits[delete]
        # break so that there is no errors
        break

print(fruits)
