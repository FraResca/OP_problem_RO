from istance_parser import *
from greedy import *
from local_search import *
from tabu_search import *
from grasp import *
from collections import defaultdict
import time
import os
import json

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
    tot_results = defaultdict(dict)
    for node in range(len(G.nodes)):
        if G.nodes[node]["score"] == 0:
            results = defaultdict(dict)
            print(f"Albergo {node}:\n")
            
            start = time.time()
            greedy_max_grad = ricerca_greedy_max_grad(G,node,TMax)
            end = time.time()
            print("Greedy Massimo Gradimento")
            print(greedy_max_grad, misura(G, greedy_max_grad))
            tempo,score = misura(G, greedy_max_grad)
            results['GreedyMaxGrad']['path'] = greedy_max_grad
            results['GreedyMaxGrad']['score'] = score
            results['GreedyMaxGrad']['duration'] = tempo
            results['GreedyMaxGrad']['elap_time'] = end-start  

            start = time.time()
            greedy_nn = ricerca_greedy_nn(G,node,TMax)
            end = time.time()
            print("Greedy Nearest Neighbour:")
            print(greedy_nn, misura(G, greedy_nn))
            tempo,score = misura(G, greedy_nn)
            results['GreedyNearNeigh']['path'] = greedy_nn
            results['GreedyNearNeigh']['score'] = score
            results['GreedyNearNeigh']['duration'] = tempo
            results['GreedyNearNeigh']['elap_time'] = end-start

            start = time.time()
            greedy_max_ins = ricerca_greedy_max_insert(G,node,TMax)
            end = time.time()
            print("Greedy Massimo Inserimento:")
            print(greedy_max_ins, misura(G,greedy_max_ins))
            tempo,score = misura(G, greedy_max_ins)
            results['GreedyMaxIns']['path'] = greedy_max_ins
            results['GreedyMaxIns']['score'] = score
            results['GreedyMaxIns']['duration'] = tempo
            results['GreedyMaxIns']['elap_time'] = end-start
            
            start = time.time()
            greedy_ind_ins = ricerca_greedy_ind_insert(G,node,TMax)
            end = time.time()
            print("Greedy Inserimento sulla base di Indice")
            print(greedy_ind_ins, misura(G,greedy_ind_ins))
            tempo,score = misura(G, greedy_ind_ins)
            results['GreedyIndIns']['path'] = greedy_ind_ins
            results['GreedyIndIns']['score'] = score
            results['GreedyIndIns']['duration'] = tempo
            results['GreedyIndIns']['elap_time'] = end-start

            start = time.time()
            greedy_rand = ricerca_greedy_random(G,node,TMax)
            end = time.time()
            print("Greedy Random")
            print(greedy_rand, misura(G,greedy_rand))
            tempo,score = misura(G, greedy_rand)
            results['GreedyRand']['path'] = greedy_rand
            results['GreedyRand']['score'] = score
            results['GreedyRand']['duration'] = tempo
            results['GreedyRand']['elap_time'] = end-start

            start = time.time()
            ls_mg_swap = ricerca_locale(G,greedy_max_grad,TMax,'swap',1,10)
            end = time.time()
            print("Ricerca locale - Greedy Massimo Gradimento - Swap")
            print(ls_mg_swap, misura(G,ls_mg_swap))
            tempo,score = misura(G, ls_mg_swap)
            results['LSMGSwap']['path'] = ls_mg_swap
            results['LSMGSwap']['score'] = score
            results['LSMGSwap']['duration'] = tempo
            results['LSMGSwap']['elap_time'] = end-start

            start = time.time()
            ls_nn_swap = ricerca_locale(G,greedy_nn,TMax,'swap',1,10)
            end = time.time()
            print("Ricerca locale - Greedy Nearest Neighbour - Swap")
            print(ls_nn_swap, misura(G,ls_nn_swap))
            tempo,score = misura(G, ls_nn_swap)
            results['LSNNSwap']['path'] = ls_nn_swap
            results['LSNNSwap']['score'] = score
            results['LSNNSwap']['duration'] = tempo
            results['LSNNSwap']['elap_time'] = end-start

            start = time.time()
            ls_mi_swap = ricerca_locale(G,greedy_max_ins,TMax,'swap',1,10)
            end = time.time()
            print("Ricerca locale - Greedy Massimo Inserimento - Swap")
            print(ls_mi_swap, misura(G,ls_mi_swap))
            tempo,score = misura(G, ls_mi_swap)
            results['LSMISwap']['path'] = ls_mi_swap
            results['LSMISwap']['score'] = score
            results['LSMISwap']['duration'] = tempo
            results['LSMISwap']['elap_time'] = end-start

            start = time.time()
            ls_mg_2opt = ricerca_locale(G,greedy_max_grad,TMax,'2opt',1,10)
            end = time.time()
            print("Ricerca locale - Greedy Massimo Gradimento - 2opt")
            print(ls_mg_2opt, misura(G,ls_mg_2opt))
            tempo,score = misura(G, ls_mg_2opt)
            results['LSMG2opt']['path'] = ls_mg_2opt
            results['LSMG2opt']['score'] = score
            results['LSMG2opt']['duration'] = tempo
            results['LSMG2opt']['elap_time'] = end-start

            start = time.time()
            ls_nn_2opt = ricerca_locale(G,greedy_nn,TMax,'2opt',1,10)
            end = time.time()
            print("Ricerca locale - Greedy Nearest Neighbour - 2opt")
            print(ls_nn_2opt, misura(G,ls_nn_2opt))
            tempo,score = misura(G, ls_nn_2opt)
            results['LSNN2opt']['path'] = ls_nn_2opt
            results['LSNN2opt']['score'] = score
            results['LSNN2opt']['duration'] = tempo
            results['LSNN2opt']['elap_time'] = end-start

            start = time.time()
            ls_mi_2opt = ricerca_locale(G,greedy_max_ins,TMax,'2opt',1,10)
            end = time.time()
            print("Ricerca locale - Greedy Massimo Inserimento - 2opt")
            print(ls_mi_2opt, misura(G,ls_mi_2opt))
            tempo,score = misura(G, ls_mi_2opt)
            results['LSMI2opt']['path'] = ls_mi_2opt
            results['LSMI2opt']['score'] = score
            results['LSMI2opt']['duration'] = tempo
            results['LSMI2opt']['elap_time'] = end-start

            ls_results = [ls_mg_swap,ls_nn_swap,ls_mi_swap,ls_mg_2opt,ls_nn_2opt,ls_mi_2opt]
            
            start = time.time()
            ts_ls = tabu_search(G,best_route(G,ls_results),TMax,750)
            end = time.time()
            print("Ricerca Tabu - Miglior Ricerca Locale")
            print(ts_ls, misura(G,ts_ls))
            tempo,score = misura(G, ts_ls)
            results['TSLS']['path'] = ts_ls
            results['TSLS']['score'] = score
            results['TSLS']['duration'] = tempo
            results['TSLS']['elap_time'] = end-start

            start = time.time()
            ts_ls_int = tabu_search_int_div(G,best_route(G,ls_results),TMax,750)
            end = time.time()
            print("Ricerca Tabu Intensificazione Diversificazione - Miglior Ricerca Locale")
            print(ts_ls_int, misura(G,ts_ls_int))
            tempo,score = misura(G, ts_ls_int)
            results['TSLSINT']['path'] = ts_ls_int
            results['TSLSINT']['score'] = score
            results['TSLSINT']['duration'] = tempo
            results['TSLSINT']['elap_time'] = end-start

            start = time.time()
            grasp = ricerca_grasp(G,node,TMax,35)
            end = time.time()
            print("Grasp")
            print(grasp, misura(G,grasp))
            tempo,score = misura(G, grasp)
            results['Grasp']['path'] = grasp
            results['Grasp']['score'] = score
            results['Grasp']['duration'] = tempo
            results['Grasp']['elap_time'] = end-start

            print("\n")
            
            tot_results[node] = results

    return tot_results

def test_OP_format(filerelpath):
    filename = os.path.basename(filerelpath)
    print(filename,"\n")
    TMax,G = from_op_format(filerelpath)
    result = all_tests(TMax,G)
    filename = filename.split('.')
    filename = filename[0]
    filename = f"{filename}.json"
    filename = "results/" + filename
    with open(filename,'w') as outfile:
        json.dump(result,outfile)
    

def test_Ferrara(TMax):
    print(f"Ferrara_{TMax}\n")
    G = from_ferrara()
    result = all_tests(TMax,G)
    filename = f"Ferrara_{TMax}.json"
    filename = "results/" + filename
    with open(filename,'w') as outfile:
        json.dump(result,outfile)

'''
test_OP_format("set_64_1/set_64_1_50.txt")
test_OP_format("set_64_1/set_64_1_80.txt")
test_OP_format("set_66_1/set_66_1_080.txt")
test_OP_format("set_66_1/set_66_1_130.txt")
test_OP_format("Tsiligirides_1/tsiligirides_problem_1_budget_50.txt")
test_OP_format("Tsiligirides_1/tsiligirides_problem_1_budget_85.txt")
test_OP_format("Tsiligirides_2/tsiligirides_problem_2_budget_35.txt")
test_OP_format("Tsiligirides_2/tsiligirides_problem_2_budget_45.txt")
test_OP_format("Tsiligirides_3/tsiligirides_problem_3_budget_050.txt")
test_OP_format("Tsiligirides_3/tsiligirides_problem_3_budget_110.txt")
test_Ferrara(60)
test_Ferrara(90)
'''