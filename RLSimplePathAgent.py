import numpy as np

# This program is to create an RL agent and see if it can learn to perform 
# correctly in a simple environment. The environment will be a 1-D path
# that has rewards at either end of the path 

# +10 reward at the ends, 0 reward everywhere else
path = np.array([10,0,0,0,0,0,0,0,0,10])
