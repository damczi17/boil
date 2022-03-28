
from event import event
import os

def graphDraw(events):
    f = open("graph.gv", "w")
    f.write('digraph G { \nrankdir="LR";\n')
    id = 0
    t0j = 0
    t1j = 0
    Lj = 0
    for i in range(len(events)):
        id = str(events[i].ID)
        t0j = str(events[i].t0j)
        t1j = str(events[i].t1j)
        Lj = str(events[i].Lj)
        f.write('struct' + id + '[shape=record,label="'+ id +'|{' + t0j + '|' + t1j + '}| ' + Lj +'"')
        if(events[i].cpm == 1):
            f.write(', color=crimson];')
        else:
            f.write('];\n')
        for j in range(len(events[i].successors)):
            f.write('struct' + id + ' -> struct' + str(events[i].successors[j]) + '[')
            if(events[i].outgoingActions[j].cpm == 1):
                f.write('color=green, ')
            f.write('label="' + str(events[i].outgoingActions[j].name) + ' ' + str(events[i].outgoingActions[j].duration) + '"];\n')

# node [shape=plaintext]
#   subgraph cluster_01 { 
#     label = "Legenda";
#     Zdarzenie
#     struct [shape=record,label="ID|{t0j|t1j}| Lj"]
#     key [label=<<table border="0" cellpadding="1" cellspacing="0" cellborder="0">
#       <tr><td align="right" port="i1">Aktywność</td></tr>
#       <tr><td align="right" port="i2">Ścieżka CPM</td></tr>
#       </table>>]
#     key2 [label=<<table border="0" cellpadding="1" cellspacing="0" cellborder="0">
#       <tr><td port="i1">&nbsp;</td></tr>
#       <tr><td port="i2">&nbsp;</td></tr>
#       </table>>]
#     key:i1:e -> key2:i1:w 
#     key:i2:e -> key2:i2:w [color=green]
#     f.write('\nstruct [shape=record,label="ID|{t0j|t1j}|Lj"];\n}')
    f.close()
    os.system("dot -Tpng graph.gv -o graph.png")
    os.system("graph.png")

def eventsCreator(activities):
    events = []
    numberOfEvents = activities[len(activities)-1].incoming #zalozenie ze w podawanych przez uzytkownika aktywnosciach ostatnia aktywnosc wchodzi do ostatniego zdarzenia
    for i in range(int(numberOfEvents)):#utworzenie listy zdarzen na podstawie przeslanych przez uzytkownika aktywnosci
        events.append(event(i+1))
    
    for i in activities:
        outgoingEventID = int(i.outgoing) - 1  #pobranie ID zdarzenia z ktorego wchodzi akrywnosc
        incomingEventID  = int(i.incoming) - 1  #pobranie ID zdarzenia do ktorego wchodzi akrywnosc
        events[incomingEventID].predecessors.append(outgoingEventID+1)    #stworzenie list poprzednikow i nastepnikow dla zdarzen
        events[outgoingEventID].successors.append(incomingEventID+1)

        events[outgoingEventID].outgoingActions.append(i)  #uzupelnienie list czasow trwania dla wchodzacych i wychodzacych aktywnosci dla zdarzen
        events[incomingEventID].incomingActions.append(i)
    return events

def t0jCounting(events):
    events[0].t0j = 0
    events[0].t1j = 0
    events[0].Lj = 0

    for i in range(1,len(events)):
        if(len(events[i].predecessors) == 1):
            id = int(events[i].predecessors[0]-1)   #pobranie ID porzednika i obliczenie przy jego pomocy czasu t0j
            events[i].t0j = int(events[id].t0j) + int(events[i].incomingActions[0].duration)
        else:
            tmp = []
            for j in range(len(events[i].predecessors)):    #sytuacja gdy zdarzenie posiada więcej niz jednego poprzednika
                id2 = int(events[i].predecessors[j]-1)
                tmp.append(int(events[id2].t0j) + int(events[i].incomingActions[j].duration)) #tworzymy liste mozliwych czasow t0j
            events[i].t0j = max(tmp) #wybieramy maksymalny czas t0j z listy
        


def t1jCounting(events):
    events[len(events)-1].t1j = int(events[len(events)-1].t0j) #przypisanie do ostatniego zdarzenia czasu t1j
    for i in range(len(events)-2,0,-1):
        if(len(events[i].successors) == 1):
            tmp = events[events[i].successors[0]-1].t1j - int(events[i].outgoingActions[0].duration)
            events[i].t1j = tmp
        else:
            tmp = []
            for j in range(len(events[i].successors)):
                tmp.append(events[events[i].successors[j]-1].t0j - int(events[i].outgoingActions[j].duration))
            events[i].t1j = min(tmp)


def LjCounting(events):
    for i in events:
        i.Lj = i.t1j - i.t0j


def cpmAlgorithm(events):
    for i in range(len(events)):
        for j in range(len(events[i].successors)):
            if(events[i].Lj == 0 and events[i].t1j + events[i].outgoingActions[j].duration == events[events[i].successors[j]-1].t1j):
                events[i].cpm = 1
                events[i].outgoingActions[j].cpm = 1

        if(i == len(events)-1):
            events[i].cpm = 1

def cpmCalculate(activities):
    events = eventsCreator(activities)
    t0jCounting(events)
    t1jCounting(events)
    LjCounting(events)
    print("\n")

    for i in events:
        print(f'ID: {i.ID} t0j: {i.t0j}')

    print("\n")
    
    for i in events:
        print(f'ID: {i.ID} t1j: {i.t1j}')

    print("\n")
    
    for i in events:
        print(f'ID: {i.ID} t1j: {i.Lj}')

    cpmAlgorithm(events)
    print("\n")
    for i in events:
        print(f'ID: {i.ID} cpm: {i.cpm}')
    
    graphDraw(events)