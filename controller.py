# Controller: 
import networkx as nx

# support all helpers from within this project
import view_graphic
import view_matrix

# Instantiate a finite state machine (network graph)... 
# ultimately the graph will be built up through interaction with the graphic view
# (or read in from a state transition matrix)
fsm=nx.Graph()

# again, edges will be added through interaction (or parsing a state transition matrix)
fsm.add_edge(1,2)

# Visualize the 
view_graphic.plotMe(nx,fsm)

# Serialize the graph
view_matrix.prettyPrint(fsm)
# separate function? or implement an optional parameter on the prettyPrint?
#view_matrix.writeToFile(fsm,'demo.csv')