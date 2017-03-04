# Controller: 
import networkx as nx

# support from within this project
import view_graphic


G=nx.Graph()
G.add_edge(1,2)

view_graphic.plotMe(G)
