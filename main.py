from activity import activity
from event import event
import os
#from eventCreator import evetsCreating

def graphDraw(activities):
    f = open("graph.gv", "w")
    f.write("digraph G { \n")
    for i in activities:
        f.write(f'  {i.outgoing} -> {i.incoming} [label="{i.name} {i.duration}"]\n')

    f.write("\n}")
    f.close()
    os.system("dot -Tpng graph.gv -o graph.png")
    os.system("graph.png")

def eventsCreator(activities):
    events = []
    numberOfEvents = activities[len(activities)-1].incoming
    for i in range(int(numberOfEvents)):
        events.append(event(i+1))
    
    for i in activities:
        incoming = int(i.outgoing) - 1
        outgoing = int(i.incoming) - 1
        events[outgoing].predecessors.append(incoming+1)
        events[incoming].outgoingActions.append(int(i.duration))
        events[outgoing].incomingActions.append(int(i.duration))
    return events


def t0jCounting(events):
    events[0].t0j = 0
    events[0].t1j = 0
    events[0].Lj = 0

    for i in range(1,len(events)):
        if(len(events[i].predecessors) == 1):
            id = int(events[i].predecessors[0]-1)
            events[i].t0j = int(events[id].t0j) + int(events[i].incomingActions[0])
        else:
            tmp = []
            for j in range(len(events[i].predecessors)):
                id2 = int(events[i].predecessors[j]-1)
                tmp.append(int(events[id2].t0j) + int(events[i].incomingActions[j]))
            events[i].t0j = max(tmp)
        

def main():
    activities = []
    activities.append(activity('A',3,'1-2'))
    activities.append(activity('B',4,'2-3'))
    activities.append(activity('C',6,'2-4'))
    activities.append(activity('D',7,'3-5'))
    activities.append(activity('E',1,'5-7'))
    activities.append(activity('F',2,'4-7'))
    activities.append(activity('G',3,'4-6'))
    activities.append(activity('H',4,'6-7'))
    activities.append(activity('I',1,'7-8'))
    activities.append(activity('J',2,'8-9'))
 
    #graphDraw(activities)

    events = eventsCreator(activities)
    print(events)

    print("\n")

    t0jCounting(events)
    for i in events:
        print(f'ID: {i.ID} t0j: {i.t0j}')


if __name__ == "__main__":
    main()



