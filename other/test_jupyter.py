# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-27 11:05:24
@UpdateDate: 2019-09-29 13:40:14
@Description: jupyter学习
'''

#%%
msg = "Hello World!"
print(msg)


#%%
import os
lst = [ x for x in range(10)]
for filename in os.listdir("."):
    a, b = os.path.split(filename)


#%%
import pandas as pd
import numpy as np
import matplotlib as plt
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
ts.plot()


#%%
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 

#%% [test]
