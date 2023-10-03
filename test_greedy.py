import networkx as nx
from istance_parser import *
from greedy import *

TMax,G = from_op_format("tsiligirides_problem_3_budget_110.txt")
greedy_max_grad = ricerca_greedy_max_grad(G,0,TMax)
greedy_nn = ricerca_greedy_nn(G,0,TMax)
greedy_max_ins = ricerca_greedy_max_insert(G,0,TMax)
greedy_ind_ins = ricerca_greedy_ind_insert(G,0,TMax)
greedy_rand_1 = ricerca_greedy_random(G,0,TMax)
greedy_rand_2 = ricerca_greedy_random(G,0,TMax)
greedy_rand_3 = ricerca_greedy_random(G,0,TMax)

print(greedy_max_grad, misura(G, greedy_max_grad))
print(greedy_nn, misura(G, greedy_nn))
print(greedy_max_ins, misura(G,greedy_max_ins))
print(greedy_ind_ins, misura(G,greedy_ind_ins))
print(greedy_rand_1, misura(G,greedy_rand_1))
print(greedy_rand_2, misura(G,greedy_rand_2))
print(greedy_rand_3, misura(G,greedy_rand_3))
