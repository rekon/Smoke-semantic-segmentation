import glob
from subprocess import call

for filename in glob.glob("*.*"):
	new_filename = filename.replace(' ','_')
	call('rename \"'+filename+'\" '+new_filename, shell=True)
	print('renamed file', filename)
