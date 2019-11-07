from Pendulum import*
import matplotlib.pyplot as plt

t, theta = Pendulum.with_rk4()()
#t, theta = Pendulum.with_euler_cromer()()
plt.plot(t, theta)
plt.show()