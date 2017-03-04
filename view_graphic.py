"""
VIEW: VISUAL GRAPHIC
Render a visual representation of the finite state machine (network graph)
ultimately, also provide functionality for interaction
"""

# Support for graphic rendering
import matplotlib.pyplot as plt

"""
Render a graph in a visual display

nx		handle to the NetworkX library functionality
fsm		networkx Graph (dict of dicts) that represents the finite state machine
"""
def plotMe(nx,fsm):
	# basic initial functionality
	nx.draw(fsm)
	plt.show()
	
	# additions...?
	# node color based on attribute
	# label with node names
	# show direction of edges (check if it is a directed graph)
	# provide interactivity...

