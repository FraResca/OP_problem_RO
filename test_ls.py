import networkx as nx
from istance_parser import *
from local_search import *
from tabu_search import *

TMax,G = from_op_format("tsiligirides_problem_3_budget_110.txt")
ls_opt_add_remove = ls_opt2_add_remove(G,0,TMax)
ls_swap_add_remove = ls_swap_add_remove(G,0,TMax)
tabu = tabu_search(G,0,TMax)

print(ls_opt_add_remove, misura(G, ls_opt_add_remove))
print(ls_swap_add_remove, misura(G, ls_swap_add_remove))
print(tabu, misura(G,tabu))