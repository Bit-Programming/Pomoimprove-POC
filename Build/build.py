import platform


# Set the "os" variable to the current OS
os = platform.system()

# Find the current OS, and run the pyinstaller command based on the OS, or say that the OS is not supported
if os == "Darwin":
	print("This application does not yet support macOS. There are plans to implement macOS support, but for now, this application only supports Windows.")
elif os == "Linux":
	print("This application does not yet support GNU/Linux. There are plans to implement GNU/Linux support, but for now, this application only supports Windows.")
elif os == "Windows":
	print("IMPLEMENT LATER")
else:
	print("This application does not support the operating system that you are running. Please use Windows for immediate support, or use macOS or GNU/Linux for eventual support.")
