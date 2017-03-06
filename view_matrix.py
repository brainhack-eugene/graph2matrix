"""
VIEW: TEXT-BASED MATRIX
Translate (serialize) the finite state machine as a two dimensional array that 
represents the state transition matrix
""" 

"""
Create the state transition matrix

fsm		networkx Graph (dict of dicts) that represents the finite state machine
"""
def prettyPrint(fsm):
	# basic version for now...
	print(fsm.adj)

		
