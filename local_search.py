from utils import *
from moves import *
from greedy import *


def first_improvement(G, route, paths):
    addlist = []
    _, score = misura(G, route)

    for path in paths:
        addlist += add_moves(G, path)

    for add in addlist:
        _, temp_score = misura(G, add)
        if temp_score > score:
            return add

    return route


def best_improvement(G, route, paths, TMax):
    addlist = []
    _, score = misura(G, route)
    for path in paths:
        addlist += add_moves(G, path, TMax)

    for add in addlist:
        _, temp_score = misura(G, add)
        if temp_score > score:
            route = add
            score = temp_score

    return route


def ls_opt2_add_remove(G, initpath, TMax):
    best_path = []
    best_score = 0
    # path = ricerca_greedy_nn(G,albergo,TMax)
    path = initpath
    while True:
        paths = opt2(G, path, 1, TMax)

        newpath = best_improvement(G, path, paths, TMax)

        if (newpath == path):
            paths = remove_moves(G, path, TMax)
            path = best_improvement(G, path, paths, TMax)
        else:
            path = newpath

        _, score = misura(G, path)
        if path == best_path:
            return path

        if score > best_score:
            best_path = path
            best_score = score


def ls_swap_add_remove(G, initpath, TMax):
    best_path = []
    best_score = 0
    # path = ricerca_greedy_nn(G,albergo,TMax)
    path = initpath

    while True:
        paths = swaps(G, path, 1, TMax)
        newpath = best_improvement(G, path, paths, TMax)
        if (newpath == path):
            paths = remove_moves(G, path, TMax)
            path = best_improvement(G, path, paths, TMax)
        else:
            path = newpath
        _, score = misura(G, path)
        # print(path)
        if path == best_path:
            return path

        if score > best_score:
            best_path = path
            best_score = score


def ricerca_locale(G, initpath, TMax, movetype, depth, MaxIter):
  best_path = []
  best_score = 0
  path = initpath
  cont = 0

  while True:
    if movetype == 'swap':
      paths = swaps(G, path, depth, TMax)
    elif movetype == '2opt':
        paths = opt2(G, path, depth, TMax)

    newpath = best_improvement(G, path, paths, TMax)
    if (newpath == path):
        cont += 1
        paths = remove_moves(G, path, TMax)
        path = best_improvement(G, path, paths, TMax)
    else:
        path = newpath

    _, score = misura(G, path)

    if cont == MaxIter:
        return best_path

    if score > best_score:
        cont = 0
        best_path = path
        best_score = score
