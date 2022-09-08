#!/usr/bin/env python
# coding: utf-8

# # Python Fundamentals 1 
# 
#   
# ##  Outline
# 
# Time to start programming! We work our way through some of the essentials of Python's core language. We will do this within a Jupyter Notebook and along the way, become familiar Markdown as well as other properties of the notebook environment. 
# 
# [This notebook largely follows the discussion in the Book.](https://nyudatabootcamp.gitbook.io/thebook/py-fun1)
# 
# ### Python
# 
# We will learn elementary syntax, calculations, assignments, and as well as python data types, e.g., floats, strings, lists, dictionaries, and built-in functions. We'll also discover some typical bugs and ways to identify, and fix.
# 
# **Buzzwords.** Isn't that enough?
# 
# **Trigger warning.** Technical content, cannot be mastered without effort.

# ---
# 
# ## Jupyter Notebook & Markdown Warmup 

# ### Jupyter Notebook Essentials
# 
# **Opening Jupyter**
# 
# If you are reading this, you've done it already. But just a reminder...
# 
# * Open your terminal (command prompt on Windows)
# 
# * Type `jupyter notebook` and press enter.  This will open a tab in your browser with the word Jupyter at the top and your computer's directory structure below it.
# 
# * In the browser tab, navigate to your `Data_Bootcamp` directory/folder.
# 
# * Click on the New button in the upper right and choose `Python 3` (it may also refer to this as `Python[Root]`.

# In your browser, you should have an empty notebook with the word Jupyter at the top.  Below it is a **menubar** with the words File, Edit, View, Cell, Kernel, and Help.  

# **Downloading a Jupyter Notebook from Github**
# * First go to the notebook github page and then click on *Raw*.
# * Then, Right click or press command+s (ctrl+s if you are using windows) to save it as .ipynb.
# * Go to location where you saved .ipynb file.
# * Open file, you will see the code.
# 

# **Playing with Jupyter**
# * Change the notebook name.  Click on the name (`Untitled` if we just created a new notebook) to the right of the word Jupyter at the top. A textbox should open up.  Use it to change the name to `bootcamp_sandbox`.
# * Toolbar buttons.  Let your mouse hover over one of them to see what it does.
# * Add a cell.  Click on the `+` in the toolbar to create a new cell. 
# * Keyboard shortcuts.

# ### Markdown Essentials

# Markdown is a simplified version of html ("hypertext markup language"), the language used to construct basic websites. It has a zen-like simplicity and beauty.

# * **Headings**.  Large bold headings are marked by hashes (`#`).  One hash for first level (very large), two for second level (a little smaller), three for third level (smaller still), four for fourth (the smallest).  Try these in a Markdown cell to see how they look:
# 
#    ```
#    # Data Bootcamp sandbox
#    ## Data Bootcamp sandbox
#    ### Data Bootcamp sandbox
#    ```
# 
#   Be sure to run the cell when you're done (`shift enter`).

# * **Bold and italics**.  If we put a word or phrase between double asterisks, it's displayed in bold.  Thus `**bold**` displays as **bold**.  If we use single asterisks, we get italics:  `*italics*` displays as *italics*.

# * **Bullet lists**.  If we want a list of items marked by bullets, we start with a blank line and mark each item with an asterisk on a new line:
# 
#   ```markdown
#   * something
#   * something else
#   ```

# * **Links**.   We construct a link with the text in square brackets and the url in parentheses immediately afterwards.  Try this one:
#   ```
#   [Data Bootcamp course](http://nyu.data-bootcamp.com/)
#   ```

# We can find more information about Markdown under Help.  Or use your [Google fu](https://www.urbandictionary.com/define.php?term=google-fu).

# **Exercise.** Ask questions if you find any of these steps mysterious:
# 
# * Close Jupyter.
# 
# * Start Jupyter.
# 
# * In Jupyter, open an new Ipython notebook within your Data_Bootcamp directory/folder, point to the code cell, the name of the notebook, and the help button.
# 
# * Save the file bootcamp_class_pyfun1 in your This file will serve as your notes for this class.
# * Create a description cell in Markdown at the top of your notebook. It should include your name and a description of what you're doing in the notebook. For example: "Mike Waugh's first notebook for Python fundamentals 1" and a date.

# ---
# ## Simple Calculations and Assignment
# 
# Literally the "bread and butter" of scientific computation...let's get started:
# 
# 

# In[1]:


# simple multiplication


# In[2]:


# add some white space, nice feature of python is that it is not sensitve to this..


# In[3]:


# add some more...


# In[4]:


# What about division...


# In[5]:


# What about module...


# **Side note** Note how in the cell I have comments that are not interperted by python. To create comments simply type ``#`` and then what ever comment you want to make. Comments are **important** because they help make your code readable. 

# In[6]:


### exponents


# In[7]:


test = log(3) # what do you think will happen here...log is not defined
              # log is not a built-in function who will have a different color in notebook
print(test)


# Note how the compute just stopped. It did not compute. Remember, python and the computer are DUMB! You gave it an instruction that it did not know what to do, so it stopped, and did not proceed. A couple of points about this:
# 
# * The top to bottom (within a code cell), simply following instructions/commands nature of a program.
# 
# * When you run this, note how (after some stuff) tells you where the problem is: Line 1, then this name log is not defined.

# **Assignment** Above I've been assigning variables... but let's look at this more closely...

# In[6]:


# x = 2


# Nice so the thing on the left is the "variable" named "x", then the thing on the right is the value that this variable is assigned... then the = sign is the operator that assighns that value.

# In[7]:


#print x

#define y


# Now we are getting somewhere, we take these variables and perform an operation. Notice that (like excel) the value assigned to z will change as we change the values assigned to x or y. But there is a difference with excel...what is it?

# In[8]:


# variable z is quotient


# Here is a place where you might want to figure out what variables there are within the enviornment. For example, what is `x`  (the type and size ignore for now) and then the value...how do you do this, with the `whos` command, which will provide this information. 

# In[10]:


#whos


# This is a nice feature in that it is a way for you to always understand what variables are in your environment at any point in time, their type, etc. 
# 
# ---
# 
# #### Time to practice
# 
# We will do this alot. Here is the deal: Below are a set of excercises, take a couple of minutes and (i) create a code cell below each one and (ii) try and answer them as best as possible. If we don't cover them all inclass, try and attempt them later as you review.

# **Exercise.** Type `w = 7` in a cell.  In the same cell, next line below, type `w = w + 2`. In the next line below type `w` (so we can see the output). What does this code do?  Why is this not a violation of basic mathematics?

# **Exercise.** In another code cell type `w = w + 2` and then `w` below it (again so we can see the output). Evaluate this cell once. Do it again. Do it again. What is going on here?

# **Exercise.**  Suppose we borrow 200 for one year at an interest rate of 5 percent.  If we pay interest plus principal at the end of the year, what is our total payment?  Compute this using the variables `principal = 200` and `i = 0.05`.

# **Exercise.** Real GDP in the US (the total value of things produced) was 15.58 trillion in 2013 and 15.96 trillion in 2014.  What was the growth rate?  Express it as an annual percentage.

# **Exercise (challenging).**  Suppose we have two variables, `x` and `y`.  How would you switch their values, so that `x` takes on `y`'s value and `y` takes on `x`'s?

# **Exercise (challenging).**  Type `x = 6` in a cell.  We've reassigned `x` so that its value is now 6, not 2. If we type and submit `z`, we see
# 
# ```
# In [10]: z
# Out[10]: .6666666666
# ```
# 
# But wait, if `z` is supposed to be `x/y`, and `x` now equals 6, then shouldn't `z` be 2? What do you think is going on?
