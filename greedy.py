import networkx as nx
from utils import *
from moves import *


def ricerca_greedy_max_grad(G, albergo, TMax):
  path = [albergo]
  t_tot = 0
  end = False

  while end == False:
    succs = []
    maxgrad = 0
    maxnode = 0
    for i in range(len(G.nodes)):
      if i not in path:
        if (t_tot + G[path[-1]][i]['time'] + G[i][albergo]['time']) < TMax and G.nodes[i]['score'] > 0:
          if G.nodes[i]['score'] > maxgrad:
            maxnode=i
            maxgrad=G.nodes[i]['score']
            succs.append(i)
    if succs == []:
      t_tot += G[path[-1]][albergo]['time']
      path.append(albergo)
      end = True
    else:
      t_tot += G[path[-1]][maxnode]['time']
      path.append(maxnode)

  return path


def ricerca_greedy_nn(G, albergo, maxtime):
  path = [albergo]
  t_tot = 0
  end = False

  while end == False:
    succs = []
    mindist = 1000
    minnode = 0
    for i in range(len(G.nodes)):
      if i not in path:
        if (t_tot + G[path[-1]][i]['time'] + G[i][albergo]['time']) < maxtime and G.nodes[i]['score'] > 0:
          if G[path[-1]][i]['time'] < mindist:
            minnode=i
            mindist=G[path[-1]][i]['time']
            succs.append(i)
    if succs == []:
      t_tot += G[path[-1]][albergo]['time']
      path.append(albergo)
      end = True
    else:
      t_tot += G[path[-1]][minnode]['time']
      path.append(minnode)

  return path


def best_small_cycle(G,albergo,TMax):
  best_cycle = []
  best_score = 0
  for i in range(len(G.nodes)):
    if i != albergo:
      if path_accettabile(G,[albergo,i,albergo],TMax):
        _,score = misura(G,[albergo,i,albergo])
        if score >= best_score:
          best_cycle = [albergo,i,albergo]
          best_score = score
  return best_cycle

def ricerca_greedy_max_insert(G,albergo,TMax):
  path = best_small_cycle(G,albergo,TMax)
  while True:
    better_path = best_add(G,path,TMax)
    if better_path == path:
      return better_path
    else:
      path = better_path



