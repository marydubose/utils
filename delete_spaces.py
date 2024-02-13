#Mary DuBose
#July 15, 2019
#This script goes through the scanned paper casefiles, looks for any file names with spaces,
#and renames the files with the spaces removed.

import os
import shutil

casefiles = r"S:\Data\Zoning2\ScannedDocuments\PaperCaseFiles"

for root, subfolder, filelist in os.walk(casefiles):
	for file in filelist:
		if " " not in file:
			continue
		else:
			old_file = os.path.join(root, file)
			new_name = file.replace(" ", "")
			new_file = os.path.join(root, new_name)
			shutil.copy2(old_file, new_file)
			os.remove(old_file)
