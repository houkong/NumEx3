from Pendulum import*
import matplotlib.pyplot as plt
import os
if not os.path.exists("plots"):
    os.mkdir("plots")


# Exercise one
pendulum = Pendulum.with_rk4(stop=60, step=0.01)
t1, theta1, omega1 = pendulum(F_D=0.0)
t2, theta2, omega2 = pendulum(F_D=0.5)
t3, theta3, omega3 = pendulum(F_D=1.2)
fig, axes = plt.subplots(2,3,sharex='col')

axes[1,0].plot(t1, theta1, label="F_D = 0.0", color="r"); axes[0,0].set_ylabel("ω [rad/s]")
axes[0,0].plot(t1, omega1, label="F_D = 0.0", color="r"); axes[1,1].set_xlabel("t [s]")
axes[1,1].plot(t2, theta2, label="F_D = 0.5", color="g");
axes[0,1].plot(t2, omega2, label="F_D = 0.5", color="g"); axes[1,0].set_ylabel("θ [rad]")
axes[1,2].plot(t3, theta3, label="F_D = 1.2", color="b");
axes[0,2].plot(t3, omega3, label="F_D = 1.2", color="b");
fig.legend(["F_D = 0.0", "F_D = 0.5", "F_D = 1.2"])
fig.tight_layout()
plt.savefig("plots\exercise1.png")
plt.clf()


# Exercise two
pendulum = Pendulum.with_rk4(stop=75, step=0.005)
t, delta_theta = pendulum.lyapunov(0.001, F_D=0.5)
plt.plot(t, np.log(delta_theta), label="F_D = 0.5")
t, delta_theta = pendulum.lyapunov(0.001, F_D=1.2)
plt.plot(t, np.log(delta_theta), label="F_D = 1.2")
plt.xlabel("t [s]")
plt.ylabel("ln(Δθ) [ln(rad)]")
plt.legend()
plt.savefig("plots\lyapunov.png")
plt.clf()

# Exercise three
pendulum = Pendulum.with_euler_cromer(stop=10000, step=0.1)
theta1, omega1 = pendulum.poincare_section(F_D=0.5)
theta2, omega2 = pendulum.poincare_section(F_D=1.2)

plt.plot(theta1, omega1, 'b.')
plt.plot(theta1, omega1, 'b.', label="F_D = 0.5")
plt.plot(theta2, omega2, 'r.', label="F_D = 1.2")
plt.xlabel("θ [rad]")
plt.ylabel("ω [rad/s]")
plt.legend()
plt.savefig("plots\poincaresection.png")
plt.clf()


# Demonstration that chaotic behaviour is also manifested in that different numerical solvers
# yields completely different trajectories for F_D = 1.2
t1, theta1, _ = Pendulum.with_euler_cromer(stop=60, step=0.001)(F_D=1.2)
t2, theta2, _ = Pendulum.with_rk4(stop=60, step=0.001)(F_D=1.2)
t3, theta3, _ = Pendulum.with_simple_euler(stop=60, step=0.001)(F_D=1.2)
plt.plot(t1, theta1, label="Euler-Cromer")
plt.plot(t2, theta2, label="Runge Kutta 4")
plt.plot(t3, theta3, label="Simple Euler")
plt.xlabel("t [s]")
plt.ylabel("θ [rad]")
plt.legend()
plt.savefig("plots\different_num_methods.png")





