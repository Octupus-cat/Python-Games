# Run Me!

class Person:
    """Person represents a person in our system."""

     # This is the initializer, it gets run when we create a new object
    def __init__(self, fname: str, lname: str, age: int):
        """Initializes a new Person object."""
        self.fname = fname
        self.lname = lname
        self.age = age

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        print(f"Hello, my name is {self.fname} {self.lname} and I am {self.age} years old. {message}")
        
        
class Parent(Person):
    """Parent represents a parent in our system."""

    def __init__(self, fname: str, lname: str, age: int, spouse=None):
        """Initializes a new Parent object."""
        super().__init__(fname, lname, age) # Call Person.__init__ to initialize the name and age attributes
        self.children = []
        
        # Set our spose but also set the spouse's spouse to us
        if spouse:
            self.spouse = spouse
            spouse.spouse = self
        
        self.spouse = None

    def add_child(self, child: Person):
        """Adds a child to the parent's list of children."""
        self.children.append(child)
        

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        
        super().say_hello(message)
        if self.spouse:
            print(f"My spouse is {self.spouse.fname}")
            
        print(f"I have {len(self.children)} children.")

        if len(self.children) > 0:
            print("Their names are:")
            for child in self.children:
                print(f"  {child.fname} {child.age}")
                
                
class Child(Person):
    """Child represents a child in our system."""

    def __init__(self, lname: str, fname: str, age: int, parents: list):
        """Initializes a new Child object."""
        super().__init__(lname, fname, age)  # Call Person.__init__ to initialize the name and age attributes
        self.parents = parents

    def say_hello(self, message: str):
        """Prints a greeting to the console."""
        super().say_hello(message)
        print(f"My parents are {', '.join([parent.fname for parent in self.parents])}")
        
        
# Now lets make a family
mom = Parent("Alice", "Lastnamington", 35)
dad = Parent("Bob", "Lastnamington", 40, mom)

charlie = Child("Charlie", "Lastnamington", 10, [mom, dad])
dahlia = Child("Dahlia", "Lastnamington", 8, [mom, dad])

# Connect the children to the parents
mom.add_child(charlie)
mom.add_child(dahlia)
dad.add_child(charlie)
dad.add_child(dahlia)


mom.say_hello("Hello!") # Call the say_hello method of the mom object
print()
dahlia.say_hello("Yo!")