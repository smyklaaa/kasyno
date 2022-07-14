class SignIn():
    """Klasa pozwalajaca na zarejstrowanie urzytkownika"""

    def __init__(self):
        self.users = open("user_list","w")

    def sign_in(self,username,password):
        while username in self.users:
            username = input("Wybrana nazwa urzytkownika jest zajeta, wybierz inna: ")
        self.users.write(f"{username},{password}")

    def check_duplicated(self):
        pass