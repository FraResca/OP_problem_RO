import networkx as nx



def misura(G, path):
  time_path = 0
  score = 0

  for i in range(len(path)-1):
    if((path[i],path[i+1]) in G.edges):
      time_path += G[path[i]][path[i+1]]['time']
      score += G.nodes[path[i+1]]['score']
    else:
      if((path[i+1],path[i]) in G.edges):
        time_path += G[path[i+1]][path[i]]['time']
        score += G.nodes[path[i]]['score']

  return time_path,score

def path_accettabile(G, path, TMax):

  # inizia e temina nello stesso nodo
  if path[0] != path[-1]:
    return False

  
  for node in path:
    # tutti i nodi sono nodi del grafo
    if node not in G.nodes:
      return False
    # i nodi non si ripetono
    if node != path[0] and path.count(node) > 1:
      return False

  tempo_path,_ = misura(G,path)

  # rimane da vincolare il tempo del tour
  if tempo_path > TMax:
    return False

  return True


