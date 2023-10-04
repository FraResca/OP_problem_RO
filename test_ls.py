import networkx as nx
from istance_parser import *
from local_search import *
from tabu_search import *
from grasp import *

TMax,G = from_op_format("set_66_1_060.txt")
path = ricerca_greedy_nn(G,0,TMax)

ls_opt_add_remove = ls_opt2_add_remove(G,path,0,TMax)
print(ls_opt_add_remove, misura(G, ls_opt_add_remove))

ls_swap_add_remove = ls_swap_add_remove(G,path,0,TMax)
print(ls_swap_add_remove, misura(G, ls_swap_add_remove))

tabu = tabu_search(G,0,TMax)
print(tabu, misura(G,tabu))

grasppath = ricerca_grasp(G,0,TMax,100)
print(grasppath, misura(G,grasppath))

