import networkx as nx
import * from utils

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