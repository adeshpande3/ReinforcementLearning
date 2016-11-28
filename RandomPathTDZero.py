import numpy as np

# This program is to create an RL agent and see if it can learn to perform 
# correctly in a simple environment. The environment will be a 1-D path
# that has a reward at one end of the path. This program uses the TD(0)
# technique for adjusting the value function

# +1 reward at the right, 0 reward everywhere else
# If agent reaches either end, the episode terminates
path = np.array([0,0,0,0,0,0,0,0,0,1])

class Agent:
	def __init__(self):
		self.valueFunction = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]) #Value function at every position is the same, initially
		self.curLoc = 4 #Starting index is at the middle
		self.alphaRate = .0001

		# V(s) = V(s) + alpha*(R(t+1) + V(s+1) - V(s))
	def simulateEpisode(self):
		while True:
			probability = np.random.rand()
			if (probability >= .5): # Go Right
				self.curLoc += 1;
				if (self.curLoc == 9):
					self.valueFunction[self.curLoc-1] += self.alphaRate*(1 + self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc-1])
					return
				else:
					self.valueFunction[self.curLoc-1] += self.alphaRate*(self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc-1])
					
			else: # Go Left
				self.curLoc -= 1;
				if (self.curLoc == 0):
					self.valueFunction[self.curLoc+1] += self.alphaRate*(self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc+1])
					return
				else:
					self.valueFunction[self.curLoc+1] += self.alphaRate*(self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc+1])


numEpisodes = 10000
my_agent = Agent()
for i in range(1,numEpisodes):
	my_agent.simulateEpisode()
	my_agent.curLoc = 4

print "The value function is ", my_agent.valueFunction[1:9]


