# alfplotlib
Functions to use with matplotlib

This intends to be the "evolution" of [nicenquickplotlib](https://github.com/SengerM/nicenquickplotlib). This time the approach will be different. The plotting task will be delivered to [Matplotlib](https://matplotlib.org/) and this collection of functions will operate on already created Matplotlib objects.

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

Example of usage
----------------

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
The default "alf style" looks like this:
<p align="center">
  <img width="460" src="https://github.com/SengerM/alfplotlib/blob/master/doc/usage_example/my_figs/Figure%201.png">
</p>
The code used to generate the previous plot can be found [here](https://github.com/SengerM/alfplotlib/tree/master/doc/usage_example).

#### The ```save_all_figs``` function
Its name says it all. This function saves all the plots you have made in the current session. You can find the source code and documentation in [this link](https://github.com/SengerM/alfplotlib/blob/master/alfplotlib/core.py). You can use most of the [```savefig```](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html) arguments with this function. For example ```apl.save_all_figs(format='pdf')``` will save the imaged in pdf format.

- ```save_all_figs``` example 1. Just save all your plots at once!
```Python
import matplotlib.pyplot as plt
import numpy as np
import alfplotlib as apl

for k in range(10):
	fig, ax = plt.subplots()
	ax.plot(np.linspace(-2,2)**k)

apl.save_all_figs() # Wow, you can save all the 10 figures that easy!?
```
- ```save_all_figs``` example 2. Use a timestamp in order to not overwrite your old plots. If you request to ```save_all_figs``` the usage of a timestamp, then it will create a new directory with a unique timestamp and the figures will be saved there. If you run the script multiple times the plots saved each time in a new directory. Example code:
```Python
import matplotlib.pyplot as plt
import numpy as np
import alfplotlib as apl

for k in range(10):
	fig, ax = plt.subplots()
	ax.plot(np.linspace(-2,2)**k)

apl.save_all_figs(timestamp=True) # Use the timestamp feature to not overwrite your images each time you save your plots.
```
- ```save_all_figs``` example 3. Create a new directory on the fly:
```Python
import matplotlib.pyplot as plt
import numpy as np
import alfplotlib as apl

for k in range(10):
	fig, ax = plt.subplots()
	ax.plot(np.linspace(-2,2)**k)

apl.save_all_figs(mkdir="my_figures") # Automatically create a directory to save your figures.
```
- ```save_all_figs``` example 4. Save the plotted data as csv files:
```Python
IN THE WISH LIST
```
