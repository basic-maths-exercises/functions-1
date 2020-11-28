# Introduction to python functions

You can use a program similar to the one you have written to plot the majority of functions that you will encounter during your undergraduate degree.  By completing the last exercise you have thus learned something that will serve you well as you continue to study mathematics.

In `main.py`, I have written code to plot a quadratic using the Python commands that you have just learned about.  I have also put comments in my code to explain what I did.  Each comment line starts with a # sign so:

````
# This is a comment
a = "This is a python command"
`````

__Try to understand my code by reading the comments and then run the code that I have written in the cell on the left.__   When you run the code a graph showing plots of multiple quadratics will appear.    

I wrote the code in the box on the left by writing a program similar to the one that you wrote for the last exercise.  I then did three copy and pastes of the code to evaluate the y values and made suitable modifications to get the values for the different quadratics that I needed.  __WRITING CODE USING COPY AND PASTE IN THIS WAY IS VERY BAD. YOU SHOULD ALWAYS TRY TO AVOID DOING THIS.__   The reason copy, pasting and modifying code is bad is that you end up writing very long programs and, as you have learned, your objective should always be to write less code and to thus make fewer mistakes. 

We can avoid doing using copy and paste and shorten our programs by writing functions.  Functions are bits of code that we can call multiple times with a single command.  The block below illustrates how Python functions work.    This block shows how we can write a short program to generate a graph showing two linear functions:

````
import matplotlib.pyplot as plt
import numpy as np

# Setup the x values at which we will evaluate the function 
xspacing = 20 / 499
xvalues = np.zeros(500)
for i in range(500) : xvalues[i] = -10 + i*xspacing 

# Here is a function that evaluates the y values for our linear function
def linear( m, c ) : 
    yvalues = np.zeros(500)
    for i in range(500) : yvalues[i] = m*xvalues[i] + c 
    return yvalues

# Now call the function to evaluate the y values for y = 2x + 4
yvalues1 = linear( 2, 4 )
# Now call the function to evaluate the y values for y = -x -3
yvalues2 = linear( -1, -3 )

# And plot the graphs
plt.plot( xvalues, yvalues1, 'b-' )
plt.plot( xvalues, yvalues2, 'r-' )
plt.savefig( "linear.png" )
````

Within the code above when:

````
yvalues1 = linear( 2, 4 )
````

is written.  The code within the function called linear is run with `m=2` and `c=4`:

````
def linear( m, c ) : 
    yvalues = np.zeros(500)
    for i in range(500) : yvalues[i] = m*xvalues[i] + c 
    return yvalues
````

The return statement at the end ensures that `yvalues1` is set equal to `yvalues`.

__To see if you have understood Python functions write a function called `quadratic` in the cell on the left.  Then use this function to replace all the copy and pasted code.__
