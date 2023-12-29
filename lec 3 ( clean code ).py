import os 
os.system("cls")

# clean code important than formatting
# and having standard formatting
# make maintainability easy
# not something a machine  ...  script not recognize it ( but it professionals and can decide )
# meaning of the "language" is part from " programming language" communicate our ideas to other developer

## importance of having clean code
# to maintain code 
# managing a successful project
# agile development " التطوير السريع "

# Technical debt is pppproblem in program by take bad decision 
## the code will be harder to change it in future than now

## expection we can use uncleann code
# simple script for a one-off task
# Code competitions
# proof concept اثبات المقهوم
# developing a prototype
# When maintenance old code to short time

## code formating
# pep-8 is the well-known standard for spacing , name , line length, and more
# clean code is beyond-يتجاوز coding standards
# Clean code is about achieving quality , and building a srtong system maintainable

## PEP-8 foucs on improve the readability and make it easy 
# The style guide evolves over time

## rule of pep-8
# use 4 space
# use hanging indents for continuation lines
# use small letters for funcution and upper for variable (constant)
# use spaces around operators and after commas
# make max of line is 79 characters
# use docstrings to document your code

## style guide 
# Searchability : ability to identify special sympol 
# Consistency : if code has uniform format make read easy 
# Better error handling : one of the suggestions in PEP-8 is limit the amount of code in try ... except 
# Code quality : when look to code in structured way , it will be proficient-لمحه to understanding ... and know bugs and fix it
# simplicity : every funncition do one task

## Documentation
# we documment code .... from concept code
# intends to explore docstrings and annotations because we use it in documment code 
# itis important to documment code because values or objects may be lost in dynamically typed

## Code comments
# we have to less the comments as poosible

## Docstrings """ """
# use it to describe class and we can know it by ==> help()

## Annotations
# the main idea of it is hint what is the code do 
# Annotations is used to select kind of variable 
# we can reuse this abstraction in more parts of our code
# it give us access to a dictionary that maps the name of the annotations
# when checking the code through annotations, this is when PEP-484 comes 

# in first version of python  the way to document the types of the parameters is docstrings
# for dynamic and nested data types, it is always a good idea to provide examples of the expected data

# Checking type consistency
# the consistency from things we need to check it automatically
# we can then use 
# annotations along with some tooling to automatically check for errors 
# automitic check first check pep-8 then check for the use of types on code 
