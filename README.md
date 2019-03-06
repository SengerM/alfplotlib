# alfplotlib
Functions to use with matplotlib

This intends to be the "evolution" of [nicenquickplotlib](https://github.com/SengerM/nicenquickplotlib). This time the approach will be different. The hard work will be delivered to [Matplotlib](https://matplotlib.org/) and this collection of functions will operate on already created Matplotlib objects.

Installation
------------

Make sure you have Pip installed, then open a terminal (cmd in Windows or any terminal in Ubuntu) and type:
- Python 2
```
pip install git+https://github.com/SengerM/alfplotlib
```
- Python 3
```
pip3 install git+https://github.com/SengerM/alfplotlib
```

First example of usage
----------------------

```Python
import matplotlib.pyplot as plt
import numpy as np
import alfplotlib as apl # This automatically loads the "alf style" for the plots.

x = np.linspace(-1,1)

fig, ax = plt.subplots()
ax.plot(x, x**2)
fig, ax = plt.subplots()
ax.plot(x,x**3)
fig, ax = plt.subplots()
ax.plot(x,np.sin(2*np.pi*x))

apl.save_all_figs(mkdir='my_figs') # Save all the figs at once.
```
