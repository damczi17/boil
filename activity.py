class activity:
    originEvent = 0
    pointedEvent = 0
    def __init__(self, name, duration, predecessor):
        self.name = name
        self.duration = duration
        self.predecessor = predecessor
        if self.predecessor == '':#jesli czynnosc nie ma poprzednika, to wychodzi zawsze z zdarzenia o ID = 1
            self.originEvent = 1

        print(f'{self.name} => {self.originEvent}')