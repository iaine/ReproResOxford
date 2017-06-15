'''
   Script to search EEBO catalogue
'''

import csv
import numpy as np
from ggplot import *

raw = open("/Users/iain.emsley/git/Texts/TCP.csv", 'r')
reader = csv.reader(raw, delimiter=",", quotechar='"')
authors = {}
mentions = {}
x = list(reader)
data = np.array(x).astype('str')

#g=pd.read_csv("/Users/iain.emsley/git/Texts/TCP.csv")
#f=g.loc[g['Author'].str.contains("Luther",na=False)]
#f["Freq"] = f.groupby('Date')['Date'].transform('count')
#ggplot(aes(x="Date",y="Freq"), data = f) + geom_point()

for d in data:
    # test for Luther being in the author column
    if "Luther" in d[5]:
        authors[int(d[6])] = d[5]
    # Luther may be mentioned but it not an author
    elif "Luther" in d[7] and "Luther" not in d[5]:
        mentions[d[0]] = d[5]

#set up the date range
dates =range(1480,1700)
aut_date = [k for k,v in authors.items()]
date = []
for d in dates:
    if d in aut_date:
        date.append(d)
    else:
        date.append(0)

#men_date = [k for k,v in mentions.iteritems()]

#now to plot the publications against date
ggplot(aes(x="year",y="Number of titles"), data = aut_date) + geompoint()
