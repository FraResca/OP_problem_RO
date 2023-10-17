from istance_parser import *
from greedy import *
from local_search import *
from tabu_search import *
from grasp import *
from pop_based import *

def best_route(G,routes):
    best_score = 0
    best_route = []

    for route in routes:
        _,score = misura(G,route)
        if score > best_score:
            best_route = route
            best_score = score
    
    return best_route

def all_tests(TMax,G):
    for node in range(len(G.nodes)):
        if G.nodes[node]["score"] == 0:
            print(f"Albergo {node}:\n")
            
            #greedy
            greedy_max_grad = ricerca_greedy_max_grad(G,node,TMax)
            print("Greedy Massimo Gradimento")
            print(greedy_max_grad, misura(G, greedy_max_grad))

            greedy_nn = ricerca_greedy_nn(G,node,TMax)
            print("Greedy Nearest Neighbour:")
            print(greedy_nn, misura(G, greedy_nn))
            
            greedy_max_ins = ricerca_greedy_max_insert(G,node,TMax)
            print("Greedy Massimo Inserimento:")
            print(greedy_max_ins, misura(G,greedy_max_ins))
            
            greedy_ind_ins = ricerca_greedy_ind_insert(G,node,TMax)
            print("Greedy Inserimento sulla base di Indice")
            print(greedy_ind_ins, misura(G,greedy_ind_ins))

            greedy_rand_1 = ricerca_greedy_random(G,node,TMax)
            print("Greedy Random")
            print(greedy_rand_1, misura(G,greedy_rand_1))


            ls_mg_swap = ricerca_locale(G,greedy_max_grad,TMax,'swap',1,10)
            print("Ricerca locale - Greedy Massimo Gradimento - Swap")
            print(ls_mg_swap, misura(G,ls_mg_swap))

            ls_nn_swap = ricerca_locale(G,greedy_nn,TMax,'swap',1,10)
            print("Ricerca locale - Greedy Nearest Neighbour - Swap")
            print(ls_nn_swap, misura(G,ls_nn_swap))

            ls_mi_swap = ricerca_locale(G,greedy_max_ins,TMax,'swap',1,10)
            print("Ricerca locale - Greedy Massimo Inserimento - Swap")
            print(ls_mi_swap, misura(G,ls_mi_swap))


            ls_mg_2opt = ricerca_locale(G,greedy_max_grad,TMax,'2opt',1,10)
            print("Ricerca locale - Greedy Massimo Gradimento - 2opt")
            print(ls_mg_2opt, misura(G,ls_mg_2opt))

            ls_nn_2opt = ricerca_locale(G,greedy_nn,TMax,'2opt',1,10)
            print("Ricerca locale - Greedy Nearest Neighbour - 2opt")
            print(ls_nn_2opt, misura(G,ls_nn_2opt))

            ls_mi_2opt = ricerca_locale(G,greedy_max_ins,TMax,'2opt',1,10)
            print("Ricerca locale - Greedy Massimo Inserimento - 2opt")
            print(ls_mi_2opt, misura(G,ls_mi_2opt))

            ls_results = [ls_mg_swap,ls_nn_swap,ls_mi_swap,ls_mg_2opt,ls_nn_2opt,ls_mi_2opt]

            ts_ls = tabu_search(G,best_route(G,ls_results),TMax,100)
            print("Ricerca Tabu - Miglior Ricerca Locale")
            print(ts_ls, misura(G,ts_ls))
            
            grasp = ricerca_grasp(G,node,TMax,25)
            print("Grasp")
            print(grasp, misura(G,grasp))

            ts_grasp = tabu_search(G,grasp,TMax,100)
            print("Ricerca Tabu - Grasp")
            print(ts_grasp, misura(G,ts_grasp))

            gen = genetic_ibrid(G,node,TMax,50)
            print("Algoritmo Genetico Ibrido")
            print(gen, misura(G,gen))

            print("\n")

def test_OP_format(filerelpath):
    TMax,G = from_op_format(filerelpath)
    all_tests(TMax,G)

def test_Ferrara():
    TMax,G = from_ferrara()
    all_tests(TMax,G)

test_Ferrara()