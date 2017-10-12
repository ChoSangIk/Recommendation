import math
import numpy as np

np.set_printoptions(precision=2,linewidth=120)

def weight(matrix):
        target_matrix = matrix
        totalItems = matrix.shape[0]
        totalGenres = matrix.shape[1]
        
        matrix_weights = np.zeros(matrix.shape) 
    
        for i in range(0, totalGenres):
            col = matrix[:,i]
            idf = math.log10(totalItems/col.sum())
            
            for j in range(0, totalItems):
                matrix_weights[j, i] = matrix[j, i] * idf
        return matrix_weights