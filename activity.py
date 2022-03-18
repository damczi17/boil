class activity:
    def __init__(self, name, duration, predecessor):
        self.originEvent = 0
        self.predecessors = []
        self.name = name
        self.duration = duration
        if predecessor == '':#jesli czynnosc nie ma poprzednika, to wychodzi zawsze z zdarzenia o ID = 1
            self.originEvent = 1
        self.predecessors = predecessor.split(",")
        print(f'{self.name} => {self.originEvent}')