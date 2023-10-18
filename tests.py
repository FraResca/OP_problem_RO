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
            
            ts_ls_divint = tabu_search_div_int(G,best_route(G,ls_results),TMax,100)
            print("Ricerca Tabu Intensificazione Diversificazione")
            print(ts_ls_divint, misura(G,ts_ls_divint))
            
            grasp = ricerca_grasp(G,node,TMax,25)
            print("Grasp")
            print(grasp, misura(G,grasp))
            
            print("\n")

def test_OP_format(filerelpath):
    TMax,G = from_op_format(filerelpath)
    all_tests(TMax,G)

def test_Ferrara(TMax):
    G = from_ferrara()
    all_tests(TMax,G)

print("Chao 64 - 50\n")
test_OP_format("set_64_1/set_64_1_50.txt")
print("Chao 64 - 80\n")
test_OP_format("set_64_1/set_64_1_80.txt")

print("Chao 66 - 85\n")
test_OP_format("set_64_1/set_66_1_085.txt")
print("Chao 66 - 130\n")
test_OP_format("set_64_1/set_66_1_130.txt")

print("Tsiligrides 1 - 60\n")
test_OP_format("Tsiligrides_1/tsiligirides_problem_1_budget_60.txt")
print("Tsiligrides 1 - 85\n")
test_OP_format("Tsiligrides_1/tsiligirides_problem_1_budget_85.txt")

print("Tsiligrides 2 - 30\n")
test_OP_format("Tsiligrides_2/tsiligirides_problem_2_budget_30.txt")
print("Tsiligrides 2 - 45\n")
test_OP_format("Tsiligrides_2/tsiligirides_problem_2_budget_45.txt")

print("Tsiligrides 3 - 30\n")
test_OP_format("Tsiligrides_3/tsiligirides_problem_3_budget_70.txt")
print("Tsiligrides 3 - 30\n")
test_OP_format("Tsiligrides_3/tsiligirides_problem_3_budget_110.txt")

print("Ferrara - 60")
test_Ferrara(60)
print("Ferrara - 90")
test_Ferrara(90)
