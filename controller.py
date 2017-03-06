# Controller: 

import networkx as nx
# but!... might also consider: https://graph-tool.skewed.de/

"""
import statematrix
sm = statematrix.StateMatrix(inputs={'C':0, 'L':1, 'R':2},
                 outputs={'centerWater':0, 'centerLED':1})
#elif CASE==100:
sm.add_state(name='wait_for_cpoke', statetimer=12,
            transitions={'Cin':'play_target'},
            outputsOff=['centerLED'])
sm.add_state(name='play_target', statetimer=0.5,
            transitions={'Cout':'wait_for_apoke','Tup':'wait_for_cpoke'},
            outputsOn=['centerLED'])
print(sm)
"""



# support all helpers from within this project
import view_matrix


import view_graphic



import model
smm = model.StateMatrixModel()
print('Instantiated state matrix designer')

print("creating 'a place to start'")
smm.createState('a place to start')
smm.recordState()
print smm.toString()

print("creating 'and then go here'")
smm.createState('and then go here')
smm.recordState()
print smm.toString()

"""
print("creating 'and then go here' (conflict!)")
if(smd.createState('and then go here')):
	smd.recordState()
print smd.toString()
"""

print("modifying with a new transition")
smm.loadState('and then go here')
smm.addTransition('a place to start','tap button')
smm.recordState()
print smm.toString()


#smd.addTransition('yikes0','yikes1')

"""
sm.add_state(name='wait_for_cpoke', statetimer=12,
            transitions={'Cin':'play_target'},
            outputsOff=['centerLED'])
"""


"""
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
"""
