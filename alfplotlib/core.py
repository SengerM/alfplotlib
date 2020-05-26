import matplotlib.pyplot as plt
import os
import datetime
from time import sleep

__alfplotlib_installation_path = os.path.dirname(os.path.abspath(__file__))

plt.style.use(__alfplotlib_installation_path + '/rc_styles/alfrc_style')

def __gen_timestamp():
	"""
	Returns a numeric string with a timestamp. It also halts the execution 
	of the program during 10 micro seconds to ensure that all returned
	timestamps are different and unique.
	
	Returns
	-------
	str
		String containing the timestamp. Format isYYYYMMDDHHMMSSmmmmmm.
	
	Example
	-------	
	>>> get_timestamp()
	'20181013234913378084'
	>>> [get_timestamp(), get_timestamp()]
	['20181013235501158401', '20181013235501158583']
	"""
	timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
	sleep(10e-6) # This ensures that there will not exist two equal timestamps.
	return timestamp

def set_fig_name(fig, name):
	"""
	Use this function to set a name for each figure which will be used when
	"save all figs" function is called.
	"""
	fig.set_label(name)

def save_all_figs(timestamp=False, mkdir=None, format='png', facecolor=(1,1,1,0), *args, **kwargs):
	"""
	Use this function to save all plots in the current session at once.
	
	Arguments
	---------
	timestamp : bool, optional 
		Default: False
		If true then all file names will be identified with one (and the
		same) timestamp. The timestamp is created at the moment this 
		function is called. If you call this function twice, you'll have 
		two different timestamps.
		This is usefull when you want not to overwrite the plots each 
		time you run your code. Let's say you are doing a simulation and you
		want to keep the plots of each different run, then you can use
		"timestamp = True".
	mkdir : str or None, optional
		Default: None
		If a string is passed then a directory will be created (with the
		specified name) and all figures will be saved in there. If None,
		all figures will be saved in the current working directory.
		Default value is 'figures'.
	format : string, optional
		Default: 'png'
		Format of image files. Default is 'png'. 
	"""
	if mkdir is not None:
		directory = mkdir + '/'
	else:
		directory = './'
	if timestamp is True:
		directory += __gen_timestamp()
	if not os.path.exists(directory):
		os.makedirs(directory)
	figs_list = [plt.figure(n) for n in plt.get_fignums()]
	for k in range(len(figs_list)):
		for ax in figs_list[k].axes:
			ax.grid(b=True, which='minor', color='#000000', alpha=0.1, linestyle='-', linewidth=0.25)
		file_name = figs_list[k].get_label()
		if file_name == '':
			file_name = __gen_timestamp()
		figs_list[k].savefig(directory + '/' + file_name + '.' + format, format=format, facecolor=facecolor, *args, **kwargs)
