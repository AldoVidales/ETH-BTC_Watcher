class dog:
    def __init__(self,name,age,race,s):
        self.name = name
        self.age = age
        self.races=race
        self.s = s

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} is rolling over the grass")




firu=dog("firu",12,"chihuaha",'h')
firu.sit()
print(firu.name)

