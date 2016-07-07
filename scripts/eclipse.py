#!/usr/bin/python3

# this script will create a workspace where eclipse can be launched
# put this project into the workspace and then launch eclipse
# this script also maximizes the eclipse window using the technique
# described in:
# http://unix.stackexchange.com/questions/103602/how-to-maximize-a-window-programmably-in-x-window

# TODO:
# - be able to run this script for two folders at one time (open eclipse for each).
# this will require that the workspace created will be unique (say tmpfile or something).
# this will also require that we signal the zoom of the window with that tmpfile id.

###########
# imports #
###########
import shutil # for rmtree
import os.path # for isdir
import subprocess # for check_call, DEVNULL
import time # for sleep

##############
# parameters #
##############
# where to put the workspace
folder='/tmp/workspace_current'
# where is the eclipse to run
eclipse=os.path.expanduser('~/install/eclipse-jee/eclipse')
# remove and recreate the workspace everytime?
remove_and_recreate=True
# debug the script?
debug=False

#############
# functions #
#############
def max_output(out):
	found_cnt=0
	found_id=None
	for x in out.split('\n'):
		fields=x.split()
		if debug:
			print(fields)
		if len(fields)>=2:
			name=' '.join(fields[2:])
			if name.endswith('Eclipse'):
				found_cnt+=1
				found_id=fields[0]
	if found_cnt==1:
		time.sleep(2)
		if debug:
			print('sending signal to ', found_id)
		subprocess.check_call([
			'wmctrl',
			'-i',
			'-r',
			found_id,
			'-b',
			'toggle,maximized_vert,maximized_horz',
		])
		return True
	else:
		return False

########
# code #
########

if remove_and_recreate:
	# remove the old folder
	if os.path.isdir(folder):
		shutil.rmtree(folder)
	# create the new folder
	os.mkdir(folder)

# run eclipse with the folder as the workspace
pid=os.fork()
if pid==0:
	# child
	subprocess.check_call([
		eclipse,
		'-nosplash',
		'-data',
		folder,
		'-pluginCustomization',
		'support/pluginCustomization.ini',
		'-fullscreen',
	], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
else:
	# parent
	# wait for child to appear as window and then maximize it
	for x in range(10):
		out=subprocess.check_output([
			'wmctrl',
			'-l',
		]).decode()
		if max_output(out):
			break
		else:
			time.sleep(2)
