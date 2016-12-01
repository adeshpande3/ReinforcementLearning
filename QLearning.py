import numpy as np
import sys
# This program is to create an RL agent and see if it can learn to perform 
# correctly in a simple environment. The environment will be a 1-D path
# that has a reward at one end of the path. This program uses a Q Learning
# approach to find the optimal policy. 

# +1 reward at the right, 0 reward everywhere else
# If agent reaches either end, the episode terminates
path = np.array([0,0,0,0,0,0,1])

class Agent:
	def __init__(self):
		self.QFunction = np.full((path.size, 2), .5) #Action value function at every position is the same, initially
		self.curLoc = 3 #Starting index is at the middle
		self.alphaRate = .1

		# Q(s,a) = Q(s,a) + alpha*(R(t+1) + argmax(Q) - Q(s,a))
	def simulateEpisode(self):
		while True:
			probability = np.random.rand()
			epsilon = .01
			if (probability <= epsilon): #Take random action (epsilon greedy policy)
				probability = np.random.rand()
				if (probability >= .5):
					action = 1; #Go Right
				else:
					action = 0; #Go Left
			else:
				action = np.argmax(self.QFunction[self.curLoc,:]) #Act greedily with respect to the Q function.

			if (action == 1): # Go Right
				self.curLoc += 1;
				if (self.curLoc == 6):
					# You get a +1 reward if you reach the rightmost space
					self.updateQFunction(self.curLoc, action, 1, -1)
					#self.QFunction[self.curLoc-1, action] += self.alphaRate*
					#(1 + np.argmax(self.QFunction[self.curLoc,:]) - self.QFunction[self.curLoc-1, action])
					return
				else:
					self.updateQFunction(self.curLoc, action, 0, -1)
					#self.QFunction[self.curLoc-1, action] += self.alphaRate*
					#(np.argmax(self.QFunction[self.curLoc,:]) - self.QFunction[self.curLoc-1, action])
					
			else: # Go Left
				self.curLoc -= 1;
				if (self.curLoc == 0):
					# You don't get any reward if you reach the leftmost space
					self.updateQFunction(self.curLoc, action, 0, 1)
					#self.QFunction[self.curLoc+1, action] += self.alphaRate*(-self.valueFunction[self.curLoc+1])
					return
				else:
					self.updateQFunction(self.curLoc, action, 0, 1)
					#self.QFunction[self.curLoc+1, action] += self.alphaRate*(self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc+1])


	def updateQFunction(self, location, action, reward, direction):
		self.QFunction[location + direction, action] += self.alphaRate*(reward + np.argmax(self.QFunction[location,:]) - self.QFunction[location + direction, action])

numEpisodes = 100
my_agent = Agent()
for i in range(1,numEpisodes):
	my_agent.simulateEpisode()
	my_agent.curLoc = 3

print "The value function is ", my_agent.QFunction[1:6]