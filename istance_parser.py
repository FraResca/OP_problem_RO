import networkx as nx
from math import sqrt

def euclidean_distance(x1,y1,x2,y2):
    return sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

def from_op_format(filename):
    G = nx.Graph()
    f = open(filename)
    op_file = f.read().split("\n")
    first_row = op_file[0].split("\t")
    TMax = float(first_row[0])

    for i in range(1,len(op_file)):
        row = op_file[i].split("\t")
        G.add_node((i-1),x=float(row[0]), y=float(row[1]), score=int(row[2]))
    
    for i in range(len(G.nodes)-1):
        for j in range(i+1, len(G.nodes)):
            G.add_edge(i,j,time=euclidean_distance(G.nodes[i]["x"],G.nodes[i]["y"],G.nodes[j]["x"],G.nodes[j]["y"]))

    return TMax,G

def from_ferrara():
    TMax = 90
    G = nx.Graph()
    with open('interesse.csv') as csv_file:
        lines = csv_file.readlines()
        for i in range(1,len(lines)):
            data = lines[i].split(',')
            raw = data[0]
            raw = raw.replace('"POINT (','')
            raw = raw.replace(')"','')
            raw = raw.split(' ')
            G.add_node((i-1), score=int(float(data[2].replace('\n',''))), x=raw[0], y=raw[1])
            print((i-1), G.nodes[i-1])
    
    with open('distanze.txt') as f:
        lines = f.readlines()
        for line in lines:
            line=line.replace('\n','')
            line=line.split(' ')
            i=int(line[0])
            j=int(line[1])
            time=int(line[2])
            G.add_edge(i,j,time=time)
            G.add_edge(j,i,time=time)

    return TMax,G