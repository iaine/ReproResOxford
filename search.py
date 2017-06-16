'''
   Script to search EEBO catalogue
'''

import pandas as pd
from ggplot import *

g=pd.read_csv("/Users/iain.emsley/git/Texts/TCP.csv")
f=g.loc[g['Author'].str.contains("Luther",na=False)]
freq = f['Date'].value_counts()
n = pd.DataFrame({'Publication':freq.index, 'Freq':freq.values})

plt = ggplot(aes(x="Publication",y="Freq"), data = n) + geom_point() \
    + ggtitle("Works attributed to Luther") + xlab("Publication Date") \
    + ylab("Number of publications")

plt.save("Luther.png")
