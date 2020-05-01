import numpy as np
import matplotlib.pyplot as pt
import sklearn.preprocessing as sk

x=np.arange(-2, 1, 0.01)
y= np.cos(x)

pt.plot(x, y) # Create line plot with yvals against xvals
pt.show()

