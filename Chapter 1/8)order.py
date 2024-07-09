## In python there is an order of this we must do first

# Imports (external functions to be decleared as being used)
from datetime import datetime

# Classes
class Time():
    def __init__(self):
        self.time = datetime.now()
    
    def callTime(self):
        print(f'time right now is {self.time}')

# Other functions

def HelloWorld():
    print("Hello World")

# Main Function

def main():
    HelloWorld()
    clock = Time()
    clock.callTime()

# OPTIONAL DEPENDING ON PROJECT!!!!

# if to run main
#Only works if file name is __main__.py

#if __name__ == '__main__':
#    main()

main()