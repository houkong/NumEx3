import numpy as np
import params


class Pendulum:
    def __init__(self, method, stop=100, step=0.01):
        # params
        self.method = method
        self.stop = stop
        self.step = step

        # default params from params.py
        self.params = {
            "g":        params.g,
            "l":        params.l,
            "q":        params.q,
            "F_D":      params.F_D,
            "Omega_D":  params.Omega_D,
            "theta0":   params.theta0,
            "omega0":   params.omega0
        }

    def __call__(self, **kwargs):
        for key, value in kwargs.items():
            assert key in self.params
            self.params[key] = value
        return self.method(self.stop, self.step, self.theta_prime, self.omega_prime, self.params["theta0"],
                           self.params["omega0"])

    @classmethod
    def with_rk4(cls, stop=60, step=0.01):
        def rk4(stop, step, theta_prime, omega_prime, theta0, omega0):
            t = np.arange(0, stop, step)
            n = int(stop / step)
            omega = np.zeros(n)
            theta = np.zeros(n)
            omega[0], theta[0] = omega0, theta0
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
                theta[i + 1] = Pendulum.reduce_angle(theta[i] + (step / 6) * (t1 + 2 * t2 + 2 * t3 + t4))
            return t, theta, omega
        return cls(rk4, stop, step)

    @classmethod
    def with_simple_euler(cls, stop=60, step=0.01):
        def simple_euler(stop, step, theta_prime, omega_prime, theta0, omega0):
            t = np.arange(0, stop, step)
            n = int(stop / step)
            omega = np.zeros(n)
            theta = np.zeros(n)
            omega[0], theta[0] = omega0, theta0
            for i in range(n - 1):
                omega[i + 1] = omega[i] + omega_prime(theta[i], omega[i], t[i]) * step
                theta[i + 1] = Pendulum.reduce_angle(theta[i] + theta_prime(None, omega[i], None) * step)
            return t, theta, omega0
        return cls(simple_euler, stop, step)

    @classmethod
    def with_euler_cromer(cls, stop=60, step=0.01):
        def euler_cromer(stop, step, theta_prime, omega_prime, theta0, omega0):
            t = np.arange(0, stop, step)
            n = int(stop / step)
            omega = np.zeros(n)
            theta = np.zeros(n)
            omega[0], theta[0] = omega0, theta0
            for i in range(n - 1):
                omega[i + 1] = omega[i] + omega_prime(theta[i], omega[i], t[i]) * step
                theta[i + 1] = Pendulum.reduce_angle(theta[i] + theta_prime(None, omega[i + 1], None) * step)
            return t, theta, omega
        return cls(euler_cromer, stop, step)

    def omega_prime(self, theta, omega, t):
        return -(self.params["g"] / self.params["l"]) * np.sin(theta) - self.params["q"] * omega + self.params["F_D"]*np.sin(self.params["Omega_D"]*t)

    @staticmethod
    def theta_prime(theta, omega, t):
        return omega

    @staticmethod
    def reduce_angle(alpha):
        if alpha > np.pi:
            return Pendulum.reduce_angle(alpha - 2*np.pi)
        elif alpha < -np.pi:
            return Pendulum.reduce_angle(alpha + 2 * np.pi)
        else:
            return alpha
