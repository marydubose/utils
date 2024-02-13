#Mary DuBose
#February 7, 2018
#This script converts GSRs saved as .bin files to the correct file extension (.tif or .pdf)

import os
import shutil

#for all files in S:\Data\MLGW\GSR\GSRIMAGES_new, need to copy & rename with the right file extension

for root, subfolders, filelist in os.walk(r"H:\MLGW\GSRS_2022\U of M Delivery 05.01.23\U of M Delivery 05.01.23"):
	for file in filelist:
		try:
			current_path = os.path.join(root, file)
			size = os.path.getsize(current_path)
			new_path = os.path.join(r"H:\MLGW\images_May2023", file)
			f = open(current_path, 'rb')
			line = f.readline()
			if line.startswith(b"II*"):
				new_path = new_path[:-4]
				new_path += ".tif"
			elif line.startswith(b"%PDF"):
				new_path = new_path[:-4]
				new_path += ".pdf"
			else:
				print(line)
				break
			shutil.copy2(current_path, new_path)
		except IOError:
			break
		finally:
			f.close()