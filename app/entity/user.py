
KEYS = ['sys_name', 'user_name']


class User:
    def __init__(self, *values):
        self.values = values

    def bind(self):
        users = {}
        for k, v in zip(KEYS, self.values):
            users[k] = v
        return users
