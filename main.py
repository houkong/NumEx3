from Pendulum import*
import matplotlib.pyplot as plt


pendel = Pendulum.with_rk4(stop=60, step=0.01)

t, theta, _ = pendel(F_D = 1.2)
t2, theta2, _ = pendel(theta0=0.21)

plt.plot(t, theta)
plt.plot(t2, theta2)
plt.show()