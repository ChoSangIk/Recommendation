
from numpy import linalg as LA
import numpy as np
norms = LA.norm(weights,ord=2,axis=1) 
dots = np.matmul(weights, weights.T)
sims = np.divide(np.divide(dots, norms).T, norms)
return sims