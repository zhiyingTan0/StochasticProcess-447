import numpy as np

"""Simple Monte Carlo simulation - toss coin to estimate probability of at least K heads in N tosses"""
N=10 # N toss each trial
p=0.5 # probability of Head
k=5 # at least k Head of N toss
trials=10000 # number of experiments

# generate N random numbers uniformly from [0,1)
# <.5 is T  >=.5 is H
def toss_N_times(N, p):
    return np.sum(np.random.rand(N) < p)
def coin_toss_monte_carlo(N, k, p, trials):
    at_least_k = 0
    for _ in range(trials):
        if toss_N_times(N, p) >= k:
            at_least_k += 1
    return at_least_k/trials

print(f"Perform {trials} trials, probability of at least {k} Heads in {N} toss is: {coin_toss_monte_carlo(N, k, p, trials)}")


