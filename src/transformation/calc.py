import numpy as np 


ORIGINAL = {67., 43, 58, 28, 74, 65, 70, 42, 57, 60}

DECIMAL_SCALING = {.67, .43, .58, .28, .74, .65, .70, .42, .57, .60}
INTERQUARTILE_RANGE = {.4, -0.8, -0.05, -1.55, .75, .3, .55, -0.85, -0.1, .05}
MAX_MIN = {0.848, 0.326, 0.652, 0.000, 1.000, 0.804, 0.913, 0.304, 0.630, 0.696}
TRIVIAL = {0.905, 0.581, 0.866, 0.378, 1.000, 0.878, 0.946, 0.568, 0.770, 0.811}
Z_SCORE = {0.731, -.925, 0.110, -1.96, 1.214, 0.593, 0.938, -.994, 0.041, 0.248}


arr = np.array(list(ORIGINAL))

for i in range(len(arr)):
    arr[i] /= np.float32(100.0)


print(arr.size)    
print(arr)