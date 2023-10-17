from istance_parser import *
from utils import *
from greedy import *
from local_search import *
import random

# pensavo di partire con 4 o 8 greedy randomizzate per il pool iniziale dei genitori

# si accoppiano le greedy generando figli composti dai nodi che i genitori hanno in comune (in pratica intersezione)
# i figli si migliorano con la ls

# si itera tenendo le n soluzioni migliori

def insert_sorted(G,pool,new,DimPool):
    _,scorenew = misura(G,new)
    #print("prima", pool)
    if pool == []:
        pool = [new]
    else:
        _,maxscore = misura(G,pool[-1])
        if maxscore <= scorenew:
            pool.append(new)
        else:
            for j in range(len(pool)):
                        _,score = misura(G,pool[j])
                        if scorenew < score:
                            pool.insert(j,new)
                            break
    
    if len(pool) > DimPool:
        del pool[0]

    return pool

def intersection(path1,path2):
    path3 = [i for i in path1 if i in path2]
    return path3

def newson(G,albergo,pool,TMax):
    MaxTentativi = 50
    for _ in range(MaxTentativi):
        samples = random.sample(range(len(pool)),2)
        newpath = intersection(pool[samples[0]],pool[samples[1]])
        if path_accettabile(G,newpath,TMax):
            newpath = ls_opt2_add_remove(G,newpath,TMax)
            return newpath
    return ricerca_greedy_random(G,albergo,TMax)

def genetic_ibrid(G,albergo,TMax,MaxIter,DimPool):
    pool = []

    for _ in range(DimPool):
        greedy = ricerca_greedy_random(G,albergo,TMax)
        newpool = insert_sorted(G,pool,greedy,DimPool)
        pool = newpool

    for i in range(MaxIter):
        son = newson(G,albergo,pool,TMax)
        newpool = insert_sorted(G,pool,son,DimPool)
        pool = newpool
        
    return pool[-1]
