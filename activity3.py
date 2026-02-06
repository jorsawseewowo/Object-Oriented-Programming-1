class parrot:
    species="birds"
    def __init__(self, name, age):
        self.name = name
        self.age = age
birb=parrot("Eddy", 5)
birg=parrot("Edd", 4)
print("My name is", birb.name, "and I am", birb.age, "years old. I am related to", birb.species)
print("My name is", birg.name, "and I am", birg.age, "years old. I am related to", birg.species)