import os
from PIL import Image

folder = r'S:\Data\Zoning2\ScannedDocuments\Microfilm_frames\OCCE-BP-024\frames\gray'
new_folder = r'S:\Data\Zoning2\ScannedDocuments\Microfilm_frames\OCCE-BP-024\frames\gray\flipped'

for file in os.listdir(folder):
	if file.endswith('tif') and int(file[13:17]) > 1313:
		img_path = os.path.join(folder, file)
		new_path = os.path.join(new_folder, file)
		try:	
			with Image.open(img_path) as img:
				rot = img.rotate(180)
				out = rot.transpose(Image.FLIP_LEFT_RIGHT)
				out.save(new_path)
				
		except OSError:
			print(path)
			continue
		
		except Exception as e:
			print(e)
			continue