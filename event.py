class event:
    def __init__(self, ID):
        self.ID = ID
        self.t0j = 0
        self.t1j = 0
        self.Lj = 0
        self.predecessors = []
        self.incomingActions = []  # akcje wchodzace do zdarzen
        self.outgoingActions = []  # akcje wychodzace ze zdarzen