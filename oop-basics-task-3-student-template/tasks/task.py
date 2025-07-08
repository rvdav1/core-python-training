class Counter:
    def __init__(self, start=0, stop=-1):
        self.value = start
        self.stop = stop
        
    def increment(self):
        if self.stop < 0 or self.value < self.stop:
            self.value += 1
        else:
            print("Maximal value is reached.")
            
    def get(self):
        return self.value