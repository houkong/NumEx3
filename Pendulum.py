import numpy as np
import params


class Pendulum:
    def __init__(self, method, friction=params.q, force=params.F_D):
        self.method = method
        self.friction = friction
        self.force = force

    def __call__(self, stop=100, step=0.01):
        return self.method(stop, step, self.theta_prime, self.omega_prime)

    @classmethod
    def with_rk4(cls, friction=params.q, force=params.F_D ):
        return cls(Pendulum.rk4, friction, force)

    @staticmethod
    def rk4(stop, step, theta_prime, omega_prime):
        t = np.arange(0, stop, step)
        n = int(stop / step)
        omega = np.zeros(n)
        theta = np.zeros(n)
        omega[0], theta[0] = params.omega0, params.theta0
        for i in range(n - 1):
            # calculate next omega
            o1 = omega_prime(theta[i], omega[i], t[i])
            o2 = omega_prime(theta[i] + o1 * step / 2, omega[i], t[i])
            o3 = omega_prime(theta[i] + o2 * step / 2, omega[i], t[i])
            o4 = omega_prime(theta[i] + o3 * step, omega[i], t[i])
            omega[i + 1] = omega[i] + (step / 6) * (o1 + 2 * o2 + 2 * o3 + o4)

            # calculate next theta
            t1 = theta_prime(None, omega[i], None)
            t2 = theta_prime(None, omega[i] + t1 * step / 2, None)
            t3 = theta_prime(None, omega[i] + t2 * step / 2, None)
            t4 = theta_prime(None, omega[i] + t3 * step, None)
            theta[i + 1] = theta[i] + (step / 6) * (t1 + 2 * t2 + 2 * t3 + t4)

        return t, theta

    def omega_prime(self, theta, omega, t):
        return -(params.g / params.l) * theta - self.friction * omega + self.force*np.sin(params.Omega_D*t)

    def theta_prime(self, theta, omega, t):
        return omega
