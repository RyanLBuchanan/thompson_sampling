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
# N_i(n)
numbers_of_selections = [0] * d
# R_i(n)
sums_of_rewards = [0] * d
total_reward = 0