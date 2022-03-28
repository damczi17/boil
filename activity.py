class activity:
    def __init__(self, name, duration, chronology):
        self.name = str(name)
        self.duration = int(duration)
        self.chronology = chronology.split("-")
        self.outgoing = int(chronology[0])
        self.incoming = int(chronology[2])
        self.cpm = 0
        print(f'{self.outgoing} => {self.name} => {self.incoming}')