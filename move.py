class Move:
    def __init__(self, name, type, category, power, accuracy, pp):
        self.name = name
        self.type = type
        self.category = category
        self.power = power
        self.accuracy = accuracy
        self.pp = pp

    def __str__(self):
        return f"Move(name='{self.name}', type='{self.type}', category='{self.category}', power='{self.power}', accuracy='{self.accuracy}', pp='{self.pp}')"