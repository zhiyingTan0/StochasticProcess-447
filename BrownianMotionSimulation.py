import numpy as np
import matplotlib.pyplot as plt

"""
    Simulate Brownian Motion by discretization the model
    s(t) = s(t-1) + /mu *delta_t + /sigma * sqrt(delta_t)*Z(0,1)
    /mu: the drift
    /sigma: the volatility
"""
def simulate_brownian_motion(dt, n_steps, drift=0.01, volatility=0.2):
    # Time step (assuming each step represents 1 unit of time)

    # increment of standard Brownian motion
    random_shocks = np.random.normal(0, 1, n_steps)

    # Initialize the array to store the Brownian motion path
    path = np.zeros(n_steps)

    # Simulate the Brownian motion with drift and volatility
    for t in range(1, n_steps):
        path[t] = path[t - 1] + drift * dt + volatility * np.sqrt(dt) * random_shocks[t]

    return path


# Simulate Brownian motion for 1,000 steps
n_steps = 100
dt = 1 # delta_t
brownian_path = simulate_brownian_motion(dt, n_steps)
# Plot the result
plt.plot(brownian_path)
plt.title('Simulated Brownian Motion with Drift and Volatility')
plt.xlabel('Time')
plt.ylabel('S(t)')
plt.show()
