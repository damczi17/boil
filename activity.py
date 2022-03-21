class activity:
    def __init__(self, name, duration, chronology):
        self.name = name
        self.duration = duration
        self.chronology = chronology.split("-")
        self.outgoing = chronology[0]
        self.incoming = chronology[2]
        print(f'{self.outgoing} => {self.name} => {self.incoming}')