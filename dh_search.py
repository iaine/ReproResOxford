'''
    Script to search for an author in EEBO index 

'''
import pandas as pd
from ggplot import *

g = pd.read_csv("data/TCP.csv")
author = g.loc[g["Author"].str.contains("Luther", na=False)]
freq = author["Date"].value_counts()

n = pd.DataFrame({'Publication':freq.index, 'Freq': freq.values})

plt = ggplot( aes(x="Publication", y = "Freq"), data = n) + geom_point() \
    + ggtitle("Works attributed to Luther") + xlab("Publication Date") \
    + ylab("Number of Publications")

plt.save("Luther.png")
