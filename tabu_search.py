from utils import *
from greedy import *
from local_search import *
import copy

def tabu_remove(G,path):
  best_score = 0
  for i in path:
    if i != path[0]:
      newpath = copy.copy(path)
      newpath.remove(i)
      _,newscore = misura(G,newpath)
      if newscore > best_score:
        best_path = newpath
        best_score = newscore
        tabu_node = i
  return best_path, tabu_node

def tabu_add_moves(G,path,tabu_list,TMax):
  movlist = []
  for i in range(len(G.nodes)):
    if i not in path and i not in tabu_list and G.nodes[i]["score"] > 0:
      for j in range(1,len(path)):
        cpypath = copy.copy(path)
        cpypath.insert(j,i)
        if(path_accettabile(G,cpypath,TMax)):
          movlist.append(cpypath)
  return movlist

def tabu_best_improvement(G,route,paths,tabu_list,TMax):
  addlist = []
  _,score = misura(G,route)
  for path in paths:
    addlist += tabu_add_moves(G,path,tabu_list,TMax)

  for add in addlist:
    _,temp_score = misura(G,add)
    if temp_score > score:
      route = add
      score = temp_score

  return route


def tabu_search(G,path,TMax,MaxIter):

  MaxTabuList = 10
  cont = 0
  _,best_score = misura(G,path)
  best_path = path
  tabu_list = []

  while True:
    paths = opt2(G,path,1,TMax)
    newpath = tabu_best_improvement(G,path,paths,tabu_list,TMax)
    
    cont += 1
    
    if newpath == path:
      path,tabu_node = tabu_remove(G,path)
      tabu_list.append(tabu_node)
      if len(tabu_list) > MaxTabuList:
        del tabu_list[0]
    else:
      path = newpath
      _,addscore = misura(G,newpath)
      if addscore > best_score:
        best_path = newpath
        best_score = addscore
        cont = 0

    if cont > MaxIter:
      return best_path
