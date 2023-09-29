def misura(G, path):
  time_path = 0
  score = 0
  for i in range(len(path)-1):
    # percorre l'arco
    if((path[i],path[i+1]) in G.edges):
      time_path += G[path[i]][path[i+1]]['time']
      score += G.nodes[path[i+1]]['score']
    else:
      if((path[i+1],path[i]) in G.edges):
        time_path += G[path[i+1]][path[i]]['time']
        score += G.nodes[path[i]]['score']
  return time_path, score