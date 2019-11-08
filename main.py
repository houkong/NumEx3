from Pendulum import*
import matplotlib.pyplot as plt
import poincare

"""
pendel = Pendulum.with_rk4(stop=60, step=0.01)

t, theta, _ = pendel(F_D = 1.2)
t2, theta2, _ = pendel(theta0=0.21)

plt.plot(t, theta)
plt.plot(t2, theta2)
plt.show()
"""


t, theta, omega = Pendulum.with_euler_cromer(stop=500000, step=0.1)(F_D=1.2)
theta, omega = poincare.section(t, theta, omega, 2*np.pi/params.Omega_D)

plt.plot(theta, omega, 'b.')
plt.show()
