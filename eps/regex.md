Searching for Data
==================

Objectives

*  Write a script and add to Git
*  Use the cloned data and search for some data


In this episode, we want to use the data [cloned](git.md) from Git and then search for some data in it. 

We are going to use a language called Python

Create a new directory and create a script in called *search.py*. (You can use notepad to create the file)

```
import csv
import numpy as np

raw = open("../git/Texts/TCP.csv", 'r')
reader = csv.reader(raw, delimiter=",", quotechar='"')
authors = []
mentions = []
x = list(reader)
data = np.array(x).astype('string')
```

In this section, we read in the data from the [cloned repository](git.md), read it into a variable to re-use.

The data is then turned into a list as np.array() expects a list and tell the new array that the list contains a string. 

```
for d in data:
    # test for Luther being in the author column
    if "Luther" in d[5]:
        authors.add(d[5])
    # Luther may be mentioned but it not an author
    else if "Luther" in d[7] and "Luther" not in d[5]:
        mentions.add(d[7])
```

Now we have code, we add it to [version control](git.md). 
