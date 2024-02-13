import os
from zipfile import ZipFile

folder = r"S:\GIS_Projects\TDOT\LiDAR\HaywoodCounty"

for item in os.listdir(folder):
	if item.endswith("zip"):
		fullpath = os.path.join(folder, item)
		with ZipFile(fullpath, "r") as zipObj:
			zipObj.extractall(folder)