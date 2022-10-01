class Password_manager():
    old_passwords = []
    def __init__(self, passw):
        self.old_passwords.append(passw)

    def get_password(self): return self.old_passwords[len(self.old_passwords) - 1]

    def set_password(self, passw): 
        self.old_passwords.append(passw) if passw not in self.old_passwords else print("Error.")

    def is_correct(self, passw): return True if self.old_passwords[len(self.old_passwords) - 1] == passw else False


user = Password_manager("12345")
print(user.get_password())

user.set_password("123123")
print(user.get_password())

user.set_password("12345")
print(user.is_correct("123123"))





        