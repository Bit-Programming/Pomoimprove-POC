import platform
import os
import shutil
from pyunpack import Archive


# Find the current OS, and run the pyinstaller command based on the OS, or say that the OS is not supported
if platform.system() == 'Darwin':
	print('Pomoimprove does not yet support macOS. There are plans to implement macOS support, but for now, Pomoimprove only supports Windows.')
elif platform.system() == 'Linux':
	print('Pomoimprove does not yet support GNU/Linux. There are plans to implement GNU/Linux support, but for now, Pomoimprove only supports Windows.')
elif platform.system() == 'Windows':
	if not os.path.exists(os.getcwd() + '/Chrome/'):
		os.chdir(os.path.dirname(__file__))
		os.chdir('../PROGRAM/')
		Archive('Chrome.7z').extractall(os.getcwd())
	os.chdir(os.path.dirname(__file__))
	os.system('cmd /c "pyinstaller windows.spec"')
	shutil.rmtree(os.getcwd() + '/build/', ignore_errors=True)
else:
	print('Pomoimprove does not support the operating system that you are running. Please use Windows for immediate support, or use macOS or GNU/Linux for eventual support.')
