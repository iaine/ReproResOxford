Visualising the Data
====================


## Objectives

*  Create an image of the data

In this part, we learn about creating reusable figures from the data that we have searched. 

Open *search.py* and add in a new library to import. 

```
from ggplot import *
```
This is an image library that is used with pandas.

````
plt = ggplot(aes(x="Publication",y="Freq"), data = n) + geom_point() \
    + ggtitle("Works attributed to Luther") + xlab("Publication Date") \
    + ylab("Number of publications")

plt.save("Luther.png")
````

The library uses a function called aes, short for aesthetics, to tell ggplot what columns the image is available and where the data is coming from.

The geom_point() tells ggplot how we want to show the data. 

As part of this, we are tell ggplot about the axes titles and titles that we will add to our image for our paper. 


Finally the image is then saved as an image file. We have now taken a data source, found some data, applied a small transformation, and then created an image for a paper, presentation or a blog.  

We should add this into the git repository.  
