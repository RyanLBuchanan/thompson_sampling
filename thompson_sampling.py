# Thompson Sampling Algorithm tutorial from Machine Learning A-Z - SuperDataScience -> Input by Ryan L Buchanan 15OCT 20

# Import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Import dataset
dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implement Thompson Sampling model
import random
# Number of users
N = 10000
# Number of adds
d = 10 
ads_selected = []
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d

for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
        if (random_beta > max_random):
            max_random = random_beta
            ad = i

# Visualize the results in histogram
plt.hist(ads_selected)
plt.title('Histogram of Ads Selections')
plt.xlabel('SUV adds')
plt.ylabel('# of Times Ad Selected')
plt.show()