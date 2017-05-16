Visualising the Data
====================


## Objectives

*  Create an image of the data

In this part, we learn about creating reusable figures from the data that we have searched. 

Open *search.py* and go to the bottom of the code. 

```
aut_date = []

for k,v in author.iteritems():
    aut_date.add(k)

men_date = []

for k,v in mention.iteritems():
    men_date.add(k)
```

###Visualising the Data

Now we use the Python's matplotlib library  to create a figure.
```
import  matplotlib.pyplot as plt
```

````
#now to plot the publications against date
plt.figure(figsize=(16,8))
plt.plot(dates, aut_date, 'r.', dates, men_date, 'b.')
plt.ylabel('Number of individual titles')
plt.xlabel('Year')
plt.title('Publications by Martin Luther or mentioning him')
plt.axvline(x=1546)
plt.show()
````
