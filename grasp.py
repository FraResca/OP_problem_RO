import networkx as nx
from utils import misura
from greedy import ricerca_greedy_random
from local_search import *


def ricerca_grasp(G,albergo,TMax,Iter):
    best_score = 0
    best_path = []
    for i in range(Iter):    

        path = ricerca_greedy_random(G,albergo,TMax)
        path = ls_opt2_add_remove(G,path,TMax)

        _,score = misura(G,path)
        
        if score > best_score:
            best_score = score
            best_path = path

    return best_path




