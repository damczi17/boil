from event import event

def evetsCreating(activities):
    counter = 1 #licznik do ID zdarzen
    events = []

    events.append(event(1)) #tworze 1 zdarzenie
    for i in activities:
        if(i == activities[0]):#Sytuacja tylko dla pierwszej aktywności inicjującej
            events[0].outgoingActions.append(i.name) #ustawiam czynnosc jako wychodzaca z 1 zdarzenia
            events.append(event(counter+1)) #tworze kolejne zdarzenie 
            events[counter].incomingActions.append(i.name) #ustawiam ze ta czynnosc wchodzi w utworzone zdarzenie
            counter += 1 #zwiekszam licznik
        elif(i.originEvent == 1 and i != activities[0]):
            events[0].outgoingActions.append(i.name)

        elif(i.originEvent == 0 and len(i.predecessors) == 1):
            for j in events:
                if(i.predecessors[0] in j.incomingActions):
                    events.append(event(counter+1))
                    j.outgoingActions.append(i.name)
                    events[counter].incomingActions.append(i.name)
                    counter += 1
        # elif(len(i.predecessor) > 1):
        #     x = i.predecessor.split(",")
        #     events.append(event(counter+1))
        #     for k in x:
        #         events[counter-1].outgoingActions += k
        #         events[counter].incomingActions += k
            
        


    return events

# Glowny problem powoduje tworzenie zdarzenia przy czynnosci c. Toworzymy nowe zdarzenie i z automatu przesuwają nam się ID zdarzen