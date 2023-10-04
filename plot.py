import networkx as nx
from matplotlib import pyplot as plt

from istance_parser import *
from local_search import *
from tabu_search import *
from grasp import *

TMax,G = from_op_format("set_66_1_130.txt")
path = ricerca_greedy_nn(G,0,TMax)

def plot_graph(G):
  pos = nx.spring_layout(G, scale=2)
  #label1 = nx.get_node_attributes(G, 'nome')
  #label2 = nx.get_node_attributes(G, 'gradimento')
  #label3 = nx.get_node_attributes(G, 'durata')
  edge_labels = nx.get_edge_attributes(G, 'tempo')
  nx.draw(G, pos)
  nx.draw_networkx_labels(G, pos)
  #nx.draw_networkx_labels(G, pos, label1)
  #nx.draw_networkx_labels(G, pos, label2)
  #nx.draw_networkx_labels(G, pos, label3)
  #nx.draw_networkx_edge_labels(G, pos, edge_labels)
  plt.show()

plot_graph(G)