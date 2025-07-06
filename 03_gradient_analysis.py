import numpy as np

def gradient_T(t, h, a):
    dt = 0.7046 - 0.0456*t - 0.0003*h + 0.0003*a
    dh = -0.0122 - 0.0003*t + 0.0400*h - 0.0001*a
    da = -0.0161 + 0.0003*t - 0.0001*h - 0.0014*a
    return np.array([dt, dh, da])

point = (10, 50, 200)
grad = gradient_T(*point)
print("Gradient at", point, ":", grad)
print("Steepest descent:", -grad)