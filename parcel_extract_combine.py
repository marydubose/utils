import os
import urllib.request
from zipfile import ZipFile
# from qgis.core import *

output_dir = r"S:\GIS_Projects\TDOT\Pollinator_Study\parcels\Comptroller"
county_file = os.path.join(output_dir, "counties.txt")

county_list = []
with open(county_file, "r") as infile:
	txt = infile.read()
	lines = txt.split("\n")
	for line in lines:
		parts = line.split()
		county_list.append(parts[0])
		
exclude = ["Chester", "Davidson", "Hamilton", "Hickman", "Knox", "Montgomery", "Rutherford", "Shelby", "Sumner", "Williamson"]
		
urlbase = "https://comptroller.tn.gov/content/dam/cot/pa/documents/landuse/maps/parcel-maps-data/"

for county in county_list:
	if county not in exclude:
		outfile = county + ".zip"
		outpath = os.path.join(output_dir, outfile)
		requrl = urlbase + outfile
		urllib.request.urlretrieve(requrl, outpath)
		
		with ZipFile(outpath, "r") as zipObj:
			zipObj.extractall(output_dir)

# QgsApplication.setPrefixPath(r"C:/PROGRA~1/QGIS3~1.16/apps/qgis-ltr", True)

# qgs = QgsApplication([], False)

# qgs.initQgis()

# for county in county_list:
	# if county not in exclude:
		# shppath = os.path.join(output_dir, county, "Parcels.shp")
		# new_shp = county + ".shp"
		# outshp = os.path.join(output_dir, new_shp)
		# processing.run("native:dissolve", {'INPUT':shppath, 'OUTPUT':outshp})

# qgs.exitQgis()


import os
indir = r"S:\GIS_Projects\TDOT\Pollinator_Study\parcels\Comptroller"
for item in os.listdir(indir):
    fullpath = os.path.join(indir, item)
    if os.path.isdir(fullpath):
        origpath = os.path.join(fullpath, "Parcels.shp")
		fixpath = os.path.join(fullpath, "Parcels_fix.shp")
		processing.run("native:fixgeometries", {'INPUT':origpath, 'OUTPUT':fixpath})
        new_shp = item + ".shp"
        outshp = os.path.join(indir, new_shp)
        processing.run("native:dissolve", {'INPUT':fixpath, 'OUTPUT':outshp})