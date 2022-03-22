import os

def graphDraw(activities):
    f = open("graph.gv", "w")
    f.write("digraph G { \n")
    for i in activities:
        f.write(f'  {i.outgoing} -> {i.incoming} [label="{i.name} {i.duration}"]\n')

    f.write("\n}")
    f.close()
    os.system("dot -Tpng graph.gv -o graph.png")
    os.system("graph.png")