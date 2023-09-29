from utils import *
from moves import *
from greedy import *

def first_improvement(G, route, paths):
  addlist = []
  _,score = misura(G,route)

  for path in paths:
    addlist += add_moves(G,path)

  for add in addlist:
    _,temp_score = misura(G,add)
    if temp_score > score:
      return add

  return route


def best_improvement(G, route, paths, TMax):
  addlist = []
  _,score = misura(G,route)
  for path in paths:
    addlist += add_moves(G,path,TMax)

  for add in addlist:
    _,temp_score = misura(G,add)
    if temp_score > score:
      route = add
      score = temp_score

  return route


def ls_opt2_add_remove(G,albergo,TMax):
  best_path = []
  best_score = 0
  path = ricerca_greedy_nn(G,albergo,TMax)

  while True:
    paths = opt2(G,path,1,TMax)
    path = best_improvement(G,path,paths,TMax)
    paths = remove_moves(G,path,TMax)
    path = best_improvement(G,path,paths,TMax)
    _,score = misura(G,path)
    if path == best_path:
      return path

    if score > best_score:
      best_path = path
      best_score = score

def ls_swap_add_remove(G,albergo,TMax):
  best_path = []
  best_score = 0
  path = ricerca_greedy_nn(G,albergo,TMax)

  while True:
    paths = swaps(G,path,1,TMax)
    path = best_improvement(G,path,paths,TMax)
    paths = remove_moves(G,path,TMax)
    path = best_improvement(G,path,paths,TMax)
    _,score = misura(G,path)
    
    if path == best_path:
      return path

    if score > best_score:
      best_path = path
      best_score = score
