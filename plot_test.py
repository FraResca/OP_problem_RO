import networkx as nx
import json
import os

from matplotlib import pyplot as plt

from istance_parser import *
from local_search import *
from tabu_search import *
from grasp import *

#TMax,G = from_op_format("Tsiligirides_1/tsiligirides_problem_1_budget_50.txt")

#path = ricerca_greedy_nn(G,0,TMax)

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


def plot_points(jsonfile):
  f = open(jsonfile)
  data = json.load(f)
  for albergo in data:
    titles = ['Greedy','LS','OltreLS']
    for title in titles:
      fig = plt.figure()
      X = []
      Y = []
      lab = []
      for tecnica in data[albergo]:
        if title == 'Greedy' or title == 'LS':
          if tecnica.startswith(title):
            X.append(round(data[albergo][tecnica]['elap_time'],5))
            Y.append(round(data[albergo][tecnica]['score'],5))
            lab.append(tecnica)
        else:
          if tecnica.startswith('TS') or tecnica == 'Grasp':
            X.append(round(data[albergo][tecnica]['elap_time'],5))
            Y.append(round(data[albergo][tecnica]['score'],5))
            lab.append(tecnica)
      filename = os.path.basename(jsonfile)
      filename = os.path.splitext(filename)[0]
      titolo = filename + "_Albergo_"+ str(int(albergo)+1) + '_' + title
      plt.title(titolo)
      plt.xlabel('Tempo')
      plt.ylabel('Score')
      plt.plot(X,Y,'o')
      for i, txt in enumerate(lab):
        plt.annotate(txt,(X[i],Y[i]),ha='center',va='bottom')
      plt.grid()
      plt.savefig('plots/' + titolo + '.jpeg')
      #plt.show()
      plt.close()
    

def allplots():
  plot_points("results/set_64_1_50.json")
  plot_points("results/set_66_1_080.json")
  plot_points("results/tsiligirides_problem_1_budget_85.json")
  plot_points("results/tsiligirides_problem_2_budget_45.json")
  plot_points("results/tsiligirides_problem_3_budget_110.json")
  plot_points("results/Ferrara_90.json")


#print_json("results/tsiligirides_problem_1_budget_50.json")

#plot_graph(G,path)

allplots()