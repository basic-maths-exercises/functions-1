import matplotlib.pyplot as plt
import numpy as np

# Setup the grid of x values at which we will evaluate the function
xspacing = 20 / 499
xvalues = np.zeros(500)
for i in range(500) : xvalues[i] = -10 + i*xspacing

# Calculate y values for the quadratic y = -2x^2 + 4x - 8
# Set the parameters of the quadratic (notice how you can do this on one line)
a, b, c = -2, 4, -8 
# Now calculate the y values from the x values.
yvalues1 = np.zeros(500)
for i in range(500) : yvalues1[i] = a*xvalues[i]*xvalues[i] + b*xvalues[i] + c

# Calcualte y values for the quadratic y = x^2 + 4x 
# (I wrote this by doing a copy and paste of code above and modifying)
a, b, c = 1, 4, 0 
yvalues2 = np.zeros(500)
for i in range(500) : yvalues2[i] = a*xvalues[i]*xvalues[i] + b*xvalues[i] + c

# Calculate y values for the quadratic y = x^2 - 8
# (also did a copy and paste and modified)
a, b, c = 1, 0, -8 
yvalues3 = np.zeros(500)
for i in range(500) : yvalues3[i] = a*xvalues[i]*xvalues[i] + b*xvalues[i] + c

# Calcualte y values for the quadratic y = -x^2 + 2x + 4
a, b, c = -1, 2, -4 
yvalues4 = np.zeros(500)
for i in range(500) : yvalues4[i] = a*xvalues[i]*xvalues[i] + b*xvalues[i] + c

# Now plot all the curves
plt.plot( xvalues, yvalues1, "b-")
plt.plot( xvalues, yvalues2, "r-")
plt.plot( xvalues, yvalues3, "g-")
plt.plot( xvalues, yvalues4, "k-")
plt.savefig("quadratics.png")
