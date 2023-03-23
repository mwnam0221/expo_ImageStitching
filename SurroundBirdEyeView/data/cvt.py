import numpy as np

camera_matrix = [[407.436654, 0.000000, 639.500000],
[0.000000, 407.436654, 359.500000],
[0.000000, 0.000000, 1.000000]]

distortion= [[0.000000 ], 
[0.000000 ],
[0.000000],
[0.000000]]


np.save('./right/new_camera_right_K.npy', camera_matrix)
np.save('./right/new_camera_right_D.npy', distortion)

