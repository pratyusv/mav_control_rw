#!/usr/bin/python

import numpy as np
text_file = open("mc_std.h","w")

params = "#ifndef INCLUDE_STD_H_"
params += "\n" 
params += "#define INCLUDE_STD_H_"
params += "\n\n"

data = np.load("./wt/std.npy")

params += "#define STD_ROWS " + str(data.shape[0]) + "\n"
# params += "#define " + str(file[:-4]).upper() +"_COLS " + str(data.shape[1]) + "\n"

params += "\n"

params += "#define STD "
for rows in range(data.shape[0]):
	# for cols in range(data.shape[1]):
	params += str(data[rows])+" ,"

params = params[:-1]

params += "\n\n"
params += "#endif"


	



text_file.write(params)
text_file.close()