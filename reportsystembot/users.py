from config import Config,USER_FILENAME

class Users:
    def __init__(self, users=None):
        self.users = users
        if self.users is None:
            self.users = self.__load_file()

    def __load_file(self):
        with open(Config().variable[USER_FILENAME],'r') as file:
            usuarios = file.readlines()
        return [User(usuario[:-1]) for usuario in usuarios]

    def get_list_users(self):
        return [user.username for user in self.users]

class User:
    def __init__(self,username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value[0] != '@':
            raise ValueError("Usuário não valido")
        self._username = value
