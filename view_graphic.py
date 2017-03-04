import matplotlib.pyplot as plt
import networkx as moo


"""
accepts a networkx object (dict of dicts) and renders

fsm		finite state machine represented as a networkx Graph (dict of dicts)
"""
def plotMe(fsm):
	moo.draw(fsm)
	plt.show()

