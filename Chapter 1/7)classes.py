## CLASSES they are a set of things that happen everytime you create one
## They are Object which means they have variables and functions in them that every object has but there values may be different

#let's create a class
class Player():
    # Do this every time we create a new Player
    def __init__(self, name):
        # set Player.name to equal what the user says is name
        self.name = name
        
    def Talk(self):
        # grab Player.name and use it in the following sentence
        print("hi my name is " + str(self.name))

me = Player("Raul")
me.Talk()
print("------------------")
bro = Player("Jhon")
bro.Talk()