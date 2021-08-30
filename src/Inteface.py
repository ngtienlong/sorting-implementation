
class Interface():

    def array_size(self, size):
        size_options = {
            1: 10,
            2: 20,
            3: 30,
            4: 40
        }
        self.array = size_options[size]
        return self.array
