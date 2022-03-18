from event import event

def evetsCreating(activities):
    counter = 1 #licznik do ID zdarzen
    events = []

    events.append(event(1)) #tworze 1 zdarzenie
    for i in activities:
        if(i.originEvent == 1):#sprawdzam czy czynnosc nie ma poprzednika, jesli tak to :
            events[0].outgoingActions.append(i.name) #ustawiam czynnosc jako wychodzaca z 1 zdarzenia
            events.append(event(counter+1)) #tworze kolejne zdarzenie 
            events[counter].incomingActions.append(i.name) #ustawiam ze ta czynnosc wchodzi w utworzone zdarzenie
            
            counter += 1 #zwiekszam licznik

        # elif(i.originEvent == 0 and len(i.predecessor) == 1):
        #     for j in events:
        #         if(j.incomingActions == i.predecessor):
        #             events.append(event(counter+1))
        #             events[counter-1].outgoingActions += i.name
        #             events[counter].incomingActions += i.name
        #             counter += 1
        # elif(len(i.predecessor) > 1):
        #     x = i.predecessor.split(",")
        #     events.append(event(counter+1))
        #     for k in x:
        #         events[counter-1].outgoingActions += k
        #         events[counter].incomingActions += k
            
            #print(x)
        
    return events