import numpy as np

"""Simulate the N steps transition of a Markov chain - Weather"""

states = ['Sunny', 'Rainy', 'Cloudy', 'Snowy', 'Windy']
transition_matrix = np.array([[0.575, 0.118 , 0.172 , 0.109 , 0.026],
                              [0.453 , 0.243 , 0.148 , 0.123 , 0.033],
                             [0.104 , 0.343 , 0.367 , 0.167 , 0.019],
                             [0.015 , 0.066 , 0.318 , 0.505 , 0.096],
                             [0.004 , 0.060 , 0.149 , 0.567 , 0.22]])

""" Matrix power of N """
N = 5
power_N = np.linalg.matrix_power(transition_matrix, N)
print("Transition Matrix P^N : ",power_N)


# Initial state distribution (probabilities)
initial_state = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # start with all 20% chance

# Number of steps
num_steps = 100

# Simulate discrete-time Markov chain
# np.random.choice(): randomly selects an element from a given list based on specified probabilities
current_state = np.random.choice(states, p=initial_state)
print(f"Step 0: {current_state}")

for step in range(1, num_steps + 1):
    current_index = states.index(current_state) #index of current state
    current_state = np.random.choice(states, p=transition_matrix[current_index])
    print(f"Step {step}: {current_state}")

