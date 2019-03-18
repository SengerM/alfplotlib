import matplotlib.pyplot as plt
import numpy as np
import alfplotlib as apl # This automatically loads the "alf style" for the plots. You can define your own styles, see this for more info → https://matplotlib.org/users/customizing.html

x = np.linspace(-2,2)
fig, ax = plt.subplots()
ax.plot(x, x**2)
ax.plot(x,x**3)
ax.plot(x,np.sin(2*np.pi*x))

apl.save_all_figs(mkdir='my_figs') # Save all the figs at once.
