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

# Visualize the results in histogram
plt.hist(ads_selected)
plt.title('Histogram of Ads Selections')
plt.xlabel('SUV adds')
plt.ylabel('# of Times Ad Selected')
plt.show()