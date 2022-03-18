class activity:
    originEvent = 0
    predecessors = []
    def __init__(self, name, duration, predecessor):
        self.name = name
        self.duration = duration
        if predecessor == '':#jesli czynnosc nie ma poprzednika, to wychodzi zawsze z zdarzenia o ID = 1
            self.originEvent = 1
        self.predecessors = predecessor.split(",")
        print(f'{self.name} => {self.originEvent}')