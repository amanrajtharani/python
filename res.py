class user:
    def __init__(self, f_name,l_name,age,caste,log_attempts):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.caste = caste
        self.log_attempts = log_attempts
    def desc(self):
        print("first name ",self.f_name)
        print("last name ",self.l_name)
        print("age ",self.age)
        print("caste ",self.caste)
    def greet(self):
        print("hello ",self.f_name," ",self.l_name)
    def increment_log_attempts(self):
        self.log_attempts += 1
    def reset_log_attempts(self):
        self.log_attempts = 0
a = user("aman","raj",21,"Tharani",5)
a.increment_log_attempts()
a.increment_log_attempts()
a.increment_log_attempts()
print(a.log_attempts)
a.reset_log_attempts()
print(a.log_attempts)