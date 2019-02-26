#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 23:50:18 2017

@author: chen
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt


def compute_sta(stim, rho, num_timesteps):
  
    sta = np.zeros((num_timesteps,))
    

    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
    

    num_spikes = np.count_nonzero(spike_times)
    print (num_spikes)
    

    for spike in spike_times:
        spke = stim[(spike - num_timesteps):spike]
        sta += spke
    sta = sta / num_spikes
    return sta