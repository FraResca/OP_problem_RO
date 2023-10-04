from utils import *
from greedy import *
import copy

def tabu_remove(G,path,albergo):
  best_score = 0
  for i in path:
    if i != albergo:
      newpath = copy.copy(path)
      newpath.remove(i)
      _,newscore = misura(G,newpath)
      if newscore > best_score:
        best_path = newpath
        best_score = newscore
        tabu_node = i
  return best_path, tabu_node

def tabu_best_imp(G,path,tabu_list,TMax):
  best_score = 0
  best_path = path
  for i in range(3,len(G.nodes)):
    if i not in tabu_list and i not in path:
      for j in range(1, len(path)-1):
        newpath = copy.copy(path)
        newpath.insert(j,i)
        if path_accettabile(G,newpath,TMax):
          _,newscore = misura(G,newpath)
          if newscore > best_score:
            best_path = newpath
            best_score = newscore
  return best_path

def best_opt2(G,path,TMax):
  best_time,_ = misura(G,path)
  best_opt = path
  opt2s = opt2_moves(G,path,TMax)
  for opt2 in opt2s:
    time,_ = misura(G,opt2)
    if time < best_time:
      best_opt = opt2
      best_time = time
  return best_opt


def tabu_search(G,albergo,TMax):

  MaxTabuList = 10
  cont = 0
  MaxIter = 1000
  path = ricerca_greedy_nn(G,albergo,TMax)
  _,best_score = misura(G,path)
  best_path = path
  tabu_list = []

  while True:
    path = best_opt2(G,path,TMax)
    addpath = tabu_best_imp(G,path,tabu_list,TMax)
    cont += 1
    if addpath == path:
      path,tabu_node = tabu_remove(G,path,albergo)
      tabu_list.append(tabu_node)
      if len(tabu_list) > MaxTabuList:
        del tabu_list[0]
    else:
      path = addpath
      _,addscore = misura(G,addpath)
      if addscore > best_score:
        best_path = addpath
        best_score = addscore
        cont = 0

    if cont > MaxIter:
      return best_path