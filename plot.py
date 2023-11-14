import networkx as nx
from matplotlib import pyplot as plt

from istance_parser import *
from local_search import *
from tabu_search import *
from grasp import *

TMax,G = from_op_format("Tsiligirides_1\\tsiligirides_problem_1_budget_50.txt")

# Path di test - tsiligirides_problem_1_budget_50.txt - poi lo tolgo
cammino = [0, 15, 16, 24, 25, 26, 27, 28, 0]

path = ricerca_greedy_nn(G,0,TMax)

# Estraggo le coordinate dei nodi e creo il vettore di coordinate
coordinates = []
for node, data in G.nodes(data=True):
    x_value = data.get('x')
    y_value = data.get('y')
    coordinates.append((x_value,y_value))
# print(coordinates)
    

def plot_graph(G):

  edges = []
  for i in range(len(cammino)-1):
    edges.append((cammino[i],cammino[i+1]))
  # pos = nx.spring_layout(G, k=2)
  fig, ax = plt.subplots()
  #label1 = nx.get_node_attributes(G, 'nome')
  #label2 = nx.get_node_attributes(G, 'gradimento')
  #label3 = nx.get_node_attributes(G, 'durata')
  edge_labels = nx.get_edge_attributes(G, 'tempo')
  nx.draw(G, coordinates, ax=ax, with_labels=True)
  nx.draw_networkx_labels(G, coordinates)
  nx.draw_networkx_nodes(G, coordinates, nodelist=cammino, node_color="tab:red")
  nx.draw_networkx_edges(G, coordinates, edgelist=edges, width=3, edge_color="tab:red")
  #nx.draw_networkx_labels(G, pos, label1)
  #nx.draw_networkx_labels(G, pos, label2)
  #nx.draw_networkx_labels(G, pos, label3)
  #nx.draw_networkx_edge_labels(G, pos, edge_labels)
  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
  plt.axis("on")
  plt.xlabel("X-axis Label")
  plt.ylabel("Y-axis Label")
  plt.show()

plot_graph(G)


