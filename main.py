from Pendulum import*
import matplotlib.pyplot as plt

"""
pendel = Pendulum.with_rk4(stop=60, step=0.01)

t, theta, _ = pendel(F_D = 1.2)
t2, theta2, _ = pendel(theta0=0.21)

plt.plot(t, theta)
plt.plot(t2, theta2)
plt.show()
"""

STEP=0.01

t, theta, omega = Pendulum.with_euler_cromer(stop=40000, step=STEP)(F_D=1.2)
thetap, omegap = [], []
for i, t_i in enumerate(t):
    if abs(t_i%(2*np.pi/params.Omega_D))<STEP:
        thetap.append(theta[i])
        omegap.append(omega[i])

plt.plot(thetap, omegap, 'b.')
plt.show()
