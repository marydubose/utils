# Mary DuBose
# June 2, 2023
# This script generates QR codes for the TDOT pollinator placards.

import os
import segno
import xlrd

urls = {}
dir = r"S:\Tech\medubose\TDOT\qr_codes"

xl = r"S:\Tech\medubose\TDOT\plantlist.xls"

wb = xlrd.open_workbook(xl)
ws = wb.sheet_by_index(0)

for row in range(ws.nrows):
	if row > 0:
		url = ws.cell(row, 5).value
		try:
			split = url.split("=")
			id = split[1]
			urls[id] = url
		except IndexError:
			print(url)
		
for key, value in urls.items():
	filename = key + ".png"
	fullpath = os.path.join(dir, filename)
	qr = segno.make(value, version=4)
	qr.save(fullpath, scale=8)
	print(filename)