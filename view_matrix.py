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

def writeToFile(fsm,filename):
	with open(filename,'wb') as outfile:
		outfile.write("need to fill this in!")
		
# ... and parse a 2D array to interpret as state transition matrix and create Graph