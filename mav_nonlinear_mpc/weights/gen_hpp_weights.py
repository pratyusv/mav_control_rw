#!/usr/bin/python

import numpy as np
import os,fnmatch

data_dir = os.listdir("./wt")

pattern = "*weight*.npy"

file_names = []

for file in data_dir:
	if (fnmatch.fnmatch(file,pattern)):
		print(file[:-4])
		file_names.append(file)

# exit()
text_file = open("mc_weights.c","w")

params = ""

for file in file_names:
	data = np.load("./wt/" + file)

	params += "#define " + str(file[:-4]).upper() +"_ROWS " + str(data.shape[0]) + "\n"
	params += "#define " + str(file[:-4]).upper() +"_COLS " + str(data.shape[1]) + "\n"

	params += "\n"

	params += "#define "+ str(file[:-4]).upper() + " "
	print(file)
	print(data.shape)
	for rows in range(data.shape[0]):
		for cols in range(data.shape[1]):
			params += str(data[rows][cols])+" ,"

	params = params[:-1]

	params += "\n\n"


	



text_file.write(params)
text_file.close()