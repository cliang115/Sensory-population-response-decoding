#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 17:54:33 2017

@author: chen
"""
import scipy.io

data = scipy.io.loadmat('tuning.mat')

import numpy as np

import matplotlib.pyplot as plt

plt.plot(np.transpose(data['stim']), np.transpose(data['neuron1']))

plt.plot(np.transpose(data['stim']), np.transpose(data['neuron2']))

plt.plot(np.transpose(data['stim']), np.transpose(data['neuron3']))

plt.plot(np.transpose(data['stim']), np.transpose(data['neuron4']))



a1 = max(np.mean(data['neuron1'], axis = 0))

b1 = max(np.mean(data['neuron2'], axis = 0))

z = np.degrees(np.arctan(np.mean(data1['r2'])/b1/np.mean(data1['r1'])*a1))
plt.plot(np.mean(data['neuron1']*10, axis = 0), np.var(data['neuron1']*10,axis = 0))
plt.plot(np.mean(data['neuron2']*10, axis = 0), np.var(data['neuron2']*10,axis = 0))
plt.plot(np.mean(data['neuron3']*10, axis = 0), np.var(data['neuron3']*10,axis = 0))
plt.plot(np.mean(data['neuron4']*10, axis = 0), np.var(data['neuron4']*10,axis = 0))