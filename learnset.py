class Learnset:
    def __init__(self):
        self.level_up = list()
        self.tmhm = list()
        self.breeding = list()
        self.tutoring = list()

    def _level_up_str(self):
        string = ""
        for entry in self.level_up:
            string += f"{entry}, "
        return f"[{string[:-2]}]"

    def __str__(self):
        return f"Learnset(ByLevelUp={self._level_up_str()})"


class LevelUpEntry:
    def __init__(self, level_list, move):
        self.level_list = level_list
        self.move = move

    def __str__(self):
        return f"LevelUpEntry(levels={self.level_list}, move={self.move})"

class TmHmEntry:
    def __init__(self, tm_num):
        self.tm_num = tm_num

class BreedingEntry:
    def __init__(self, parent_list, move):
        self.parent_list = parent_list
        self.move = move

class TutoringEntry:
    def __init__(self, game_list, move):
        self.game_list = game_list
        self.move = move