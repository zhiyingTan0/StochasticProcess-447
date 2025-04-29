import math
import numpy as np


"""
 Consider entire random walk as 1 trial
 p_hat = probability of reaching position 0 at least once
 1-p_hat = probability of failing to reaching position 0 at any steps

 Intuition: According to CLT, when independent random sample size init_num_trials is large enough, with a finite mu & sigma. 
 The sample mean will approximate a normal distribution. Mean of the sample in here is exactly 
 
 Standard Deviation estimate 1 =  sqrt(estimate_p*(1-estimate_p)) --> when sample is large > 30, (CLT) and confident enough it is a Binomial
 Standard Deviation estimate 2 =  sample standard deviation (s) --> when sample is small
 Standard Error is sigma/sqrt(n)
"""

N = 10
init_num_trials= 1000 # intialize a sample size to estimate probability
p = 0.52 # probability of step forward +1
E=np.array([0.1, 0.001, 0.0001, 0.0001, 0.00001]) # target margin of errors
z_score = 1.96 # z_score of 95% confidence interval

def simulate_random_walk_numpy(N, p, num_trials):
    pos=5
    samples = np.random.binomial(n=1, p=p, size=num_trials*N).reshape(num_trials,N)*2-1
    estimate_prob = np.sum((np.cumsum(samples, axis=1)+pos <= 0).any(axis=0) ) / num_trials
    return estimate_prob

def calculate_sample_size (N, p, E, z_score):
    p_hat = simulate_random_walk_numpy(N, p, init_num_trials)

    # 95% CI estimate_prob
    # E = z_score*estimate_stderr = z_score * sqrt(p*(1-p))/sqrt(sample_size)
    # --> sample_size = z_score^2 *(1-p)*p / E^2
    sample_size = math.pow(z_score,2)*(1-p_hat)*p_hat / np.pow(E, 2)
    print(f"At least a sample size of {sample_size} is required to achieve accuracy ", E)

calculate_sample_size(N,p, E, z_score)











