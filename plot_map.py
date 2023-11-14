import networkx as nx
from matplotlib import pyplot as plt
import os

from istance_parser import *
from local_search import *
from tabu_search import *
from grasp import *

def plot_graph(G,path,titolo):
  coordinates = []
  for node, data in G.nodes(data=True):
    x_value = data.get('x')
    y_value = data.get('y')
    coordinates.append((x_value,y_value))

  edges = []
  for i in range(len(path)-1):
    edges.append((path[i],path[i+1]))

  fig, ax = plt.subplots()

  edge_labels = nx.get_edge_attributes(G, 'tempo')
  nx.draw(G, coordinates, ax=ax, with_labels=True)
  nx.draw_networkx_labels(G, coordinates)
  nx.draw_networkx_nodes(G, coordinates, nodelist=path, node_color="tab:red")
  nx.draw_networkx_edges(G, coordinates, edgelist=edges, width=3, edge_color="tab:red")

  ax.tick_params(left=True, bottom=True, labelleft=True, labelbottom=True)
  plt.title(titolo)
  plt.axis("on")
  plt.xlabel("Longitudine")
  plt.ylabel("Latitudine")
  #plt.show()
  plt.savefig('graph_plots/' + titolo + '.jpeg')
  plt.close()

def util_plot(G,filename):
  jsonpath = 'results/' + filename + '.json'
  f = open(jsonpath)
  data = json.load(f)
  for albergo in data:
    for tecnica in data[albergo]:
      plot_graph(G,data[albergo][tecnica]['path'],filename+'_' + 'Albergo_' + albergo + '_' + tecnica)

def op_plotmap(filepath):
  _,G = from_op_format(filepath)
  filename = os.path.basename(filepath)
  filename = os.path.splitext(filename)[0]
  util_plot(G,filename)

def fe_plotmap(TMax):
  G = from_ferrara()
  filename = 'Ferrara_' + str(TMax)
  util_plot(G,filename)
  

op_plotmap('set_64_1/set_64_1_50.txt')
op_plotmap('set_66_1/set_66_1_080.txt')
op_plotmap('Tsiligirides_1/tsiligirides_problem_1_budget_50.txt')
op_plotmap('Tsiligirides_1/tsiligirides_problem_1_budget_85.txt')
op_plotmap('Tsiligirides_2/tsiligirides_problem_2_budget_35.txt')
op_plotmap('Tsiligirides_2/tsiligirides_problem_2_budget_45.txt')
op_plotmap('Tsiligirides_3/tsiligirides_problem_3_budget_050.txt')
op_plotmap('Tsiligirides_3/tsiligirides_problem_3_budget_110.txt')
fe_plotmap(60)
fe_plotmap(90)