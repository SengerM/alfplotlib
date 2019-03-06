import matplotlib.pyplot as plt
import os
import datetime
from time import sleep

__alfplotlib_installation_path = os.path.dirname(os.path.abspath(__file__))

plt.style.use(__alfplotlib_installation_path + '/alfplotlib/' + 'alfrc_style')

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

def save_all_figs(timestamp=False, mkdir=None, image_format='png', *args, **kwargs):
	"""
	Use this function to save all plots in the current session at once.
	
	Arguments
	---------
	timestamp : bool or str, optional
		If true then all file names will be identified with one (and the
		same) timestamp.
		If 'now' then the timestamp is generated at the time you call the
		save_all function.
		This is usefull when you want not to overwrite the plots each 
		time you run your code.
		Default value is False.
	mkdir : str or None, optional
		If a string is passed then a directory will be created (with the
		specified name) and all figures will be saved in there. If None,
		all figures will be saved in the current working directory.
		Default value is 'figures'.
	image_format : string, optional
		Format of image files. Default is 'png'. 
	"""
	if mkdir is not None:
		directory = mkdir + '/'
	else:
		directory = '.'
	if timestamp is True:
		directory += __gen_timestamp()
	if not os.path.exists(directory):
		os.makedirs(directory)
	figs_list = [plt.figure(n) for n in plt.get_fignums()]
	for k in range(len(figs_list)):
		file_name = figs_list[k].canvas.manager.window.wm_title()
		figs_list[k].savefig(directory + '/' + file_name + '.' + image_format, *args, **kwargs)
