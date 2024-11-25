import numpy as np
""" Simulate a 1D random walk and calculate the probability of returning to the origin after N steps simulations."""

N = 10 # N steps of random walk
p = 0.5 # probability of move +1
num_trails = 10000 #number of experiments


def simulate_random_walk(N, p):
    """walk for N steps"""
    pos=0
    for _ in range(N):
        pos+=np.random.choice([1, -1], p=[p, 1 - p])
    return pos

def calculate_probability(N, p, num_trials):
    return_to_origin = 0
    for _ in range(num_trials):
        final_pos = simulate_random_walk(N, p)
        if final_pos == 0:
            return_to_origin += 1
    return return_to_origin/num_trials

print(f"Probability of return to origin after {N} step Ramdom walk is "
      f"{calculate_probability(N,p,num_trails): .5f}")




