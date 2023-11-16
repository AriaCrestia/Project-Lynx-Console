import platform

class SystemInfo:
	def Platform():
		return f"{platform.system()}"
	def ReleaseVer():
		return f"{platform.release()}"
	def FullInfo():
		return f"{platform.system()} {platform.release()}"