'''
   Script to search EEBO catalogue
'''
#uncomment if using Jupyter
#output_notebook()

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import output_notebook

authors=pd.read_csv("data/TCP.csv")
luther=authors.loc[authors['Author'].str.contains("Luther",na=False)]
freq = luther['Date'].value_counts()
freq_data = pd.DataFrame({'Publication':freq.index, 'Freq':freq.values})
freq_data = freq_data.sort_values(by=["Publication"])

plot = figure(title="Plot of Publications mentioning Luther by Year", plot_width=800, plot_height=400)

plot.circle(freq_data['Publication'], freq_data['Freq'])
plot.xaxis[0].axis_label = 'Date'
plot.yaxis[0].axis_label = 'Number of Items'
show(plot)

# create a new plot with a datetime axis type
yearly = authors_df[['Date','Title']].groupby(['Date']).count().reset_index()
yearly.describe()
# create a new plot with a datetime axis type
plot2 = figure(plot_width=1200, plot_height=250)

plot2.line(yearly['Date'], yearly['Author'], color='navy')

show(plot2)
