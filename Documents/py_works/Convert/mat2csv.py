import pandas as pd
import scipy
from scipy import io
#%%
data = scipy.io.loadmat(r"C:\Users\H\Documents\Lab_BUPT\Data\Convert\disper_AOM1.mat")
print(data)
print(data.keys()) #查看mat的名字
#%%
x = data['dispersion_data']
print(type(x))
print(x)
#%%
df = pd.DataFrame(x)
df.to_csv(r"C:\Users\H\Documents\Lab_BUPT\Data\Convert\disper_AOM1.CSV", index=False)
#%%