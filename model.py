class SingleState(object):
	# TODO: from statematrix.py - include in StateMatrix object and access there?  or global?
	# default timer duration: more time than a task is expected to last
	# conceptually equivalent to infinite duration
	VERYLONGTIME = 100
	
	# A unique list of transitions that occur in this state
	# transition matrix; this list gets augmented, but does not
	# track counts of instances to support removal (if there are
	# unused transition actions, they will end up being an empty
	# column in the computed matrix representation)
	TRANSITION_LIST = set()
	
	
	# the state will be assigned a unique identifier within the state matrix
	# when it gets added to the StateMatrix object
	def __init__(self,name,isNew=True):
		# required values
		if not name:
			raise Exception('Each state must have a name.')
		self._name = name
		self._statetimer = SingleState.VERYLONGTIME
		
		# fill in default values, as needed
		self._transitions = {}
		self._outputsOn = []
		self._outputsOff = []
		self._trigger = []
		self._serialOut = 0
		self._isNew = isNew
	
	@property
	def name(self):
		""" (Human friendly) label for the state """
		return self._name
	
	@property
	def statetimer(self):
		""" Duration of the state (max time when setting a countdown timer) """
		return statetimer._name
	
	def addTransition(self,toName,action):
		self._transitions[action]=toName
		SingleState.TRANSITION_LIST.add(action)
	
	""" ------------------------------------------------------------------------ 
	MATRIX VIEW 
	
	Functionalty to support a (text-based) matrix view of the finite state
	machine
	"""
	@staticmethod
	def toStringHeader():
		result = '  label \t\t'
		for a in SingleState.TRANSITION_LIST:
			result += a+'\t'
		return result
		
	def toString(self):
		result = self._name+'\t'
		for a in SingleState.TRANSITION_LIST:
			if a in self._transitions:
				result += self._transitions[a]+'\t' 
			else: 
				result += '--None--\t'
		return result


# needs to be Python3
# uses Tk...
class StateMatrixModel(object):
	def __init__(self):
		self.nodeList = {}

	"""
	Create a SingleState object to collect all of the details for a 
	new state

	Returns true on success, false otherwise
	"""
	def createState(self,name):
		if(name in self.nodeList):
			print('... A node by that name already exists: '+name)
			return False
		else:
			self.stateInProgress = SingleState(name)
			return True

	def loadState(self,name):
		if(name in self.nodeList):
			self.stateInProgress = self.nodeList[name]
			return True
		else:
			print('... Unable to find node: '+name)
			return False

	def addTransition(self,toName,action):
		if(self.stateInProgress):
			self.stateInProgress.addTransition(toName,action)
		else:
			print('... Create or load a state before attempting to modify')
	
	def recordState(self):
		if(self.stateInProgress):
			self.nodeList[self.stateInProgress.name]=self.stateInProgress
			self.stateInProgress = None
		else:
			print('... No state in progress')
	

	""" ------------------------------------------------------------------------ 
	MATRIX VIEW 

	Functionalty to support a (text-based) matrix view of the finite state
	machine
	"""		
	def toString(self):
		result = SingleState.toStringHeader()+'\n'
		i=0
		for n in self.nodeList:
			result += str(i)+' '+self.nodeList[n].toString()+'\n'
			i+=1
		return result

	def writeToFile(self,filename):
		with open(filename,'wb') as outfile:
			outfile.write("need to fill this in!")

	# parse a 2D array from a file to interpret as finite state machine
	def readFromFile(self,filename):
		with open(filename,'rb') as infile:
			for line in file:
				print '.'
			print 'Do something...'


	def saveToStateMatrix(self):
		# instantiate a statematrix object and populate it with all of the 
		# accumulated details
		self.sm.add_state(
			self.stateInProgress.name,
			self.stateInProgress.statetimer,
			self.stateInProgress.transitions,
			self.stateInProgress.outputsOn,
			self.stateInProgress.outputsOff,
			self.stateInProgress.trigger,
			self.stateInProgress.serialOut);
		print self.sm
# end class def: statematrixDesigner
