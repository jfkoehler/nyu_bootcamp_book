#!/usr/bin/env python
# coding: utf-8

# ### Python Fundamentals I (Part II)

# ---
# ## Printing (and help)
# 
# It's important in the sense that if we don't tell the computer to report or "print" the results, then generally we will not see it. 
# 
# First, let's practice using the help command by `print?`

# In[1]:


get_ipython().run_line_magic('pinfo', 'print')


# So a window should pop up showing things that (i) values must be seperated by commas, when it is printed how to seperate them, what to do at the end, etc.

# In[2]:


get_ipython().run_line_magic('pinfo', 'abs')


# In[3]:


#print two variables
a = 1
b = 'steve'
print(a, b, sep = '--')


# In[4]:


# try using \n
print(a, b, sep = '\n\n\n')
a


# Notice all the white space, this is what the character `\n` does, it stands for a return or jump to the next line. 

# ---
# ## Strings

# This is where I think python is VERY POWERFULL...lots of enviorenments can do numerical calculations, plotting well, but handling and manipulating strings is less common...
# 
# * **Lesson 1:** A string is a collection of characters between quotation marks
# 
# * **Lesson 2:** A string may look like a number, but it is not. '12'/3 this is not going to work as "12" is a string, python does not see it as a number, and then it is being asked to perform a numerical computation on something that is not a number, thus an error message.

# In[5]:


a = "some"
b = "thing"
#concatenate
a + b


# In[6]:


#printing variables and f strings
print("these are some variables", a, b)


# In[7]:


print(f'This is variable a: {a}')


# ---
# ### Time to practice
# 
# Below are a set of excercises, take a couple of minutes and (i) create a code cell below each one and (ii) try and answer them as best as possible. If we don't cover them all inclass, try and attempt them later as you review.

# **Exercise.** What happens if we run the statement: 'Chase'/2? Why?

# In[8]:


'Chase'/2


# **Exercise.** This one's a little harder. Assign your first name as a string to the variable firstname and your last name to the variable lastname.  Use them to construct a new variable equal to your first name, a space, then your last name. Hint: Think about how you would express a space as a string.

# In[16]:


firstname = 'Jacob'
lastname = 'Koehler'
fullname = firstname + " " + lastname
print(fullname)


# In[19]:


fullname2 = f'{firstname} {lastname}'
print(fullname2)


# In[21]:


ex = 12.435666
print(f'{ex: .2f}')


# **Exercise.** Set s = 'string'. What is s + s? 2*s? s*2? What is the logic here?

# In[17]:


s = 'string'
print(s + s, 2*s, s*2)


# ---
# ## Quotation Marks
# 
# Here is the thing, you'll notice that sometimes I use single quotation, double quotation marks...
# * First, both are valid ways to define a string. The real issue is my inconsistent use partly this is a problem within the NYU databoot camp team...I actually prefer double.
# * Second, the fact that both are valid is not an accident, in fact, double quotation marks and even **triple** quotation marks play an important roles. 

# In[26]:


# single vs. double
print('This is a string')
print("This is also a string")
print("I'm hungry")


# **Note** how in the last line of code I can use the apostrophe. This is the value added of double quotation marks in that it can handle more complicated punctuation within the quoation marks. 
# Now what about this...

# In[28]:


# skipping lines
ex_string2 = """this is an 
example that I wanted to run on"""


# Here triple quotation marks allow us to have multiple lines.

# ---
# ### Time to practice
# 
# **Exercise.** In the Four score etc code, replace the triple double quotes with 
# triple single quotes. What happens?

# **Exercise.** Fix this code:

# In[30]:


bad_string = "Sarah's code"

print(bad_string)


# **Exercise.** Which of these are strings? Which are not? Edit the markdown cell and type next to each one string, not string.
# * apple
# * "orange" 
# * 'lemon84'
# * "1" 
# * string 
# * 4 
# * 15.6 
# * '32.5'

# ---
# ## Lists

# **Key concept:** A list is an ordered collection of items. This will obviously be important as data will naturally come in a list or list like form. Moreover, this will also give us our first taste of "slicing" or grabbing specific elements of a list. 

# In[31]:


# Some examples of listis...
alist = [1, 2, 3]
print(alist)


# Now what is really cool is that you can have a list with different types...

# In[32]:


# list with different types
alist2 = ['a', 'b', 1, 2.4]
print(alist2)


# So notice that the first part of the list is an integer, then a string, then the variable a (which currently is a string as well) Then there is the combining of list... so here is this awesome example

# In[33]:


# combine lists
alist + alist2 


# So notice what this did here, it litterally took randomlist and then added it to the stringlist, so we have a new list that combines all of this
# 
# What do you think this does...

# In[34]:


# list of lists
another_list = [alist, alist2]
print(another_list)


# VERY INTERESTING....This took the two lists and the created another list which is composed of two lists!!! A "List of Lists"

# Final point, the book does not talk about this yet, [later it does](https://nyudatabootcamp.gitbook.io/thebook/py-fun2), but its worth understanding the "ordered" part...this means for each item in the list we can call that item with its order in the list or number. Key: Python starts from the number 0, so the first item in a list is item number
# zero...Lets try some stuff

# In[37]:


#indexing the list
alist2[0] #the first item in the list
alist2[-1] #the last item in the list


# ### Time to practice

# **Exercise.** How would you explain a list to a classmate?

# In[ ]:





# **Exercise.** Add `print(numberlist)` and `print(variablelist)` to your code and note 
# the format of the output. What do the square brackets tell us? The single 
# quotes around some entries?

# In[ ]:





# **Exercise.** What is the output? How would you explain it to a classmates?

# In[38]:


a = 1
b = '2'
c = 'three'
d = [1, 2, 3]
mixedlist = [a, b, c, d]
print(mixedlist)


# In[41]:


print(mixedlist[-1][1])


# **Exercise.** Suppose `x = [1, 2, 3]` is a list. What is `x + x`? `2*x`? Try them and see.

# In[39]:


x = [1,2,3]
print(x + x, 2 * x)


# **mtwn** One thing that is interesting here is that (for those of you with prior experince in math or computing), you may be thinking that a numerical operation on a list will be like a vector operiation (a list looks similar to a vector). But it does not. In this sense the list operations are more general, usable for doing things like expanding the list, combining lists, etc. If we want to perform vector-like operations, then we need to change the type and import the `numpy` package. We will see this later.

# In[42]:


x + 3


# In[43]:


x[0] = 'steve'
print(x)


# ---
# ## Tuples
# 
# Tuples are very similar to lists, but the key issue is once a tuple is set, then the entries in it cannot be changed. This is what they call "immutability" of a tuple. In contrast, in a list you can change individual elements. Let's see this. 
# 
# 
# test_tuple = (1,2,3) # Similar to a list, but round brackets...
# 

# In[44]:


numberlist = [1, 2, 3]


# In[45]:


print(numberlist)
numberlist[0] = 328
print(numberlist) # Note how I changed the fist entry int he list!!!


# Now here is a tuple...like with a list, individual elements are seperated by a comma. Unlike a list, we see round brackets, not square. 

# In[46]:


test_tuple = (1,2,3) # Similar to a list, but round brackets...
print(test_tuple)


# And again, notice that when it is printed out we see the round brakcets indicating that it is a tuple.

# In[47]:


test_tuple[0] = 328 # UNCOMMENT THIS PART OF THE CODE TO UNDERSTAND 


# This won't run "TypeError: 'tuple' object does not support item assignment" meaning, that once set you can not assignment new values... This is the immutability property of a tuple.

# ---
# 
# ## Dictionaries
# 
# Dictionaries are (unordered) pairs of things defined by curly brackets {}, separated by commas, with the items in each pair separated by colon. We use them a fair amount of time for several reasons: One they are great for creating (small) table like datasets that can be converted to a DataFrame. Second, they are great for converting some value in your data. In one example, I had a dataset that had education catagorized by a string like ["primary", "secondary"] and I wanted to covert it into years of schooling. So I used a dictionary that mapped the words into years. Third, we often come accross them as a data structure generated by APIs. 
# 
# For example, here is a list of first and last names:

# In[48]:


# create a dictionary
ex_dict = {'name': 'Lenny', 'age': 2}
print(ex_dict)


# In[49]:


# extract a value
ex_dict['name']


# What about this...

# In[50]:


# extract a key
ex_dict['Lenny']


# In[51]:


ex_dict.keys()


# What happend here... we can't go from values to keys with a dictionary. The main idea is a dictionary is a one-to-many data structure. That means we must have unique keys (this is the one part)...but different keys can have the same value (this is the many part). This implies that going backwards from values to keys is not possible. 
# 
# For example, we can...

# In[52]:


#reassign a value
ex_dict2 = {'names': ['Lenny', 'Hardy'], 'ages': [2, 3]}
print(ex_dict2)


# In[53]:


ex_dict2['names'] = ['Jacob', 'Erika']
ex_dict2


# ### Time to practice
# 
# **Exercise.** Print the names. Does it come out in the same order we typed it?

# In[ ]:





# **Exercise.** Construct a dictionary whose keys are the integers 1, 2, and 3 and whose values are the same numbers as words: one, two, three. How would you get the word associated with the key 2?

# In[ ]:





# **Exercise.** Enter the code
# 
# ```
# d = {'Donald': 'Duck', 'Mickey': 'Mouse', 'Donald': 'Trump'}
# 
# print(d)
# ```
# 
# What happened?

# In[ ]:





# **Exercise.** Consider the dictionary
# 
# ```
# data = {'Year': [1990, 2000, 2010], 'GDP':  [8.95, 12.56, 14.78]}
# 
# ```
# 
# What are the keys here? The values? What do you think this dictionary represents?

# In[ ]:





# ---
# ## Built in Functions
# 
# We have already seen several ones, e.g., `whos` which tells what variables are defined and some properties (type, value) as well. Then we have seen the `print` function which will print the results on the screen. Here are some other ones we will use all the time
# * `len` tells us the lenght of the list, string, dictionary etc.
# * `type` tells us the type of the variable, e.g. a list, sting, float, integer, dictionary...
# Here are some examples

# In[54]:


print(len('hello world')) # note how len is "counting how many characters" 
                          # And it is including the white space...
    
print(len([1, 5, -3])) # How many times in the list

print(len((1, 5, -3))) # how many items in the tuple

print(len('1234')) # String, so how many characters

print(len('12.34')) # Again, a string....


# In[55]:


len(12.34) # same issue with a floating point number...


# Then this is the type command...

# In[56]:


print(type(2)) # Its saying an integer

print(type(2.5)) # A floating point number, or float

print(type('2.5')) # Looks like a number, but a string

print(type('something')) # String

print(type([1, 5, -3])) # Here it sees that this is a list...

print(type((1, 5, -3))) # A tuple


# What is a floating point number...this is **mtwn** but the basic idea is that numbers can not be stored in the computers memory with infinite precision (why? a computers memory is not infinite), so they are approximated. With a 64-bit computer and double precision arithmatic this is about to 16 digits. 

# ---
# ## Changing types

# Types matter a lot in python, but sometimes we will want to change the type of a varible. This is something that will come up often in our data work....

# In[57]:


s = '12.34' # This is a string (check it to veryify...)

f = float(s) # This builtin function will convert the string to a float

print(type(f)) # It should now tells us that f is a float...

s = "12"

i = int(s) # This should convert the string to an integer...what if we did the 
            # string "12.34"??? 

print(type(i)) # This should be a type integer...


# Then we can always convert it back....

# In[ ]:


s = str(12) # So start with an integer and go to a string...
print('s has type', type(s))

t = str(12.34) # Or start with a float and go to a string as well
print('t has type', type(f))


# **Big picture** This is again a super powerful aspect of python that makes it very applicable for working with data...the ability to go from numbers to strings and back.

# In[ ]:


# This is cool...start with a string and make it a list by the command list
x = 'abc'

y = list(x)

print(y) # So now y should be a list of a, b, c


# ### Time to practice

# **Exercise.** What happens if we apply the function float to the string 'some'?

# **Exercise.** What is the result of `list(str(int(float('12.34'))))`? 
# Why? Hint: Start in the middle (the string '12.34') and work your way out, 
# one step at a time. This is similar to question 13 and 14 on Code Practice #1. 

# **Exercise.** How would you convert the integer i = 1234 to the 
# list l = ['1', '2', '3', '4']? This is similar to question 18 on Code Practice #1. Lets do that one instead. 

# **Exercise (challenging).** This one is tricky, but it came up in some work we  were doing. Suppose year is a string containing the year of a particular piece of data; for example, year = '2015'. 
# How would we construct a **string** for the following year?

# ---
# ## Programming Errors 
# 
# Fact of life: **you will make errors.** Many errors. The key to programming is (i) not getting discouraged and living with that fact and (ii) learning how to make sense of error messages and **self-correct** those errors. 
# 
# Point (i) is a life skill that takes years to learn. However, we can help you with (ii), below we talk through some very common error messages and how to identify them. 

# ### Name Error
# It happens when we use something not defined, it could be a variable or a function. The associated output is an error message that includes (i) what line the issue is occuring in and (ii) the name that could not be found. Here are two examples:

# In[ ]:


# Using not defined variable
print(NotDefined)


# In[ ]:


# Another situation, here we are 
# using function that is not defined.
log(3) 


# So you see in both of these instances that there is an arrow pointing to the line within each code cell. In the first instance it is pointing to line 2. This is where the issue is. In the second instance, it is pointing to line number 3. 
# 
# And after pointing to the issue, below that is says ``NameError:`` and stuff. In the first instance, it tells us `NotDefined` is well...not defined. In the second instance, its saying the same thing. It just does not know what log is.  

# ### Type Error
# This one happens all the time too. It happens when an inappropriate operation or function is applied to that specific data type. Here are some examples:

# In[ ]:


x = "2"
y = 2

z = x + y


# Like above, it tells us that line number 4 is the issue, i.e. where we are tying to add "2" and 2. And the issue is a type issue, we can't add two different types (in this case a string and an integer).

# Here is another example relating to tuples. Recall that with a tuple, the data type is immutable. That is it can't be changed. But lets try and change it...

# In[ ]:


tuple_error=(2,3)
tuple_error[0]=5


# Here it says, line 2...there is a problem. A ``TypeError`` problem. And what is the specific issue, well the tuple object does not support this kind of operation.
# 
# **Important** A lot of the problams in interperting the error message lies in deciphering the cryptic messages like "'tuple' object does not support item assignment" So how do we do this...**use google** Often the first result will be a question posted to [www.stackoverflow.com](www.stackoverflow.com) which is a place for programers to ask and answer questions. This is a good place to be comfortable with and seek help from. 
# 
# **Excercise:** In the google search area type "tuple' object does not support item assignment" What did you find? 
# 

# ### Invalid Syntax
# 
# Syntax errors can be detected before your program begins to run. These types of errors are usually typing mistakes (fat fingers), but migth be hard to find out at first. Here we give two examples:

# In[ ]:


# Define a simple list and let's call the first one in the list
randomlist =[1,8,3,7]
randomlist[0]]


# I know this example may seem easy to identify, but imagine when you write a long code like below, it could be hard. Can you find where is missing?
# 

# In[ ]:


goal_model_data = pandas.concat([train[['HomeTeam','AwayTeam','HomeGoals']].assign(home=1).rename(
                columns={'HomeTeam':'team', 'AwayTeam':'opponent','HomeGoals':'goals'}),
               train[['AwayTeam','HomeTeam','AwayGoals']].assign(home=0).rename(
                columns={'AwayTeam':'team', 'HomeTeam':'opponent','AwayGoals':'goals'}])


# In[ ]:


# Or when we define a string
bad_string = 'code"


# ### Key Error
# Python raises a *KeyError* whenever a `dict()` object is requested (using the format `a = adict[key]`) and the key is not in the dictionary.

# In[ ]:


names = {'Dave': 'Backus', 'Chase': 'Coleman', 'Spencer': 'Lyon', 'Glenn': 'Okun'}
names['David']


# ### "No Idea" Errors
# 
# These are errors that you have no idea what is going on. A couple of tips:
# - **Ask a friend.** While the movie vision of a coder is some guy in a hoody in a dark room by himself, this is not how we work. Working together, as a team, is an important aspect of data analysis and coding in general. So if you have a problem, ask for help. Explain to him/her what you were trying to do (often just this process helps solve the issue) and then show them the output.
# 
# - **Google fu** Use google. Chances are you are not the first one to have this problem. Just cut and past the error message into google and track down what other people have to say about it.
# 

# ---
# ## Summary

# **Congratulations!** First, it's amazing that you have made it this far. Reflect on what you knew before working through this notebook. Now reflect on what you can do...AMAZING!!! Let us summarize some key things that we covered.
# 
# 
# * **Assignments and variables**: We say we assign what's on the right to the thing on the left: x = 17.4 assigns the number 17.4 to the variable x.
# * **Data types and structures**:
#     * Strings. Strings are collections of characters in quotes: 'this is a string'.
#     * Lists. Lists are collections of things in square brackets: [1, 'help', 3.14159].
#     * Number types: integers vs. floats. Examples of integers include -1, 2, 5, 42. They cannot involve fractions. Floats use decimal points: 12.34. Thus 2 is an integer and 2.0 is a float.
#     * Dictionary. Dictionaries are collections of unordered things in `{}` with key-value pairs: names = {'Dave': 'Backus', 'Chase': 'Coleman'}.
# 
#     
# * **Built-in functions**: 
#     * The `print()` function. Use `print('something', x)` to display the `value(s)` of the `object(s)` in parentheses.
#     * The `type()` function. The command `type(x)` tells us what kind of object x is. Past examples include integers, floating point numbers, strings, and lists.
#     
# * **Type conversions**: 
#     * Use `str()` to convert a float or integer to a string. 
#     * Use `float()` or `int()` to convert a string into a float or integer. 
#     * Use `list()` to convert a string to a list of its characters.
# 
# * **Error message types**:
#     * NameError. Usually happens when using something not defined which could be variable or methods.
#     * TypeError. Raise when an operation or function is applied to an object of inappropriate type. For example, tuples have no `"="` methods while number no `len`.   
#     * Invalid syntax. Syntax errors can be detected before your program begins to run. So first thing to do is to check typos, parentheses, etc.
#     * KeyError. It happens when you refer a key not previously defined in the dictionary. 
# 
# ### Useful Tricks and Programming Tools
# 
# * **Comments.** Use the hash symbol # to add comments to your code and explain what you’re doing. Don't underestimate the importance of creating well commented code. Here are some thoughts on this...
#     - https://blogs.msdn.microsoft.com/oldnewthing/20070406-00/?p=27343
#     - https://blog.codinghorror.com/when-understanding-means-rewriting/
# 
# 
# * **Help.** We can get help for a function or method foo by typing `foo?` in the IPython console or foo in the Object explorer. Try each of them with the `type()` function to remind yourself how this works.
# 
# * **Error Messages** Look at the message, (i) read where the issue is and (ii) track down what the message is associated with that line. Or ask a friend!

# In[ ]:




