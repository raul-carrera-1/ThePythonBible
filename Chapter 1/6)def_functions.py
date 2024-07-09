## Functions wrote as "def" are matchine which grab info or don't and return or not things back

# for example let's have a function that can identify names

def findName(list_: list, name_: str):
    for i in range(len(list_)):
        if(list_[i] == name_): 
            return True
    return False

Names = ['Pedro', 'Luis', 'David']
Find = 'David'
# call the function and give it there values
# store what's returned in a variable
answer = findName(Names, Find)
print(answer)
Find = 'Paul'
answer = findName(Names, Find)
print(answer)