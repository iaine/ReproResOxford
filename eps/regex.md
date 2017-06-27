Searching for Data
==================

## Objectives

*  Write a script and add to Git
*  Use the cloned data and search for some data


In this episode, we want to use the data [cloned](git.md) taken from Git and then search for some data in it. An important part of reproducible research is showing your methodology and storing it.  

We are going to use a language called Python. 

Go into the repository that you've cloned and create a script in called *search.py*. (You can use notepad to create the file). 

We are going to import a library called pandas. This provides all the functions from that library for our script
.
```
import pandas as pd

g=pd.read_csv("data/TCP.csv")
f=g.loc[g['Author'].str.contains("Luther",na=False)]
freq = f['Date'].value_counts()
```

In this section, we read in the data from the [cloned repository](git.md) and store it in a variable to make it accessible for the script. 

In the next line, we find all lines containing the word, "Luther". We cannot guarantee how Martin Luther is 
represented within the data but we want to view all the relevant data. 

Although the data has authors and dates, what we want to show is a publication history of the number of volumes over time. In the final line, we create a version of the data that has the number of times a date appears in a variable.  


```
n = pd.DataFrame({'Publication':freq.index, 'Freq':freq.values})
```

In the inal line, the convert the freq variable into a form that the image library understands and also removes the duplicate Date column that the frequency creates. 

Now we have code, we add it to [version control](git.md) and can create our image. 
