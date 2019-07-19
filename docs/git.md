Git
===

## Objectives

*  Learn a little about version control
*  Learn about cloning a repository
*  Learn a little about adding, pushing, and pulling

## Version Control

Code and data change. Version control tracks how code and changes. 

Imagine that you are working on a paper with multiple collaborators, each of whom has a suggestion. One way os to use track changes in Word or version history in Google Docs.

Once changes are accepted, it is hard to follow the history and to understand the flow. 

Version Control starts from the initial document and stores the versions in a discoverable manner.  

## Fork a repository

First we will copy a repository online. 

Sign into your Github account. 

Go to http://github.com/iaine/ReproResOxford

Click on the 'fork' button. This copies my repository into your own space when you click the button. 

## Clone an existing repository

First, we are going to clone a repository. This means that we download and set up a link with an existing repository. It also means that we can pull all the changes made in it to our local machine. 

```
   git clone https://github.com/iaine/ReproResOxford.git
```

This fetches the repository with data from the *textcreationpartnership* project and creates it on our machine in its own directory. 

## Add

Now that you have an existing git directory and have given it a remote location to push into, we can now add some files. This tells git that you want to add a file to version control and what you want to add. 

```
git add search.py
```

## Commit
Now that the data has been added, you need to commit it. You do this with git commit

```
git commit -m 'Adding search.py'
```

This adds the file to the staging area, ready to be added to Github. When you commit, you have to add a message for the log. This should be short but meaningful so that you understnand the change added. 

## Pull

Git uses a concept called branches, which we will not cover in this lecture. By default, every git repository contains a master branch. This is considered to be the main branch and alsways ready to be run.  

```
    git pull origin master
```
It is good practice to use git pull before you push new code into the repository to allow you to synchronise data. 

It allows your local version to come up to date with any other changes before you send your changes to the main branch. You may find that you have a merge issue, it can be fixed early on. 

## Push

Now we can move our code from our local machine to the online version. 

```
    git push origin master
```

Using git push origin, we tell the local git to push the committed changes to the online repository. 
