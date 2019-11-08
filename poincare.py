import numpy as np

def section(t, _theta, _omega, mod):
    n = len(t)
    tol = t[1]-t[0]
    points = int(n//mod)
    theta = np.zeros(points)
    omega = np.zeros(points)
    count = 0
    for i, t_i in enumerate(t):
        if abs(t_i % mod) < tol/2:
            theta[count] = _theta[i]
            omega[count] = _omega[i]
            count += 1
    return theta, omega