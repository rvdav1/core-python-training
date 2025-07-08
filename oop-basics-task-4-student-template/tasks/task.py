class HistoryDict:
    def __init__(self, initial_dict=None):
        self.data = initial_dict or {}
        self.history = []

    def set_value(self, key, value):
        self.data[key] = value
        self.history.append(key)
        if len(self.history) > 5:
            self.history.pop(0)

    def get_value(self, key):
        return self.data.get(key)

    def get_history(self):
        return self.history