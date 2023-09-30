from utils import *
import copy

def add_moves(G,path,TMax):
  movlist = []
  for i in range(4,len(G.nodes)):
    if i not in path:
      for j in range(1,len(path)):
        cpypath = copy.copy(path)
        cpypath.insert(j,i)
        if(path_accettabile(G,cpypath,TMax)):
          movlist.append(cpypath)
  return movlist

def first_add(G,route):
  paths = add_moves(G,route)
  best_score = 0
  for path in paths:
    _,score = misura(G,path)
    if score > best_score:
      return path
  return route

def best_add(G,path,TMax):
  paths = add_moves(G,path,TMax)
  best_path = []
  best_score = 0
  for path in paths:
    _,score = misura(G,path)
    if score > best_score:
      best_path = path
      best_score = score
  if best_path == []:
    return path
  else: return best_path



def best_add_ind(G,path,TMax):
  paths = add_moves(G,path,TMax)
  best_path = []
  best_score = 0
  for path in paths:
    score = misura_ind(G,path)
    if score > best_score:
      best_path = path
      best_score = score
  if best_path == []:
    return path
  else: return best_path


def swap_moves(G,path,TMax):
  movlist = []
  for i in range(len(path)-1):
    for j in range(i+1, len(path)):
      cpypath = copy.copy(path)
      temp = cpypath[j]
      cpypath[j] = cpypath[i]
      cpypath[i] = temp
      if(path_accettabile(G,cpypath,TMax)):
        movlist.append(cpypath)
  return movlist

def swaps(G,path,depth,TMax):
  swaplist = []
  if depth == 1:
    swaplist += swap_moves(G,path,TMax)
  elif depth > 1:
    swaplist += swaps(G,path,depth-1,TMax)
    for swap in swaplist:
      deep_swaps = swap_moves(G,swap,TMax)
      for d_swap in deep_swaps:
        if d_swap not in swaplist:
          swaplist.append(d_swap)
  return swaplist


def opt2_moves(G,path,TMax):
  movlist = [path]
  for i in range(1,len(path)-1):
    for j in range(i+2, len(path)):
      if len(path[i:j])!=len(path)-2:
        substr = copy.copy(path[i:j])
        substr.reverse()
        newstr = path[:i] + substr + path[j:]
        if(path_accettabile(G,newstr,TMax)):
          movlist.append(newstr)
  return movlist

def opt2(G,path,depth,TMax):
  opt2list = []
  if depth == 1:
    opt2list += opt2_moves(G,path,TMax)
  elif depth > 1:
    opt2list += opt2(G,path,depth-1,TMax)
    for opt in opt2list:
      deep_opt2 = opt2_moves(G,opt)
      for d_opt2 in deep_opt2:
        if d_opt2 not in opt2list:
          opt2list.append(d_opt2)
  return opt2list


def remove_moves(G,path,TMax):
  movlist=[]
  for i in range(1,len(path)-1):
    cpypath = copy.copy(path)
    cpypath.remove(cpypath[i])
    if(path_accettabile(G,cpypath,TMax)):
      movlist.append(cpypath)
  return movlist