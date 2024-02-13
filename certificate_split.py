#Mary DuBose
#May 1, 2019
#This script takes scanned Use & Occupancy booklet certificates that are
#multi-page PDFs wtih each page containing 2 certificates, and splits them
#into the individual certificates, naming them with the permit number.

import copy
import math
import os
import sys
import PyPDF2

cert_dir = r'C:\temp\Certificates\3000-3005'
new_dir = r'F:\zoning\Index_Cards\Certificates_Misc'
err_dir = r'F:\zoning\Index_Cards\Certificates_Misc\errors'
split_dir = r'F:\zoning\Index_Cards\Certificates_Misc\split'
spliterr_dir = r'F:\zoning\Index_Cards\Certificates_Misc\errors\split'

for root, subfolder, filelist in os.walk(cert_dir):
	for file in filelist:
		num_string = file[:-4] #should remove the .pdf from end of filename?
		nums = num_string.split('-')
		try:
			permit_nums = [int(x) for x in nums]
			if len(permit_nums) != 2:
				print(permit_nums)
			else:
				check = (permit_nums[1] - permit_nums[0] + 1)/2
				full_path = os.path.join(root, file)
				pdf_file = PyPDF2.PdfFileReader(full_path)
				pages = pdf_file.getNumPages()
				if pages != check: #this means numbering won't be right so don't do anything, just print info
					print(root + '\\' + file)
					print("Pages: " + str(pages))
					print("Check: " + str(check))
					page_index = permit_nums[0]
					for page in range(pages):
						if page_index > max(permit_nums):
							print(page_index)
						pdf_writer = PyPDF2.PdfFileWriter()
						pdf_writer.addPage(pdf_file.getPage(page))
						outfile = err_dir + '\\' + str(page_index) + '.pdf'
						with open(outfile, 'wb') as out:
							pdf_writer.write(out)
						page_index += 2
				else: #split each PDF into pages before splitting pages in half
					page_index = permit_nums[0]
					for page in range(pages):
						if page_index > max(permit_nums):
							print(page_index)
						pdf_writer = PyPDF2.PdfFileWriter()
						pdf_writer.addPage(pdf_file.getPage(page))
					
						outfile = new_dir + '\\' + str(page_index) + '.pdf'
						with open(outfile, 'wb') as out:
							pdf_writer.write(out)
						page_index += 2

		except ValueError:
			print(file)
		
			
#split each page in half			
for page in os.listdir(new_dir):
	full_path = os.path.join(new_dir, page)
	if os.path.isdir(full_path):
		continue
	inp = PyPDF2.PdfFileReader(full_path)
	output1 = PyPDF2.PdfFileWriter()
	output2 = PyPDF2.PdfFileWriter()
	
	permit = [str(c) for c in page if c.isdigit()]
	p1 = ''
	for num in permit:
		p1 += num
	p1 = int(p1)
	p2 = p1 + 1
	p1, p2 = str(p1), str(p2)
	
	p = inp.getPage(0)
	q = copy.copy(p)
	q.mediaBox = copy.copy(p.mediaBox)
	
	x1, x2 = p.mediaBox.lowerLeft
	x3, x4 = p.mediaBox.upperRight
	
	x1, x2 = math.floor(x1), math.floor(x2)
	x3, x4 = math.floor(x3), math.floor(x4)
	x5, x6 = math.floor(x3/2), math.floor(x4/2)
	
	p.mediaBox.upperRight = (x3, x4)
	p.mediaBox.lowerLeft = (x1, x6)
	
	q.mediaBox.upperRight = (x3, x6)
	q.mediaBox.lowerLeft = (x1, x2)
	
	output1.addPage(p)
	output2.addPage(q)
	
	out1 = split_dir + '\\' + p1 + '.pdf'
	with open(out1, 'wb') as outfile:
		output1.write(outfile)
	out2 = split_dir + '\\' + p2 + '.pdf'
	with open(out2, 'wb') as outfile:
		output2.write(outfile)
		
for page in os.listdir(err_dir):
	full_path = os.path.join(err_dir, page)
	if os.path.isdir(full_path):
		continue
	inp = PyPDF2.PdfFileReader(full_path)
	output1 = PyPDF2.PdfFileWriter()
	output2 = PyPDF2.PdfFileWriter()
	
	permit = [str(c) for c in page if c.isdigit()]
	p1 = ''
	for num in permit:
		p1 += num
	p1 = int(p1)
	p2 = p1 + 1
	p1, p2 = str(p1), str(p2)
	
	p = inp.getPage(0)
	q = copy.copy(p)
	q.mediaBox = copy.copy(p.mediaBox)
	
	x1, x2 = p.mediaBox.lowerLeft
	x3, x4 = p.mediaBox.upperRight
	
	x1, x2 = math.floor(x1), math.floor(x2)
	x3, x4 = math.floor(x3), math.floor(x4)
	x5, x6 = math.floor(x3/2), math.floor(x4/2)
	
	p.mediaBox.upperRight = (x3, x4)
	p.mediaBox.lowerLeft = (x1, x6)
	
	q.mediaBox.upperRight = (x3, x6)
	q.mediaBox.lowerLeft = (x1, x2)
	
	output1.addPage(p)
	output2.addPage(q)
	
	out1 = spliterr_dir + '\\' + p1 + '.pdf'
	with open(out1, 'wb') as outfile:
		output1.write(outfile)
	out2 = spliterr_dir + '\\' + p2 + '.pdf'
	with open(out2, 'wb') as outfile:
		output2.write(outfile)
		
		