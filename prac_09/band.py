from musician import Musician


class Band:

    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strs = [f"{musician}" for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strs)})"

    def __repr__(self):
        return str(vars(self))

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        play_info = []
        for musician in self.musicians:
            play_info.append(musician.play())
        return '\n'.join(play_info)
