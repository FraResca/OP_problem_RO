from utils import *
from greedy import *
from local_search import *
from istance_parser import*
import copy

def tabu_remove(G,path,intens):
  best_score = 0
  for i in path:
    if i != path[0] and i not in intens:
      
      newpath = copy.copy(path)
      newpath.remove(i)
      _,newscore = misura(G,newpath)
      if newscore > best_score:
        best_path = newpath
        best_score = newscore
        tabu_node = i
      
  return best_path,tabu_node

'''
def tabu_remove(path,intens):
  newpath = copy.copy(path)
  nodes = [i for i in range(1,len(newpath)-1) if newpath[i] not in intens]
  rand_node = random.choice(nodes)
  tabu_node = newpath[rand_node]
  del newpath[rand_node]
  return newpath,tabu_node
'''
  
def tabu_add_moves(G,path,tabu_list,TMax,divers):
  movlist = []
  for i in range(len(G.nodes)):
    if i not in path and i not in tabu_list and i not in divers and G.nodes[i]["score"] > 0:
      for j in range(1,len(path)):
        cpypath = copy.copy(path)
        cpypath.insert(j,i)
        if(path_accettabile(G,cpypath,TMax)):
          movlist.append(cpypath)
  return movlist

def tabu_best_improvement(G,route,paths,tabu_list,TMax,divers):
  addlist = []
  _,score = misura(G,route)
  for path in paths:
    addlist += tabu_add_moves(G,path,tabu_list,TMax,divers)

  for add in addlist:
    _,temp_score = misura(G,add)
    if temp_score > score:
      route = add
      score = temp_score

  return route


def tabu_search(G,path,TMax,MaxIter):

  MaxTabuList = 5
  cont = 0
  _,best_score = misura(G,path)
  best_path = path
  tabu_list = []

  while True:
    paths = opt2(G,path,1,TMax)
    newpath = tabu_best_improvement(G,path,paths,tabu_list,TMax,[])
    
    cont += 1
    
    if newpath == path:
      path,tabu_node = tabu_remove(path,[])
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

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def disgiunction(lst1, lst2):
    lst3 = [value for value in lst1 if value not in lst2]
    return lst3

def multi_intersection(lists):
    inters = lists[0][0]
    for i in range(1,len(lists)):
      inters = intersection(inters,lists[i][0])
    return inters    

def pos_tendency(last_list):
  if len(last_list) > 1:
    for i in range(1,len(last_list)):
      if last_list[i][1] <= last_list[i-1][1]:
        return False
  return True

def neg_tendency(last_list):
  if len(last_list) > 1:
    for i in range(1,len(last_list)):
      if last_list[i][1] > last_list[i-1][1]:
        return False
    return True

def thin(G,fat):
  thinner = copy.copy(fat)
  worst_score = 1000
  for i in range(1,len(thinner)-1):
    if G.nodes[thinner[i]]['score'] < worst_score:
      worst_node = i
  del thinner[worst_node]
  return thinner

def tabu_search_int_div(G,path,TMax,MaxIter):
  albergo = path[0]
  MaxTabuList = 5
  MaxMem = 5
  ShortMem = 3
  cont = 0
  _,best_score = misura(G,path)
  best_path = path
  tabu_list = []
  long_mem = []
  intens = []
  divers = []

  while True:
    paths = opt2(G,path,1,TMax)
    newpath = tabu_best_improvement(G,path,paths,tabu_list,TMax,[])
    
    cont += 1
    
    if newpath == path:
      path,tabu_node = tabu_remove(path,intens)
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

      long_mem.append([path,addscore])
      if len(long_mem) > MaxMem:
        del long_mem[0]

      if len(long_mem) == MaxMem:
        if pos_tendency(long_mem) == True:
          intens = multi_intersection(long_mem)
          while len(intens) > len(path)/2:
            intens = thin(G,intens)
          divers = []
        else: intens = []
        if neg_tendency(long_mem[:-ShortMem]) == True:
          divers = multi_intersection(long_mem)
          path = [albergo] + disgiunction(path,divers) + [albergo]
          intens = []
          cont = 0

    if cont > MaxIter:
        return best_path