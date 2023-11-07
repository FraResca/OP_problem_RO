import networkx as nx
import json

from matplotlib import pyplot as plt

from istance_parser import *
from local_search import *
from tabu_search import *
from grasp import *

TMax,G = from_op_format("Tsiligirides_1/tsiligirides_problem_1_budget_50.txt")

path = ricerca_greedy_nn(G,0,TMax)

def plot_graph(G,cammino):

  edges = []
  for i in range(len(cammino)-1):
    edges.append((cammino[i],cammino[i+1]))
  pos = nx.spring_layout(G, scale=2)
  fig, ax = plt.subplots()
  #label1 = nx.get_node_attributes(G, 'nome')
  #label2 = nx.get_node_attributes(G, 'gradimento')
  #label3 = nx.get_node_attributes(G, 'durata')
  edge_labels = nx.get_edge_attributes(G, 'tempo')
  nx.draw(G, pos=pos, ax=ax)
  nx.draw_networkx_labels(G, pos)
  nx.draw_networkx_nodes(G, pos, nodelist=cammino, node_color="tab:red", ax=ax)
  nx.draw_networkx_edges(G, pos, edgelist=edges, width=3, edge_color="tab:red", ax=ax)
  #nx.draw_networkx_labels(G, pos, label1)
  #nx.draw_networkx_labels(G, pos, label2)
  #nx.draw_networkx_labels(G, pos, label3)
  #nx.draw_networkx_edge_labels(G, pos, edge_labels)
  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
  plt.axis("on")
  plt.show()

def print_json(filepath):
  f = open(filepath)
  data = json.load(f)
  for albergo in data:
    print("Albergo: ", albergo)
    for tecnica in data[albergo]:
      print("\tTecnica: ", tecnica)
      for metrica in data[albergo][tecnica]:
        print("\t\t", metrica, data[albergo][tecnica][metrica])

print_json("tsiligirides_problem_1_budget_50.json")

plot_graph(G,path)



