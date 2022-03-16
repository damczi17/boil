class event:
    t0j = 0
    t1j = 0
    Lj = 0
    incomingActions = '' #akcje wchodzace do zdarzen
    outgoingActions = '' #akcje wychodzace ze zdarzen
    def __init__(self, ID):
        self.ID = ID