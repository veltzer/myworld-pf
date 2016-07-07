#!/usr/bin/python3

'''
This script preps eclipse for my use by installing cdt and vrapper
on it

TODO:
- check if the feature exists (see my eclipse notes about how to do that)
and only install the feature if it is missing.
'''

###########
# imports #
###########
import subprocess # for check_call

##############
# parameters #
##############
# show progress?
progress=True
# debug
debug=False
# what features do I want installed?
features=[
	'org.eclipse.cdt',
	'net.sourceforge.vrapper',
]

########
# code #
########
for feature in features:
	if progress:
		print('doing feature [{0}]'.format(feature))
	args=[
		'./eclipse',
		'-nosplash',
		'-application',
		'org.eclipse.equinox.p2.director',
		'-repository',
		'http://download.eclipse.org/releases/neon/',
		'-installIU',
		feature+'.feature.group',
	]
	if debug:
		subprocess.check_call(args)
	else:
		subprocess.check_call(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
