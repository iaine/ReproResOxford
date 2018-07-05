'''
   Script to search EEBO catalogue
'''
#uncomment if using Jupyter
#%matplotlib inline

import pandas as pd
from ggplot import *

authors=pd.read_csv("data/TCP.csv")
luther=authors.loc[authors['Author'].str.contains("Luther",na=False)]
freq = luther['Date'].value_counts()
freq_data = pd.DataFrame({'Publication':freq.index, 'Freq':freq.values})
freq_data = freq_data.sort_values(by=["Publication"])

plt = ggplot(aes(x="Publication",y="Freq", weight="Publication"), data = freq_data) + geom_point() \
    + ggtitle("Works attributed to Luther") + xlab("Publication Date") \
    + ylab("Number of publications")

plt.save("Luther.png")
