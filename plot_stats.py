import networkx as nx
import json
import os

from matplotlib import pyplot as plt

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
      plt.savefig('stat_plots/' + titolo + '.jpeg')
      #plt.show()
      plt.close()
    

def allplots():
  plot_points("results/set_64_1_50.json")
  plot_points("results/set_66_1_080.json")
  plot_points("results/tsiligirides_problem_1_budget_85.json")
  plot_points("results/tsiligirides_problem_2_budget_45.json")
  plot_points("results/tsiligirides_problem_3_budget_110.json")
  plot_points("results/Ferrara_90.json")

allplots()