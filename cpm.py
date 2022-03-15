
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

class event:
    t0j = 0
    t1j = 0
    Lj = 0
    incomingActions = '' #akcje wchodzace do zdarzen
    outgoingActions = '' #akcje wychodzace ze zdarzen
    def __init__(self, ID):
        self.ID = ID

def evetsCreating(activities):
    counter = 1 #licznik do ID zdarzen
    events = []
    events.append(event(1)) #tworze 1 zdarzenie
    for i in activities:
        if(i.originEvent == 1):#sprawdzam czy czynnosc nie ma poprzednika, jesli tak to :
            events[0].outgoingActions += i.name #ustawiam czynnosc jako wychodzaca z 1 zdarzenia
            events.append(event(counter+1)) #tworze kolejne zdarzenie 
            events[counter].incomingActions += i.name #ustawiam ze ta czynnosc wchodzi w utworzone zdarzenie
            counter += 1 #zwiekszam licznik

        elif(i.originEvent == 0 and len(i.predecessor) == 1):
            for j in events:
                if(j.incomingActions.find(i.predecessor) == 0):
                    events.append(event(counter+1))
                    events[counter-1].outgoingActions += i.name
                    events[counter].incomingActions += i.name
                    counter += 1

    return events
    
def main():
    activities = []
    activities.append(activity('A',5,''))
    activities.append(activity('B',3,'A'))
    activities.append(activity('C',4,''))
    activities.append(activity('D',6,'A'))
    activities.append(activity('E',4,'D'))
    activities.append(activity('F',3,'B,C,D'))

    events = evetsCreating(activities)

    for i in events:
        print(f'ID {i.ID} wchodzi: {i.incomingActions}  wychodzi: {i.outgoingActions}')


if __name__ == "__main__":
    main()



# def main():
#     actions = []
#     print("Enter actions and finish with ]]:")
#     while True:
#         name = input("Enter action name: ")
#         duration = input("Enter action duration: ")
#         print("Enter predecessors and finish with //")
#         predecessors = []
#         while True:
#             predecessor = input("Enter predecessor : ")
#             if predecessor != "//":
#                 predecessors.append(predecessor)
#             else:
#                 break
#         actions.append(action(name, duration, predecessors))
#         finish = input("If you want to finish, press \"/\", otherwise press enter")
#         if finish == "/":
#             break

# if __name__ == "__main__":
#      main()