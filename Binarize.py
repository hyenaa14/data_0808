import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn. preprocessing import Binarizer

from pandas.plotting import scatter_matrix
header=['preg','plas','pres','skin','test','mass','pedi','age','class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)

array=data.values
X=array[:,0.8]
Y=[]

scaler=Binarizer(threshold=0.5)
rescaled_X
print(rescaled_X)

