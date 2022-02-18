#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:44:14 2020

@author: laura
"""

import matplotlib.pyplot as plt
import numpy as np

n=[35,197,8500000]
f=[0.094,0.176,7.261622]
c=0.00268
t=np.zeros(10000000)
g=np.zeros(10000000)
for i in range(len(t)):
    t[i]=i
    g[i]=i*c

dados=plt.scatter(n,f,marker='*',color='navy',label="Dados")
linha,=plt.plot(t,g,label="g(n)=c*n",color='red',ls='-')
plt.xlabel("n=|V|+|A|")
plt.ylabel("Tempo(n=|V|+|A|) (s)")
plt.legend(handles=[dados,linha],loc='best')
plt.show()