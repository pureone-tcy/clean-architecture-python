KEYS = ['sys_name', 'user_name']


class Message:
    def __init__(self, *values):
        self.values = values

    def bind(self):
        messages = {}
        for k, v in zip(KEYS, self.values):
            messages[k] = v
        return messages
