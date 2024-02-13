#Mary DuBose
#October 3, 2019
#This script formats the Excel sheets to be used for extracting addresses from 
#the OPD microfilm files.
#It also converts the tif files to PDFs.

import img2pdf
import os
import xlrd
import xlwt

excel_dir = r"F:\zoning\Microfilm\OPD_Excels_Final"
microfilm_dir = r"S:\Data\Zoning2\ScannedDocuments\Microfilm"
pdf_dir = r"F:\zoning\Microfilm\Microfilm_Casefiles"
papercase_dir = r"S:\Data\Zoning2\ScannedDocuments\PaperCaseFiles"

roll_names = []
roll_paths = {}

for workbook in os.listdir(excel_dir):
	roll = workbook[:-5]
	roll_names.append(roll)
	
for root, subfolder, filelist in os.walk(microfilm_dir):
	for folder in subfolder:
		if folder in roll_names:
			int_path = os.path.join(root, folder)
			full_path = os.path.join(int_path, "frames")
			roll_paths[folder] = full_path
			
for workbook in os.listdir(excel_dir):
	excel_in = os.path.join(excel_dir, workbook)
	wb = xlrd.open_workbook(excel_in)
	ws = wb.sheet_by_index(0)
	for row in range(ws.nrows):
		if row > 0:
			img_old = ws.cell(row, 0).value
			img_new = ws.cell(row, 1).value
			if img_old != "":
				if not img_old.endswith("tif"):
					img_old += ".tif"
			if img_new != "":
				img_new += ".pdf"
			if img_old != "" and img_new != "":
				roll = workbook[:-5]
				rpath = roll_paths[roll]
				tif_path = os.path.join(rpath, img_old)
				pdf_path = os.path.join(pdf_dir, img_new)
				try:
					with open(pdf_path, "wb") as f:
						f.write(img2pdf.convert(tif_path))
				except TypeError:
					print("Error converting file: " + tif_path)
					continue
					
new_files = []
					
for pdf in os.listdir(pdf_dir):
	new_files.append(pdf)
	
proceed = input("List of new PDFs is created. Now move the PDFs to the correct folders and enter Y when complete. ")

addr_dict = {}

if proceed == 'Y':
	for root, subfolder, filelist in os.walk(papercase_dir):
		for file in filelist:
			if file in new_files:
				full_path = os.path.join(root, file)
				addr_dict[file] = full_path
				
excel_out = r"F:\zoning\MicrofilmAddressExtraction.xls"
wb = wlxt.Workbook()
ws = wb.add_sheet("Sheet1")
row = 0

for key, value in addr_dict.items():
	ws.write(row, 0, value)
	ws.write(row, 1, key)
	row += 1
	

	