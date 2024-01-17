from utils import *
from greedy import *
from local_search import *
from istance_parser import*
import copy

def tabu_remove(G,path,intens):
  newpath = copy.copy(path)
  nodes = [i for i in range(1,len(newpath)-1) if newpath[i] not in intens]
  rand_node = random.choice(nodes)
  tabu_node = newpath[rand_node]
  del newpath[rand_node]
  return newpath,tabu_node

'''
def tabu_remove(G,path,intens):
  newpath = copy.copy(path)
  nodes = [i for i in range(1,len(newpath)-1) if newpath[i] not in intens]
  worst_node = nodes[0]
  for node in nodes:
    if G.nodes[node]["score"] < G.nodes[worst_node]["score"]:
      worst_node = node
  tabu_node = newpath[worst_node]
  del newpath[worst_node]
  return newpath,tabu_node
'''
  
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
      path,tabu_node = tabu_remove(G,path,[])
      tabu_list.append(tabu_node)
      if len(tabu_list) > MaxTabuList:
        del tabu_list[0]
    else:
      path = newpath
      _,addscore = misura(G,newpath)
      if addscore > best_score:
        best_path = newpath
        best_score = addscore
        #cont = 0

    if cont > MaxIter:
      return best_path


def growing(G,mem):
  _,last_score = misura(G,mem[0])
  for i in range(1,len(mem)):
    _,score = misura(G,mem[i])
    if score >= last_score:
      last_score = score
    else: return False
  return True

def intersection(lst1, lst2):
  lst3 = [value for value in lst1 if value in lst2]
  return lst3

def multi_intersection(paths):
  inters = paths[0]
  for i in range(1,len(paths)):
    inters = intersection(inters,paths[i])
  return inters

def intensification(G,mem,MaxInt):
  intens = multi_intersection(mem)
  if len(intens) > MaxInt:
    intens = random.sample(intens,MaxInt)
  return intens

def disjunction(lst1, lst2):
  lst3 = [value for value in lst1 if value not in lst2]
  return lst3

def multi_disjunction(paths):
  inters = paths[0]
  for i in range(1,len(paths)):
    inters = disjunction(paths[i],inters)
  return inters

def diversification(G,mem,albergo):
  divers = multi_disjunction(mem)
  divers = [albergo] + divers + [albergo]
  return divers

def tabu_search_int_div(G,path,TMax,MaxIter):

  MaxTabuList = 5
  cont = 0
  _,best_score = misura(G,path)
  best_path = path
  tabu_list = []
  MaxMem = 20
  LongMem = 10
  ShortMem = 5
  mem = []
  MaxInt = 5
  intens = []
  
  while True:
    paths = opt2(G,path,1,TMax)
    newpath = tabu_best_improvement(G,path,paths,tabu_list,TMax)
    
    cont += 1
    
    if newpath == path:
      path,tabu_node = tabu_remove(G,path,intens)
      tabu_list.append(tabu_node)
      if len(tabu_list) > MaxTabuList:
        del tabu_list[0]
    else:
      path = newpath
      _,addscore = misura(G,newpath)
      if addscore > best_score:
        best_path = newpath
        best_score = addscore
        #cont = 0
    
    if(len(tabu_list)!=0):
      mem.append(path)
      if len(mem) > MaxMem:
        del mem[0]

    if len(mem) >= ShortMem and growing(G,mem[-ShortMem:]):
            intens = intensification(G,mem,MaxInt)
    if len(mem) == MaxMem and len(tabu_list) == MaxTabuList:  
        if not(growing(G,mem)):
            path = diversification(G,mem[-LongMem:],path[0])
            mem = []
            intens = []
            tabu_list = []

    if cont > MaxIter:
      return best_path