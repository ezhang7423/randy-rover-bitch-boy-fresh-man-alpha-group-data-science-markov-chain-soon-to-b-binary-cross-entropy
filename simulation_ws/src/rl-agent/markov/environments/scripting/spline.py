import numpy as np
import matplotlib.pyplot as plt
import os


os.chdir('correct')
splines = np.array([[[0.0000, 0.0000], [-3.1785, -0.0953], [-9.5096, -2.8057], [-10.9285, -3.4642]], [[-10.9285, -3.4642], [-12.1964, -4.0728], [-15.7917, -5.6964], [-16.6071, -7.7857]], [[-16.6071, -7.7857], [-17.2561, -9.2857], [-19.0, -9.5475], [-19.8332, -8.8214]], [[-19.8332, -8.8214], [-20.6668, -8.0954], [-22.2857, -6.1786], [-23.9286, -5.517]], [[-23.9286, -5.517], [-25.5714, -4.9643], [-32.3393, -4.0893], [-35.3929, -3.6786]], [[-35.3929, -3.6786], [-37.6429, -3.5357], [-40.625, -3.3929], [-44.2500, -4.0000]]])
 
def blend(a, b, alpha):
        return b * alpha + a * (1-alpha)
 
def evaluate_at_alpha(a, b, c, d, alpha):
    a1 = blend(a, b, alpha)
    b1 = blend(b, c, alpha)
    c1 = blend(c, d, alpha)
 
    a2 = blend(a1, b1, alpha)
    b2 = blend(b1, c1, alpha)
   
    return blend(a2, b2, alpha)
 
 
def discretize_splines(splines):
    spline_points = []
    for i in range(0, len(splines)):
        for alpha in np.arange(0, 1.00, 0.06): # (6 / step) + 1
            spline_points.append(evaluate_at_alpha(splines[i][0], splines[i][1], splines[i][2], splines[i][3], alpha)) 
   
    spline_points.append(np.array([-44.25, -4.00]))
    return np.array(spline_points)
 
 
spline_points = discretize_splines(splines)
print("spline_points!")
print(spline_points)
 
 
spline_x = spline_points[:, 0]
spline_x = spline_x[2:]
print("spline_x:")
print(spline_x)
 
spline_y = spline_points[:, 1]
spline_y = spline_y[2:]
plt.plot(spline_x, spline_y)
 


np.save('spline_x.npy', spline_x)
np.save('spline_y.npy', spline_y)
plt.show()