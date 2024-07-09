## Handling errors is used for when error occur and these are ways to use it to detect error and not ket the program crash

# Try this...
try:
    my_list = [1, 2, 3]
    print(my_list[5])
# If index out of range error happens then do...
except IndexError:
    print("Index out of range!")

# Try this...
try:
    my_dict = {"a": 1, "b": 2}
    print(my_dict["c"])
# If key not found error happens then...
except KeyError:
    print("Key not found in dictionary!")

# Try this...
try:
    number = int("abc")
# If var fail to transform then...
except ValueError:
    print("Invalid value for conversion!")

#### IMPORTANT!!!!!

# Try this...
try:
    with open('non_existent_file.txt', 'r') as file:
        data = file.read()
# If file not found then do...
except FileNotFoundError:
    print("File not found!")

# Try this...
try:
    import non_existent_module
# If import failed then do...
except ImportError:
    print("Module not found!")

# Try this...
try:
    raise RuntimeError("This is a runtime error.")
# If any error then get error name and do...
except RuntimeError as e:
    print(e)

# Try this...
try:
    raise Exception("Fail")
# If any error then do... 
except Exception:
    print("Error")




