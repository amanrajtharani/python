class user:
    def __init__(self, f_name,l_name,age,caste):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.caste = caste
    def desc(self):
        print("first name ",self.f_name)
        print("last name ",self.l_name)
        print("age ",self.age)
        print("caste ",self.caste)
    def greet(self):
        print("hello ",self.f_name," ",self.l_name)
a = user("aman","raj",21,"tharani")
a.desc()