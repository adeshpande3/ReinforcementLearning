import numpy as np

# This program is to create an RL agent and see if it can learn to perform 
# correctly in a simple environment. The environment will be a 1-D path
# that has a reward at one end of the path. This program uses the Monte Carlo
# technique for adjusting the value function. 

# Monte Carlo is different from
# TD in that you update the value function after each episode, not after 
# each move. This is because we need to observe the total reward until
# the episode finishes, in order to make the value function update. 

# +1 reward at the right, 0 reward everywhere else
# If agent reaches either end, the episode terminates
path = np.array([0,0,0,0,0,0,1])

class Agent:
	def __init__(self):
		self.valueFunction = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5]) #Value function at every position is the same, initially
		self.curLoc = 3 #Starting index is at the middle
		self.alphaRate = .1

		# V(s) = V(s) + alpha*(G(t) - V(s))
	def simulateEpisode(self):
		positionsVisited = []
		while True:
			positionsVisited.append(self.curLoc)
			probability = np.random.rand()
			if (probability >= .5): # Go Right
				self.curLoc += 1;
				if (self.curLoc == 6):
					# You get a +1 reward if you reach the rightmost space
					self.updateValueFunction(positionsVisited, 1)
					return	
			else: # Go Left
				self.curLoc -= 1;
				if (self.curLoc == 0):
					# You don't get any reward if you reach the leftmost space
					self.updateValueFunction(positionsVisited, 0)
					return

	def updateValueFunction(self, positions, reward):
		if (reward == 1):
			for pos in positions:
				self.valueFunction[pos] += self.alphaRate*(1 - self.valueFunction[pos])
		else:
			for pos in positions:
				self.valueFunction[pos] += self.alphaRate*(-self.valueFunction[pos])

numEpisodes = 10000
my_agent = Agent()
for i in range(0,numEpisodes):
	my_agent.simulateEpisode()
	my_agent.curLoc = 3

print "The value function is ", my_agent.valueFunction[1:6]


