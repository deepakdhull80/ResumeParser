import os 


def files(primary=True):
	pri="primary_file"
	sec="secondaryFile"
	# print(os.curdir)
	if primary:
		os.chdir(pri)
	else:
		os.chdir(sec)

	res=os.listdir()
	os.chdir("..")

	return res
# os.chdir("../primary_file")
# print(os.listdir())

# print(files(False))