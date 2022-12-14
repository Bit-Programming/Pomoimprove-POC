import platform
import os


# Find the current OS, and run the pyinstaller command based on the OS, or say that the OS is not supported
if platform.system() == "Darwin":
	print('Pomoimprove does not yet support macOS. There are plans to implement macOS support, but for now, Pomoimprove only supports Windows.')
elif platform.system() == "Linux":
	print('Pomoimprove does not yet support GNU/Linux. There are plans to implement GNU/Linux support, but for now, Pomoimprove only supports Windows.')
elif platform.system() == "Windows":
	print('Coming soon.')
else:
	print('Pomoimprove does not support the operating system that you are running. Please use Windows for immediate support, or use macOS or GNU/Linux for eventual support.')
