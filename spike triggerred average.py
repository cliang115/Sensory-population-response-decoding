#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 23:47:30 2017

@author: chen
"""

import numpy as np
import matplotlib.pyplot as plt
import pickle
from compute_sta import compute_sta
FILENAME = 'H1 neuron.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)
    
stim = data['stim']
rho = data['rho']
    
sampling_period = 2
num_timesteps = 150

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')