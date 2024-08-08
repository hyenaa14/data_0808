import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from pandas.plotting import scatter_matrix
header=['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)


plt.clf()
pd.plotting.scatter_matrix(data)
plt.savefig('./result.scatter.png')