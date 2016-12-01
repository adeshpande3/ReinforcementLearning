import numpy as np

# This program is to create an RL agent and see if it can learn to perform 
# correctly in a simple environment. The environment will be a 1-D path
# that has a reward at one end of the path. This program uses the TD(0)
# technique for adjusting the value function

# +1 reward at the right, 0 reward everywhere else
# If agent reaches either end, the episode terminates

# Got the practice problem from here: http://i.stack.imgur.com/JHdT2.png
path = np.array([0,0,0,0,0,0,1])

class Agent:
	def __init__(self):
		self.valueFunction = np.array([0.5,0.5,0.5,0.5,0.5,0.5,0.5]) #Value function at every position is the same, initially
		self.curLoc = 3 #Starting index is at the middle
		self.alphaRate = .1

		# V(s) = V(s) + alpha*(R(t+1) + V(s+1) - V(s))
	def simulateEpisode(self):
		while True:
			probability = np.random.rand()
			if (probability >= .5): # Go Right
				self.curLoc += 1;
				if (self.curLoc == 6):
					# You get a +1 reward if you reach the rightmost space
					self.valueFunction[self.curLoc-1] += self.alphaRate*(1 + self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc-1])
					return
				else:
					self.valueFunction[self.curLoc-1] += self.alphaRate*(self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc-1])
					
			else: # Go Left
				self.curLoc -= 1;
				if (self.curLoc == 0):
					# You don't get any reward if you reach the leftmost space
					self.valueFunction[self.curLoc+1] += self.alphaRate*(-self.valueFunction[self.curLoc+1])
					return
				else:
					self.valueFunction[self.curLoc+1] += self.alphaRate*(self.valueFunction[self.curLoc] - self.valueFunction[self.curLoc+1])


numEpisodes = 100
my_agent = Agent()
for i in range(1,numEpisodes):
	my_agent.simulateEpisode()
	my_agent.curLoc = 3

print "The value function is ", my_agent.valueFunction[1:6]
v_function = my_agent.valueFunction[1:6]
v_function = v_function/sum(v_function)
print "The value function is ", v_function


