import random

class Player:
    def __init__(self) -> None:
        self.player = None
    def set_player(self, player):
        self.player = player
    def start_music(self, music):
        pass

class Jukebox:
    def __init__(self):
        self.records = []
        self.charge = 100
        self.player = None
    def set_player(self, player):
        self.player.set_player(player)
    def chaeging(self, pay):
        if pay >= self.charge:
            return pay - self.charge
        else:
            return -1
    def set_record(self, record):
        self.records.append(record)
    def start_random_music(self):
        if not self.records:
            raise Exception("no record")
        self.player.start_music(self.records[random.uniform(0, len(self.records))])
