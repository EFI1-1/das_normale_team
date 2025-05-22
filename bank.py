from user import User

class Bank:
    def __init__(self):
        self.users = {
            "1234":User("1234", 500.0),
            "0000":User("0000", 1000.0)
        }

    def login(self, pin: str) -> User:
        return self.users.get(pin)