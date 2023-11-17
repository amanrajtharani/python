class User:
    def __init__(self, f_name, l_name, age, caste, log_attempts):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.caste = caste
        self.log_attempts = log_attempts
    def desc(self):
        print("first name ", self.f_name)
        print("last name ", self.l_name)
        print("age ", self.age)
        print("caste ", self.caste)

    def greet(self):
        print("hello ", self.f_name, " ", self.l_name)

    def increment_log_attempts(self):
        self.log_attempts += 1

    def reset_log_attempts(self):
        self.log_attempts = 0

    class Admin:
        def __init__(self):
            self.pr = []
            self.pr.append("can add book")
            self.pr.append("can delete book")
            self.pr.append("can ban book")

        def show_pr(self):
            for i in range(0, len(self.pr)):
                print(self.pr[i])

a = User.Admin()
a.show_pr()
