# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 09:00:41 2018

@author: asd
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
x = np.random.randn(1000) #生产1000个随机数
D = pd.DataFrame([x,x+1]).T #构造两列
D.plot(kind = 'box') #画箱型图
plt.show()