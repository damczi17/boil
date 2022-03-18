class event:
    def __init__(self, ID):
        self.t0j = 0
        self.t1j = 0
        self.Lj = 0
        self.incomingActions = []  # akcje wchodzace do zdarzen
        self.outgoingActions = []  # akcje wychodzace ze zdarzen
        self.ID = ID