from istance_parser import *
from utils import *
from greedy import *

# pensavo di partire con 4 o 8 greedy randomizzate per il pool iniziale dei genitori

# si accoppiano le greedy generando figli composti dai nodi che i genitori hanno in comune
# i figli si migliorano con la ls

# si itera tenendo le n soluzioni migliori

# NON FUNZIONA UN CAZZO

def insert_sorted(G,pool,new,DimPool):
    _,scorenew = misura(G,new)
    #print("prima", pool)
    if pool == []:
        pool = [new]   
    else:
        for j in range(len(pool)):
                    _,score = misura(G,pool[j])
                    if scorenew < score:
                        pool.insert(j,new)
                        break
        #pool.append(new)
    #print("dopo", pool)

    return pool

def genetic_ibrid(G,albergo,TMax):
    DimPool = 8
    pool = []
    for i in range(DimPool):
        greedy = ricerca_greedy_random(G,albergo,TMax)
        newpool = insert_sorted(G,pool,greedy,DimPool)
        pool = newpool

    for i in pool:
        print(i, misura(G,i))

TMax,G = from_op_format("set_66_1_060.txt")

genetic_ibrid(G,0,TMax)
