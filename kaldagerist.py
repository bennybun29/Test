class Boy:
    def __init__(self, hair, height, talent):
        self.hair = hair
        self.height = height
        self.talent = talent

    def describe(self):
        print("The Boy you described has a hair type of " + self.hair + ", his height is " + self.height + ', and his talent is ' + self.talent + ".")

class Girl:
    def __init__(self, hair, height, talent):
        self.hair = hair
        self.height = height
        self.talent = talent
    
    def described(self):
        print("The Girl you described has hair type of " + self.hair + ", her height is " + self.height + ', and her talent is ' + self.talent + ".")