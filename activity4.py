class parrot:
    species="birds"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return"{} sings {}".format(self.name, song)
    def dance(self):
        return "{} is now dancing".format(self.name)
spy = parrot("Spy", 35)
scout = parrot("Scout", 21)
print(spy.sing("Monster"))
print(spy.dance())
print(scout.sing("Happy"))
print(scout.dance())