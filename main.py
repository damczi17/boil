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
 
    graphDraw(activities)

    

if __name__ == "__main__":
    main()



