Git
===

## Objectives

*  Learn a little about version control
*  Learn about cloning a repository
*  Learn a little about creating, pushing, and pulling


## Clone an existing repository

First, we are going to clone a repository. This means that we download and set up a link with an existing repository. It also means that we can pull all the changes made in it to our local machine. 

```
   git clone https://github.com/textcreationpartnership/Texts.git
```

This fetches the Texts repository from the *textcreationpartnership* project and creates it on our machine in its own directory. 

## Setting up a repository

First we need to create a repository and then add its location to your git
```
   git init
   git remote add origin https://github.com/<yourgithubname>/Luther.git
```

## Add

Now that you have an existing git directory and have given it a remote location to push into, we can now add some ffiles. This tells git that you want to add a file to version control and what you want to add. 

```
git add search.py
```

## Commit
Now that the data has been added, you need to commit it. You do this with git commit

```
git commit -m 'Adding search.py'
```

## Pull

Git uses a concept called branches, which we will not cover in this lecture. By default, every git repositoy contains a master branch. This is considered to be the main branch. 

```
    git pull origin master
```
It is good practice to use git pull before you push new code into the repository to allow you to synchronise data. 

## Push
Now we can move our code from our local machine to the online version. 
```
    git push origin master
```
