from utils import *
from greedy import *
from local_search import *
from istance_parser import*
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


def tabu_remove_int(G,path,intens):
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
  return best_path, tabu_node

def tabu_add_moves_div(G,path,tabu_list,TMax,divers):
  movlist = []
  for i in range(len(G.nodes)):
    if i not in path and i not in tabu_list and i not in divers and G.nodes[i]["score"] > 0:
      for j in range(1,len(path)):
        cpypath = copy.copy(path)
        cpypath.insert(j,i)
        if(path_accettabile(G,cpypath,TMax)):
          movlist.append(cpypath)
  return movlist

def tabu_best_improvement_div(G,route,paths,tabu_list,TMax,divers):
  addlist = []
  _,score = misura(G,route)
  for path in paths:
    addlist += tabu_add_moves_div(G,path,tabu_list,TMax,divers)

  for add in addlist:
    _,temp_score = misura(G,add)
    if temp_score > score:
      route = add
      score = temp_score

  return route

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
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

# Forse ho capito male
def tabu_search_div_int(G,path,TMax,MaxIter):

  MaxTabuList = 5
  MaxMemoria = 5
  cont = 0
  _,best_score = misura(G,path)
  best_path = path
  tabu_list = []
  last_list = []
  intens = []
  divers = []

  while True:
    paths = opt2(G,path,1,TMax)
    newpath = tabu_best_improvement_div(G,path,paths,tabu_list,TMax,divers)
    
    cont += 1
    
    if newpath == path:
      path,tabu_node = tabu_remove_int(G,path,intens)
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

      last_list.append([path,addscore])
      if len(last_list) > MaxMemoria:
        del last_list[0]

      if len(last_list) == MaxMemoria:
        if pos_tendency(last_list) == True:
          intens = multi_intersection(last_list)
        elif pos_tendency(last_list) == False and intens != []:
          intens = []


        if neg_tendency(last_list) == True:
          divers = multi_intersection(last_list)
        elif neg_tendency(last_list) == False and divers != []:
          divers = []


      print("Path:",path)
      print("Tabu list:",tabu_list)
      print("Intensificazione",intens)
      print("Diversificazione",divers)
      print("Memoria")
      for i in last_list:
        print(i)

      if cont > MaxIter:
        return best_path


TMax,G = from_op_format("set_64_1/set_64_1_50.txt")
path = ricerca_greedy_max_grad(G,0,TMax)
res = tabu_search_div_int(G,path,TMax,100)
print(res,misura(G,res))
